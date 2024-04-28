import ErrorComponent from 'components/ErrorComponent';
import LoadingWrapper from 'components/LoadingWrapper';
import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { getCast } from 'services/api';
import { createImageUrl } from 'utils/createImageUrl';
import { Character, Image, Item, List, Name, Wrapper } from './Cast.styled';

const Cast = () => {
  const [cast, setCast] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const { movieId } = useParams();

  useEffect(() => {
    setIsLoading(true);
    setError(null);

    getCast(movieId)
      .then(({ cast }) => {
        setCast(cast);
      })
      .catch(err => {
        setError(err.message);
      })
      .finally(() => {
        setIsLoading(false);
      });
  }, [movieId]);

  return (
    <LoadingWrapper isLoading={isLoading} error={error}>
      <Wrapper>
        {cast.length > 0 ? (
          <List>
            {cast.map(({ cast_id, character, name, profile_path }) => (
              <Item key={cast_id}>
                <Image
                  src={
                    !profile_path
                      ? `${process.env.PUBLIC_URL}/no-image.png`
                      : createImageUrl(profile_path)
                  }
                  alt={name}
                />
                <Name>{name}</Name>
                <Character>Character: {character}</Character>
              </Item>
            ))}
          </List>
        ) : (
          <ErrorComponent message="There are no cast here" />
        )}
      </Wrapper>
    </LoadingWrapper>
  );
};

export default Cast;
