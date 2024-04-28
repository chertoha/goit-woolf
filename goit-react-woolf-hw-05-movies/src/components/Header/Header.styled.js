import { NavLink } from 'react-router-dom';
import styled from 'styled-components';

export const StyledHeader = styled('header')``;

export const Wrapper = styled('div')`
  padding: 30px 0;
  border-bottom: 1px solid gray;
`;

export const Nav = styled('nav')``;

export const StyledLink = styled(NavLink)`
  font-size: 20px;
  color: black;
  padding: 8px 10px;

  font-weight: 500;

  transition: color 300ms ease-in-out;

  &.active {
    color: red;
  }

  &:hover {
    color: red;
  }
`;
