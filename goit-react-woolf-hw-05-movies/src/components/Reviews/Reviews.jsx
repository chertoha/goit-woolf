import ErrorComponent from 'components/ErrorComponent';
import LoadingWrapper from 'components/LoadingWrapper';
import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { getReviews } from 'services/api';
import { Author, Item, List, Review, Wrapper } from './Reviews.styled';

const Reviews = () => {
  const [reviews, setReviews] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const { movieId } = useParams();

  useEffect(() => {
    setIsLoading(true);
    setError(null);

    getReviews(movieId)
      .then(({ results }) => {
        setReviews(results);
      })
      .catch(err => {
        setError(err.message);
      })
      .finally(() => {
        setIsLoading(false);
      });
  }, [movieId]);

  return (
    <LoadingWrapper error={error} isLoading={isLoading}>
      <Wrapper>
        {reviews.length > 0 ? (
          <List>
            {reviews.map(({ id, author, content }) => (
              <Item key={id}>
                <Author>Author: {author}</Author>
                <Review>{content}</Review>
              </Item>
            ))}
          </List>
        ) : (
          <ErrorComponent message="Here are no reviews yet" />
        )}
      </Wrapper>
    </LoadingWrapper>
  );
};

export default Reviews;
