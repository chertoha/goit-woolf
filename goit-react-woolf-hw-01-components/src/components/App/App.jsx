import Container from 'components/Container';
import Profile from 'components/Profile';
import Section from 'components/Section';
import Statistics from 'components/Statistics';
import FriendList from 'components/FriendList';
import user from 'utils/user.json';
import stats from 'utils/data.json';
import friends from 'utils/friends.json';
import transactions from 'utils/transactions.json';
import TransactionHistory from 'components/TransactionHistory';

const App = () => {
  return (
    <div>
      <Section>
        <Container>
          <Profile
            username={user.username}
            tag={user.tag}
            location={user.location}
            avatar={user.avatar}
            stats={user.stats}
          />
        </Container>
      </Section>

      <Section>
        <Container>
          <Statistics stats={stats} title="Upload stats" />
        </Container>
      </Section>

      <Section>
        <Container>
          <FriendList friends={friends} />
        </Container>
      </Section>

      <Section>
        <Container>
          <TransactionHistory items={transactions} />
        </Container>
      </Section>
    </div>
  );
};

export default App;
