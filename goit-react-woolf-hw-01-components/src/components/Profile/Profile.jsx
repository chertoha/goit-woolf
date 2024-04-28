import PropTypes from 'prop-types';
import {
  Avatar,
  AvatarWrapper,
  Description,
  Label,
  Location,
  Name,
  StatItem,
  StatList,
  Tag,
  Value,
  Wrapper,
} from './Profile.styled';

const Profile = ({
  username,
  tag,
  location,
  avatar,
  stats: { followers, views, likes },
}) => {
  return (
    <Wrapper>
      <Description>
        <AvatarWrapper>
          <Avatar src={avatar} alt="User avatar" width={335} />
        </AvatarWrapper>
        <Name>{username}</Name>
        <Tag>@{tag}</Tag>
        <Location>{location}</Location>
      </Description>

      <StatList>
        <StatItem>
          <Label>Followers</Label>
          <Value>{followers}</Value>
        </StatItem>
        <StatItem>
          <Label>Views</Label>
          <Value>{views}</Value>
        </StatItem>
        <StatItem>
          <Label>Likes</Label>
          <Value>{likes}</Value>
        </StatItem>
      </StatList>
    </Wrapper>
  );
};

export default Profile;

Profile.propTypes = {
  username: PropTypes.string.isRequired,
  tag: PropTypes.string.isRequired,
  location: PropTypes.string.isRequired,
  avatar: PropTypes.string.isRequired,
  stats: PropTypes.shape({
    followers: PropTypes.number.isRequired,
    views: PropTypes.number.isRequired,
    likes: PropTypes.number.isRequired,
  }).isRequired,
};
