import PropTypes from 'prop-types';
import { Avatar, Name, Status } from './FriendList.styled';

const FriendItem = ({ name, avatar, isOnline }) => {
  return (
    <>
      <Status $isonline={isOnline}></Status>
      <Avatar src={avatar} alt={name} width="48" />
      <Name> {name}</Name>
    </>
  );
};

export default FriendItem;

FriendItem.propTypes = {
  name: PropTypes.string.isRequired,
  avatar: PropTypes.string.isRequired,
  isOnline: PropTypes.bool.isRequired,
};
