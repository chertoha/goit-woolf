import axios from 'axios';

const API_KEY = '40477492-fb7a942987769cd06fc4fed72';
const BASE_URL = 'https://pixabay.com/api/';

export const PER_PAGE = 40;

export const api = axios.create({
  baseURL: BASE_URL,
  params: {
    key: API_KEY,
    image_type: 'photo',
    orientation: 'horizontal',
    safesearch: true,
  },
});
