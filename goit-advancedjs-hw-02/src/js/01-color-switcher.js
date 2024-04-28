const INTERVAL_VALUE = 1000;

const startButton = document.querySelector('[data-start]');
const stopButton = document.querySelector('[data-stop]');

stopButton.disabled = true;

const intervalInstance = createInterval(() => {
  document.body.style.backgroundColor = getRandomHexColor();
}, INTERVAL_VALUE);

startButton.addEventListener('click', () => {
  intervalInstance.startInterval();
  toggleButtons();
});
stopButton.addEventListener('click', () => {
  intervalInstance.stopInterval();
  toggleButtons();
});

// ------------------------------------- Helpers
export function createInterval(callback, time) {
  let intervalId = null;

  return {
    startInterval: () => {
      intervalId = setInterval(callback, time);
    },

    stopInterval: () => {
      clearInterval(intervalId);
      intervalId = null;
    },
  };
}

function toggleButtons() {
  startButton.disabled = !startButton.disabled;
  stopButton.disabled = !stopButton.disabled;
}

function getRandomHexColor() {
  return `#${Math.floor(Math.random() * 16777215)
    .toString(16)
    .padStart(6, 0)}`;
}
