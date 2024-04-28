import styled from 'styled-components';

export const Wrapper = styled('div')``;

export const List = styled('ul')`
  display: grid;
  gap: 30px;
  grid-template-columns: repeat(2, 1fr);

  @media screen and (min-width: 768px) {
    grid-template-columns: repeat(5, 1fr);
  }

  @media screen and (min-width: 1440px) {
    grid-template-columns: repeat(8, 1fr);
  }
`;

export const Item = styled('li')``;

export const Image = styled('img')`
  display: block;
  height: 200px;
  width: 100%;
  object-fit: cover;
`;

export const Name = styled('p')`
  margin-top: 10px;
`;

export const Character = styled('p')`
  margin-top: 10px;
`;
