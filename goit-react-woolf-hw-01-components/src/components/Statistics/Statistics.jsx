import PropTypes from 'prop-types';
import StatElement from './StatElement';
import { StatItem, StatList, Title, Wrapper } from './Statistics.styled';
import { getRandomHexColor } from 'helpers/randomColor';

const Statistics = ({ title, stats }) => {
  return (
    <Wrapper>
      {title && <Title>Upload stats</Title>}

      <StatList>
        {stats.map(({ id, ...props }) => (
          <StatItem key={id} $bgcolor={getRandomHexColor()}>
            <StatElement {...props} />
          </StatItem>
        ))}
      </StatList>
    </Wrapper>
  );
};

export default Statistics;

Statistics.propTypes = {
  title: PropTypes.string,
  stats: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.string.isRequired,
      label: PropTypes.string.isRequired,
      percentage: PropTypes.number.isRequired,
    })
  ).isRequired,
};
