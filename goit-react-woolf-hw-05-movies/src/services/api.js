import axios from 'axios';
import { ACCESS_TOKEN, BASE_URL } from 'utils/config';

const api = axios.create({
  baseURL: BASE_URL,
  headers: {
    Authorization: `Bearer ${ACCESS_TOKEN}`,
  },
  params: {
    language: 'en-US',
  },
});

export const getTrendings = async () => {
  const response = await api.get('/trending/movie/day');
  return response.data;
};

export const findMovie = async query => {
  const response = await api.get('/search/movie', {
    params: { include_adult: false, query, page: 1 },
  });
  return response.data;
};

export const getMovieById = async movieId => {
  const response = await api.get(`/movie/${movieId}`);
  return response.data;
};

export const getCast = async movieId => {
  const response = await api.get(`/movie/${movieId}/credits`);
  return response.data;
};

export const getReviews = async movieId => {
  const response = await api.get(`/movie/${movieId}/reviews`);
  return response.data;
};
