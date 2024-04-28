import PropTypes from 'prop-types';
import { StyledButton } from './Feedback.styled';

const FeedbackButton = ({ onClick, value }) => {
  return (
    <StyledButton type="button" onClick={onClick}>
      {value}
    </StyledButton>
  );
};

export default FeedbackButton;

FeedbackButton.propTypes = {
  onClick: PropTypes.func.isRequired,
  value: PropTypes.string.isRequired,
};
