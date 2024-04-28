const rangeSlider = document.querySelector("#font-size-control");
const textField = document.querySelector("#text");

const size = rangeSlider.value;
textField.style.fontSize = `${size}px`;

rangeSlider.addEventListener("input", (e) => {
  const size = e.target.value;
  textField.style.fontSize = `${size}px`;
});
