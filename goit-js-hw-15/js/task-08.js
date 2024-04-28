const loginForm = document.querySelector(".login-form");

loginForm.addEventListener("submit", (e) => {
  e.preventDefault();

  const { email, password } = e.target.elements;

  if (email.value === "" || password.value === "") {
    alert("All fields have to be filled!");
    return;
  }

  const result = { email: email.value, password: password.value };
  console.log(result);

  e.target.reset();
});
