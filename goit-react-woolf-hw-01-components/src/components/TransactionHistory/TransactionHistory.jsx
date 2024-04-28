import PropTypes from 'prop-types';
import { Head, Row, Table, Wrapper } from './TransactionHistory.styled';
import TransactionRow from './TransactionRow';

const TransactionHistory = ({ items }) => {
  return (
    <Wrapper>
      <Table>
        <thead>
          <Row>
            <Head>Type</Head>
            <Head>Amount</Head>
            <Head>Currency</Head>
          </Row>
        </thead>

        <tbody>
          {items.map(({ id, ...props }) => (
            <Row key={id}>
              <TransactionRow {...props} />
            </Row>
          ))}
        </tbody>
      </Table>
    </Wrapper>
  );
};

export default TransactionHistory;

TransactionHistory.propTypes = {
  items: PropTypes.arrayOf(
    PropTypes.shape({
      type: PropTypes.string.isRequired,
      amount: PropTypes.string.isRequired,
      currency: PropTypes.string.isRequired,
    })
  ).isRequired,
};
