import PropTypes from 'prop-types';
import { Form, SearchField, SubmitButton } from './SearchForm.styled';
import { IoIosSearch } from 'react-icons/io';

const SearchForm = ({ onSubmit }) => {
  const onSubmitHandler = e => {
    e.preventDefault();
    onSubmit(e.target.elements.searchMovie.value);
  };

  return (
    <Form autoComplete="off" onSubmit={onSubmitHandler}>
      <SearchField type="text" name="searchMovie" />
      <SubmitButton type="submit">
        <IoIosSearch size={16} />
      </SubmitButton>
    </Form>
  );
};

export default SearchForm;

SearchForm.propTypes = {
  onSubmit: PropTypes.func.isRequired,
};
