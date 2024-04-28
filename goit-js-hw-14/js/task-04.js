const valueField = document.querySelector("#value");
const decrementBtn = document.querySelector(
  "#counter button[data-action=decrement]"
);
const incrementBtn = document.querySelector(
  "#counter button[data-action=increment]"
);

let counterValue = 0;

decrementBtn.addEventListener("click", () => {
  counterValue -= 1;
  valueFieldRefresh();
});

incrementBtn.addEventListener("click", () => {
  counterValue += 1;
  valueFieldRefresh();
});

function valueFieldRefresh() {
  valueField.textContent = counterValue;
}
