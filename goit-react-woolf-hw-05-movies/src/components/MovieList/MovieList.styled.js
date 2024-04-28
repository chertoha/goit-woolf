import styled from 'styled-components';
import { Link } from 'react-router-dom';

export const List = styled('ul')`
  padding-left: 30px;
`;

export const Item = styled('li')`
  border-bottom: 1px solid lightgray;
`;

export const MovieLink = styled(Link)`
  display: block;
  padding-top: 10px;
  padding-bottom: 10px;
  font-size: 16px;
  font-weight: 700;
  color: gray;

  transition: color 300ms ease-in-out;

  &:hover {
    color: red;
  }
`;
