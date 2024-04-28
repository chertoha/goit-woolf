import styled from 'styled-components';

export const Wrapper = styled('div')`
  border-bottom: 1px solid gray;
  padding-bottom: 40px;

  @media screen and (min-width: 768px) {
    display: flex;
    column-gap: 30px;
  }
`;

export const StyledImage = styled('img')`
  flex-shrink: 0;
  display: block;

  height: auto;
  width: 100%;

  @media screen and (min-width: 768px) {
    width: 30%;
  }
`;

export const Meta = styled('div')`
  flex-grow: 1;
`;

export const Heading1 = styled('h1')`
  font-size: 30px;
  margin-bottom: 20px;

  @media screen and (max-width: 767.98px) {
    margin-top: 20px;
  }
`;

export const Heading2 = styled('h2')`
  font-size: 20px;
  margin-bottom: 10px;
  margin-top: 20px;
`;

export const Overview = styled('p')``;

export const Genres = styled('p')``;
