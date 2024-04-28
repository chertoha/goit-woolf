import PropTypes from 'prop-types';
import MovieItemLink from './MovieItemLink';
import { Item, List } from './MovieList.styled';

const MovieList = ({ list }) => {
  return (
    <List>
      {list.map(({ id, title }) => (
        <Item key={id}>
          <MovieItemLink href={`/movies/${id}`} title={title} />
        </Item>
      ))}
    </List>
  );
};

export default MovieList;

MovieList.propTypes = {
  list: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.number.isRequired,
      title: PropTypes.string.isRequired,
    })
  ).isRequired,
};
