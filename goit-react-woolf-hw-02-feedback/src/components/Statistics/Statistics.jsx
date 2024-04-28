import PropTypes from 'prop-types';
import Stat from './Stat';
import { Item, List, Percentage, Total, Wrapper } from './Statistics.styled';

const Statistics = ({ total, positivePercentage, options }) => {
  return (
    <Wrapper>
      <List>
        {options.map(({ key, value }) => (
          <Item key={key}>
            <Stat label={key} value={value} />
          </Item>
        ))}
      </List>

      <Total>Total: {total}</Total>
      <Percentage>Positive feedback: {positivePercentage}%</Percentage>
    </Wrapper>
  );
};

export default Statistics;

Statistics.propTypes = {
  good: PropTypes.number.isRequired,
  neutral: PropTypes.number.isRequired,
  bad: PropTypes.number.isRequired,
  total: PropTypes.number.isRequired,
  positivePercentage: PropTypes.string.isRequired,
};
