import PropTypes from 'prop-types';
import { Message, Wrapper } from './ErrorComponent.styled';
import Container from 'components/Container';

const ErrorComponent = ({ message }) => {
  return (
    <Container>
      <Wrapper>
        <Message>{message}</Message>
      </Wrapper>
    </Container>
  );
};

export default ErrorComponent;

ErrorComponent.propTypes = {
  message: PropTypes.string.isRequired,
};
