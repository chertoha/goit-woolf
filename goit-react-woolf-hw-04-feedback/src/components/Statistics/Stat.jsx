import PropTypes from 'prop-types';
import { Label, StyledStat } from './Statistics.styled';

const Stat = ({ label, value }) => {
  return (
    <StyledStat>
      <Label>{label}</Label>: {value}
    </StyledStat>
  );
};
export default Stat;

Stat.propTypes = {
  label: PropTypes.string.isRequired,
  value: PropTypes.number.isRequired,
};
