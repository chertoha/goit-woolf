import PropTypes from 'prop-types';
import FeedbackButton from './FeedbackButton';
import { List, Item, Wrapper } from './Feedback.styled';

const Feedback = ({ options }) => {
  return (
    <Wrapper>
      <List>
        {options.map(({ option, handler }) => (
          <Item key={option}>
            <FeedbackButton onClick={handler} value={option} />
          </Item>
        ))}
      </List>
    </Wrapper>
  );
};

export default Feedback;

Feedback.propTypes = {
  options: PropTypes.arrayOf(
    PropTypes.shape({
      option: PropTypes.string.isRequired,
      handler: PropTypes.func.isRequired,
    })
  ).isRequired,
};
