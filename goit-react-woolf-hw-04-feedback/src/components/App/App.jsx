import Container from 'components/Container';
import Feedback from 'components/Feedback';
import Notification from 'components/Notification';
import Section from 'components/Section';
import Statistics from 'components/Statistics';
import { useState } from 'react';

const App = () => {
  const [good, setGood] = useState(0);
  const [neutral, setNeutral] = useState(0);
  const [bad, setBad] = useState(0);

  const increase = set => {
    set(prevState => prevState + 1);
  };

  const countTotalFeedback = (...args) => {
    return args.reduce((acc, arg) => acc + arg, 0);
  };

  const countPositiveFeedbackPercentage = (positiveValue, total) => {
    return ((positiveValue / total) * 100).toFixed(0);
  };

  const total = countTotalFeedback(good, neutral, bad);
  const positivePercentage = countPositiveFeedbackPercentage(good, total);

  const options = [
    { option: 'Good', value: good, handler: () => increase(setGood) },
    { option: 'Neutral', value: neutral, handler: () => increase(setNeutral) },
    { option: 'Bad', value: bad, handler: () => increase(setBad) },
  ];

  return (
    <div>
      <h1 hidden>User's feedback application</h1>

      <Container>
        <Section title="Please leave feedback">
          <Feedback options={options} />
        </Section>
      </Container>

      <Container>
        <Section title="Statistics">
          {total > 0 ? (
            <Statistics
              total={total}
              positivePercentage={positivePercentage}
              options={options}
            />
          ) : (
            <Notification message="There is no feedback yet!" />
          )}
        </Section>
      </Container>
    </div>
  );
};

export default App;
