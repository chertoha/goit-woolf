import styled from 'styled-components';

export const Wrapper = styled('div')`
  padding-top: 20px;

  max-width: 400px;
  margin: 0 auto;

  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 8px;

  box-shadow: 4px 4px 6px 0px rgba(0, 0, 0, 0.1);
`;

export const Description = styled('div')`
  text-align: center;
  padding: 0 10px;
`;

export const AvatarWrapper = styled('div')`
  margin: 0 auto;
  max-width: 300px;
  max-height: 300px;
  padding: 50px;
  border-radius: 50%;
  overflow: hidden;
  background-color: rgba(0, 0, 0, 0.05);
`;

export const Avatar = styled('img')`
  display: block;
  margin: 0 auto;
  max-width: 100%;
`;

export const Name = styled('p')`
  margin-top: 20px;
  font-size: 28px;
  font-weight: 700;
`;

export const Tag = styled('p')`
  margin-top: 10px;
  font-size: 20px;
  color: gray;
`;

export const Location = styled(Tag)`
  margin-top: 10px;
`;

export const StatList = styled('ul')`
  margin-top: 40px;
  display: flex;

  border-top: 1px solid rgba(0, 0, 0, 0.2);
  background-color: rgba(0, 0, 0, 0.05);

  @media screen and (max-width: 375px) {
    flex-direction: column;
  }
`;

export const StatItem = styled('li')`
  border-right: 1px solid rgba(0, 0, 0, 0.1);
  flex-basis: calc(100% / 3);
  padding: 20px;

  display: flex;
  flex-direction: column;
  align-items: center;

  row-gap: 10px;

  @media screen and (max-width: 375px) {
    border-bottom: 1px solid rgba(0, 0, 0, 0.1);
  }

  &:last-child {
    border-right: none;
    border-bottom: none;
  }
`;

export const Label = styled('span')`
  font-size: 20px;
  font-weight: 700;
`;

export const Value = styled('span')`
  font-size: 20px;
`;
