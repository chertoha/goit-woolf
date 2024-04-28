import PropTypes from 'prop-types';
import FeedbackButton from './FeedbackButton';
import { List, Item, Wrapper } from './Feedback.styled';

const Feedback = ({ options, buttonHandler }) => {
  return (
    <Wrapper>
      <List>
        {options.map(option => (
          <Item key={option}>
            <FeedbackButton
              onClick={() => {
                buttonHandler(option);
              }}
              value={option}
            />
          </Item>
        ))}
      </List>
    </Wrapper>
  );
};

export default Feedback;

Feedback.propTypes = {
  options: PropTypes.arrayOf(PropTypes.string).isRequired,
  buttonHandler: PropTypes.func.isRequired,
};
