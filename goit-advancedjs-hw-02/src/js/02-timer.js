import flatpickr from 'flatpickr';
import iziToast from 'izitoast';
import 'flatpickr/dist/flatpickr.min.css';
import 'izitoast/dist/css/iziToast.min.css';

const datePickerRef = document.querySelector('input#datetime-picker');
const startButton = document.querySelector('button[data-start]');
const timer = {
  days: document.querySelector('.timer .value[data-days]'),
  hours: document.querySelector('.timer .value[data-hours]'),
  minutes: document.querySelector('.timer .value[data-minutes]'),
  seconds: document.querySelector('.timer .value[data-seconds]'),

  setTime({ days, hours, minutes, seconds }) {
    this.days.innerText = addLeadingZero(days.toString());
    this.hours.innerText = addLeadingZero(hours.toString());
    this.minutes.innerText = addLeadingZero(minutes.toString());
    this.seconds.innerText = addLeadingZero(seconds.toString());
  },
};

iziToast.settings({
  closeOnClick: true,
  position: 'topCenter',
  progressBar: false,
  timeout: false,
  title: 'Error!',
  message: 'Please choose a date in the future',
});

startButton.disabled = true;
let selectedDate = null;

const datePicker = flatpickr(datePickerRef, {
  enableTime: true,
  time_24hr: true,
  defaultDate: new Date(),
  dateFormat: 'd.m.Y H:i',
  minuteIncrement: 1,
  onClose: onClosePickerHandler,
});

startButton.addEventListener('click', onStartButtonClickHandler);

// ----------------------------- Helpers

function onClosePickerHandler(selectedDates) {
  selectedDate = selectedDates[0];
  if (!checkDate(selectedDate)) return;
  startButton.disabled = false;
}

function onStartButtonClickHandler() {
  datePickerRef.disabled = true;

  if (!checkDate(selectedDate)) return;

  startButton.disabled = true;

  const intervalId = setInterval(() => {
    let timeLeft = selectedDate - new Date();
    if (timeLeft <= 0) {
      clearInterval(intervalId);
      timer.setTime(convertMs(0));
      datePickerRef.disabled = false;
      return;
    }

    timer.setTime(convertMs(timeLeft));
  }, 1000);
}

function checkDate(selectedDate) {
  if (selectedDate > new Date()) return true;
  iziToast.error();
  datePicker.defaultDate = new Date();
  return false;
}

function addLeadingZero(value) {
  return value.padStart(2, '0');
}

function convertMs(ms) {
  // Number of milliseconds per unit of time
  const second = 1000;
  const minute = second * 60;
  const hour = minute * 60;
  const day = hour * 24;

  // Remaining days
  const days = Math.floor(ms / day);
  // Remaining hours
  const hours = Math.floor((ms % day) / hour);
  // Remaining minutes
  const minutes = Math.floor(((ms % day) % hour) / minute);
  // Remaining seconds
  const seconds = Math.floor((((ms % day) % hour) % minute) / second);

  return { days, hours, minutes, seconds };
}
