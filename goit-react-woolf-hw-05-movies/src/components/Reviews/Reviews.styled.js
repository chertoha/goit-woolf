import styled from 'styled-components';

export const Wrapper = styled('div')``;

export const List = styled('ul')``;

export const Item = styled('li')`
  margin-bottom: 30px;

  &:last-child {
    margin-bottom: 0;
  }
`;

export const Author = styled('h4')`
  font-size: 16px;
  margin-bottom: 5px;
`;

export const Review = styled('p')`
  line-height: 1.5;
`;
