import Container from 'components/Container';
import { Nav, StyledHeader, StyledLink, Wrapper } from './Header.styled';

const Header = () => {
  return (
    <StyledHeader>
      <Container>
        <Wrapper>
          <Nav>
            <StyledLink to="/">Home</StyledLink>
            <StyledLink to="/movies">Movies</StyledLink>
          </Nav>
        </Wrapper>
      </Container>
    </StyledHeader>
  );
};

export default Header;
