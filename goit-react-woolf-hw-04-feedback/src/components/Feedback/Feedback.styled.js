import styled from 'styled-components';

export const Wrapper = styled('div')`
  margin-top: 20px;
`;

export const List = styled('ul')`
  @media screen and (min-width: 768px) {
    display: flex;
    column-gap: 10px;
  }
`;

export const Item = styled('li')`
  margin-top: 10px;

  @media screen and (min-width: 768px) {
    margin-top: 0;
  }

  &:first-child {
    margin-top: 0;
  }
`;

export const StyledButton = styled('button')`
  width: 100px;
  padding: 12px 20px;
  border: 2px solid rgba(0, 0, 0, 0.8);
  border-radius: 6px;
  font-size: 16px;
  color: #ffffff;
  font-weight: bold;
  background-color: rgba(0, 0, 0, 0.5);
  transition: all 300ms ease-in-out;

  &::first-letter {
    text-transform: uppercase;
  }

  &:hover {
    background-color: #ffffff;
    color: black;
    border: 2px solid rgba(0, 0, 0, 0.8);
  }
`;
