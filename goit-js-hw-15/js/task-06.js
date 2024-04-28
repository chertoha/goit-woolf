const field = document.querySelector("#validation-input");

field.addEventListener("blur", onFieldBlurHandler);

function onFieldBlurHandler(e) {
  const validLength = Number(this.dataset.length);
  const value = e.target.value;

  if (value.length !== validLength) {
    this.classList.remove("valid");
    this.classList.add("invalid");
  } else {
    this.classList.remove("invalid");
    this.classList.add("valid");
  }
}
