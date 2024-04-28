import { NavLink } from 'react-router-dom';
import styled from 'styled-components';

export const Wrapper = styled('div')`
  padding-bottom: 30px;
  border-bottom: 1px solid gray;
`;

export const Heading2 = styled('h2')`
  font-size: 16px;
`;

export const List = styled('ul')`
  margin-top: 10px;
  display: flex;
  align-items: center;

  column-gap: 10px;
`;

export const Item = styled('li')``;

export const StyledLink = styled(NavLink)`
  padding: 8px 0;
  color: black;
  text-decoration: underline;
  transition: color 300ms ease-in-out;
  font-size: 16px;

  &.active {
    color: red;
  }

  &:hover {
    color: red;
  }
`;
