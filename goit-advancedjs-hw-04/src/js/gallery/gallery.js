import SimpleLightbox from 'simplelightbox';
import 'simplelightbox/dist/simple-lightbox.min.css';
import { PER_PAGE } from '../config';
import { createGallery } from './createGallery';
import { createGAlleryMarkup } from './gallery-markup';

const form = document.querySelector('.search');
const gallery = document.querySelector('.gallery');
const loadMoreBtn = document.querySelector('.load-more');
const loaderRef = document.querySelector('.loader');

const lightbox = new SimpleLightbox('.gallery a', {
  showCounter: false,
});

const galleryInstance = createGallery(render, {
  limit: PER_PAGE,
  loader: createHideable(loaderRef),
  smoothScroll,
  loadMore: createHideable(loadMoreBtn),
});

form.addEventListener('submit', e => {
  e.preventDefault();
  const query = e.target.elements.searchQuery.value.trim();

  galleryInstance.setQuery(query);
});

loadMoreBtn.addEventListener('click', () => {
  galleryInstance.increasePage();
});

//-------------------------------------------------Helpers

function render(data) {
  const markup = createGAlleryMarkup(data);
  gallery.innerHTML = '';
  gallery.insertAdjacentHTML('beforeend', markup);
  lightbox.refresh();
}

function smoothScroll() {
  const { height: cardHeight } = document
    .querySelector('.gallery')
    .firstElementChild.getBoundingClientRect();

  window.scrollBy({
    top: cardHeight * 2.3,
    behavior: 'smooth',
  });
}

function createHideable(instance) {
  return {
    show() {
      instance.classList.add('visible');
    },
    hide() {
      instance.classList.remove('visible');
    },
  };
}
