const categoryList = document.querySelector("#categories");
const categoryItems = categoryList.children;
console.log(`Number of categories: ${categoryItems.length}\n\n`);

[...categoryItems].forEach((item) => {
  const title = item.firstElementChild;
  const elements = title.nextElementSibling.children;

  console.log(`Category: ${title.textContent}`);
  console.log(`Elements: ${elements.length}\n\n`);
});
