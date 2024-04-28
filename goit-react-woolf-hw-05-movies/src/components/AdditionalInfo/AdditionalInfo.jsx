import PropTypes from 'prop-types';
import {
  Heading2,
  Item,
  List,
  StyledLink,
  Wrapper,
} from './AdditionalInfo.styled';

const AdditionalInfo = ({ location }) => {
  return (
    <Wrapper>
      <Heading2>Additional information:</Heading2>

      <List>
        <Item>
          <StyledLink to="cast" state={{ from: location }}>
            Cast
          </StyledLink>
        </Item>
        <Item>
          <StyledLink to="reviews" state={{ from: location }}>
            Reviews
          </StyledLink>
        </Item>
      </List>
    </Wrapper>
  );
};

export default AdditionalInfo;

AdditionalInfo.propTypes = {
  location: PropTypes.object,
};
