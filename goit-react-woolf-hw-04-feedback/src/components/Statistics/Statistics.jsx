import PropTypes from 'prop-types';
import Stat from './Stat';
import { Item, List, Percentage, Total, Wrapper } from './Statistics.styled';

const Statistics = ({ total, positivePercentage, options }) => {
  return (
    <Wrapper>
      <List>
        {options.map(({ option, value }) => (
          <Item key={option}>
            <Stat label={option} value={value} />
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
  options: PropTypes.arrayOf(
    PropTypes.shape({
      option: PropTypes.string.isRequired,
      value: PropTypes.number.isRequired,
    })
  ).isRequired,
  total: PropTypes.number.isRequired,
  positivePercentage: PropTypes.string.isRequired,
};
