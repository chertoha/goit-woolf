import woodsImage from "../assets/woods.jpg";
import notWoodsImage from "../assets/not-woods.jpg";
import totallyNotWoodsImage from "../assets/totally-not-woods.jpg";

export const posts = [
  {
    id: 1,
    img: woodsImage,
    title: "Ліс",
    comments: 0,
    location: "Ivano-Frankivs'k Region, Ukraine",
    likes: 153,
  },
  {
    id: 2,
    img: notWoodsImage,
    title: "Не Ліс",
    comments: 0,
    location: "Ivano-Frankivs'k Region, Ukraine",
    likes: 200,
  },
  {
    id: 3,
    img: totallyNotWoodsImage,
    title: "Зовсім не Ліс",
    comments: 0,
    location: "Ivano-Frankivs'k Region, Ukraine",
    likes: 200,
  },
];
