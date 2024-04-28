import PropTypes from 'prop-types';
import { StyledSection } from './Section.styled';

const Section = ({ children }) => {
  return <StyledSection>{children}</StyledSection>;
};

export default Section;

Section.propTypes = {
  children: PropTypes.node.isRequired,
};
