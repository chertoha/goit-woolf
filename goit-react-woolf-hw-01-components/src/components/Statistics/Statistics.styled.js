import styled from 'styled-components';

export const Wrapper = styled('div')`
  max-width: 400px;
  margin: 0 auto;

  background-color: lightgray;
`;

export const Title = styled('h2')`
  padding: 40px;
  font-size: 24px;
  text-transform: uppercase;
  text-align: center;
  color: gray;
`;

export const StatList = styled('ul')`
  display: flex;
  flex-wrap: wrap;
`;

export const StatItem = styled('li')`
  padding: 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
  row-gap: 8px;

  flex-basis: calc(100% / 5);

  color: white;
  background-color: ${p => p.$bgcolor};
`;

export const Label = styled('span')`
  font-size: 20px;
`;

export const Percentage = styled('span')``;
