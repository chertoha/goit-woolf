import styled from 'styled-components';

export const List = styled('ul')`
  max-width: 400px;
  margin: 0 auto;
`;

export const Item = styled('li')`
  margin-bottom: 15px;
  padding: 20px;
  display: flex;
  align-items: center;
  column-gap: 20px;

  border: 1px solid rgba(0, 0, 0, 0.1);
  box-shadow: 4px 4px 6px 0px rgba(0, 0, 0, 0.1);

  &:last-child {
    margin-bottom: 0;
  }
`;

export const Status = styled('span')`
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background-color: ${p => (p.$isonline ? 'green' : 'red')};
`;

export const Name = styled('p')`
  font-size: 20px;
  font-weight: 500;
`;

export const Avatar = styled('img')``;
