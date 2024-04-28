import Container from 'components/Container';
import Feedback from 'components/Feedback';
import Notification from 'components/Notification';
import Section from 'components/Section';
import Statistics from 'components/Statistics';
import { Component } from 'react';

const FEEDBACK_VALUE = {
  GOOD: 'good',
  NEUTRAL: 'neutral',
  BAD: 'bad',
};

class App extends Component {
  state = {
    [FEEDBACK_VALUE.GOOD]: 0,
    [FEEDBACK_VALUE.NEUTRAL]: 0,
    [FEEDBACK_VALUE.BAD]: 0,
  };

  increase = name => {
    this.setState(state => ({ ...state, [name]: state[name] + 1 }));
  };

  countTotalFeedback = (...args) => {
    return args.reduce((acc, arg) => acc + arg, 0);
  };

  countPositiveFeedbackPercentage = (positiveValue, total) => {
    return ((positiveValue / total) * 100).toFixed(0);
  };

  render() {
    const total = this.countTotalFeedback(...Object.values(this.state));
    const positivePercentage = this.countPositiveFeedbackPercentage(
      this.state[FEEDBACK_VALUE.GOOD],
      total
    );
    const feedbackOptions = Object.keys(this.state);

    const statisticsOptions = Object.keys(this.state).map(key => ({
      key,
      value: this.state[key],
    }));

    return (
      <div>
        <h1 hidden>User's feedback application</h1>

        <Container>
          <Section title="Please leave feedback">
            <Feedback buttonHandler={this.increase} options={feedbackOptions} />
          </Section>
        </Container>

        <Container>
          <Section title="Statistics">
            {total > 0 ? (
              <Statistics
                total={total}
                positivePercentage={positivePercentage}
                options={statisticsOptions}
              />
            ) : (
              <Notification message="There is no feedback yet!" />
            )}
          </Section>
        </Container>
      </div>
    );
  }
}

export default App;
