const inputField = document.querySelector("#name-input");
const outputField = document.querySelector("#name-output");

const DEFAULT_INPUT_VALUE = "Anonymous";

inputField.addEventListener("input", (e) => {
  const value = e.target.value;
  outputField.textContent = value === "" ? DEFAULT_INPUT_VALUE : value;
});
