import Container from 'components/Container';
import Section from 'components/Section';
import MovieList from 'components/MovieList';
import LoadingWrapper from 'components/LoadingWrapper';
import { Heading, ListWrapper } from './Home.styled';
import { useEffect, useState } from 'react';
import { getTrendings } from 'services/api';

const Home = () => {
  const [movies, setMovies] = useState([]);
  const [error, setError] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    setIsLoading(true);
    setError(null);
    getTrendings()
      .then(({ results }) => {
        setMovies(results);
      })
      .catch(err => {
        setError(err.message);
      })
      .finally(() => {
        setIsLoading(false);
      });
  }, []);

  return (
    <Section>
      <Container>
        <Heading>Trending today</Heading>

        <LoadingWrapper isLoading={isLoading} error={error}>
          <ListWrapper>
            {movies.length > 0 && <MovieList list={movies} />}
          </ListWrapper>
        </LoadingWrapper>
      </Container>
    </Section>
  );
};

export default Home;
