import PropTypes from 'prop-types';
import { Label, Percentage } from './Statistics.styled';

const StatElement = ({ label, percentage }) => {
  return (
    <>
      <Label>{label}</Label>
      <Percentage>{percentage}%</Percentage>
    </>
  );
};

export default StatElement;

StatElement.propTypes = {
  label: PropTypes.string.isRequired,
  percentage: PropTypes.number.isRequired,
};
