import styled from 'styled-components';

export const Wrapper = styled('div')`
  max-width: 800px;
  margin: 0 auto;
`;

export const Table = styled('table')`
  border: 1px solid gray;
  border-collapse: collapse;
  width: 100%;
`;
export const Row = styled('tr')`
  &:nth-child(2n) {
    background-color: aliceblue;
  }

  & > td:nth-child(2) {
    @media screen and (min-width: 768px) {
      padding-right: 90px;
      text-align: right;
    }
  }
`;

export const Head = styled('th')`
  text-transform: uppercase;
  border: 1px solid gray;
  font-size: 12px;
  padding: 10px;
  color: white;
  background-color: lightblue;

  @media screen and (min-width: 768px) {
    font-size: 16px;
  }
`;

export const Cell = styled('td')`
  width: calc(100% / 3);
  padding: 10px;
  /* text-align: center; */
  font-size: 12px;
  border: 1px solid gray;

  @media screen and (min-width: 768px) {
    padding-left: 80px;
    font-size: 16px;
  }
`;
