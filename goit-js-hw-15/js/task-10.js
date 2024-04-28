function getRandomHexColor() {
  return `#${Math.floor(Math.random() * 16777215)
    .toString(16)
    .padStart(6, 0)}`;
}

const amountField = document.querySelector("#controls > input[type=number]");
const createBtn = document.querySelector("#controls > button[data-create]");
const destroyBtn = document.querySelector("#controls > button[data-destroy]");
const boxContainer = document.querySelector("#boxes");

const FIRST_BOX_SIZE = 30;
const SIZE_STEP = 10;

const createBoxes = (amount) => {
  amount = Number(amount);

  if (Number.isNaN(amount)) {
    console.error("Amount must be a number!");
    return;
  }

  const { min, max } = amountField;
  if (amount < min || amount > max) {
    console.error(`Amount must be between ${min} and ${max}`);
    return;
  }

  const boxes = [...Array(amount)].map((val, i) => {
    const box = document.createElement("div");
    const size = i * SIZE_STEP + FIRST_BOX_SIZE;
    box.style.width = `${size}px`;
    box.style.height = `${size}px`;
    box.style.backgroundColor = getRandomHexColor();
    return box;
  });

  boxContainer.append(...boxes);
};

const destroyBoxes = () => {
  boxContainer.innerHTML = "";
};

createBtn.addEventListener("click", () => {
  const amount = amountField.value;
  createBoxes(amount);
});

destroyBtn.addEventListener("click", destroyBoxes);
