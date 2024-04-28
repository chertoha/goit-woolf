import { Link } from 'react-router-dom';
import styled from 'styled-components';

export const StyledLink = styled(Link)`
  padding-top: 20px;
  display: inline-flex;
  align-items: center;
  column-gap: 10px;

  color: black;
  transition: color 300ms ease-in-out;

  &:hover {
    color: red;
  }
`;
