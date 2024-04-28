import styled from 'styled-components';

export const Form = styled('form')`
  display: flex;
`;

export const SearchField = styled('input')`
  font-size: 20px;
  padding: 8px 20px;
  border: 1px solid gray;
  outline: none;
`;

export const SubmitButton = styled('button')`
  padding: 0 12px;
  display: block;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid gray;
  border-left: none;

  &:hover {
    background-color: rgba(0, 0, 0, 0.03);
  }
`;
