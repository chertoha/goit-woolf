import PropTypes from 'prop-types';
import { Cell } from './TransactionHistory.styled';

const TransactionRow = ({ type, amount, currency }) => {
  return (
    <>
      <Cell>{type}</Cell>
      <Cell>{amount}</Cell>
      <Cell>{currency}</Cell>
    </>
  );
};

export default TransactionRow;

TransactionRow.propTypes = {
  type: PropTypes.string.isRequired,
  amount: PropTypes.string.isRequired,
  currency: PropTypes.string.isRequired,
};
