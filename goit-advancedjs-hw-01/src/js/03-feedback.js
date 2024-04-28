import throttle from 'lodash.throttle';
const FORM_STORAGE_KEY = 'feedback-form-state';

const form = document.querySelector('.feedback-form');
const fields = form.querySelectorAll('[name]');

let state = getPersistedState();
fillFields();

form.addEventListener('input', throttle(onInput, 500));
form.addEventListener('submit', onSubmit);

// --------------------- Helpers
function onInput(e) {
  const { name, value } = e.target;
  state = { ...state, [name]: value };
  persistState(state);
}

function onSubmit(e) {
  e.preventDefault();
  console.log(state);
  clearPersistedState();
  form.reset();
}

function getPersistedState() {
  const state = localStorage.getItem(FORM_STORAGE_KEY);
  return state ? JSON.parse(state) : {};
}

function persistState(state) {
  localStorage.setItem(FORM_STORAGE_KEY, JSON.stringify(state));
}

function clearPersistedState() {
  localStorage.removeItem(FORM_STORAGE_KEY);
  state = {};
}

function fillFields() {
  fields.forEach(field => {
    field.value = state[field.name] || '';
  });
}
