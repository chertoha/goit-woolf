import PropTypes from 'prop-types';
import { createImageUrl } from 'utils/createImageUrl';
import {
  Genres,
  Heading1,
  Heading2,
  Meta,
  Overview,
  StyledImage,
  Wrapper,
} from './MovieCard.styled';

const MovieCard = ({ title, poster_path, overview, genres }) => {
  return (
    <Wrapper>
      <StyledImage
        src={
          !poster_path
            ? `${process.env.PUBLIC_URL}/no-image.png`
            : createImageUrl(poster_path)
        }
        alt={title}
      />

      <Meta>
        <Heading1>{title}</Heading1>

        <Heading2>Overview</Heading2>
        <Overview>{overview}</Overview>

        {genres && genres.length > 0 && (
          <>
            <Heading2>Genres</Heading2>
            <Genres>
              {genres[0]?.name &&
                genres.map(({ name }) => <span key={name}>{name}&nbsp;</span>)}
            </Genres>
          </>
        )}
      </Meta>
    </Wrapper>
  );
};

export default MovieCard;

MovieCard.propTypes = {
  title: PropTypes.string,
  poster_path: PropTypes.string,
  overview: PropTypes.string,
  genres: PropTypes.arrayOf(
    PropTypes.shape({
      name: PropTypes.string,
    })
  ),
};
