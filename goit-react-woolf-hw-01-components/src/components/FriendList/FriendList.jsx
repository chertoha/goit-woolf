import PropTypes from 'prop-types';
import FriendItem from './FriendItem';
import { Item, List } from './FriendList.styled';

const FriendList = ({ friends }) => {
  return (
    <List>
      {friends.map(({ id, ...props }) => (
        <Item key={id}>
          <FriendItem {...props} />
        </Item>
      ))}
    </List>
  );
};

export default FriendList;

FriendList.propTypes = {
  friends: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.number.isRequired,
      name: PropTypes.string.isRequired,
      avatar: PropTypes.string.isRequired,
      isOnline: PropTypes.bool.isRequired,
    })
  ).isRequired,
};
