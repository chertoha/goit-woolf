import iziToast from 'izitoast';
import 'izitoast/dist/css/iziToast.min.css';

iziToast.settings({
  timeout: 4000,
  position: 'topRight',
  maxWidth: '400px',
  titleSize: '16px',
  messageSize: '16px',
});

const warning = message => {
  iziToast.warning({
    title: 'Attention!',
    message,
  });
};

const error = message => {
  iziToast.error({
    title: 'Error!',
    message,
  });
};

const success = message => {
  iziToast.success({
    title: 'Success!',
    message,
  });
};

export const toast = {
  emptyList: message => {
    warning(
      message ||
        'Sorry, there are no images matching your search query. Please try again.'
    );
  },

  endCollection: message => {
    warning(
      message || "We're sorry, but you've reached the end of search results."
    );
  },

  fetchError: message => {
    error(message || 'Sorry. Something went wrong while fetching!');
  },

  foundTotal: total => {
    success(`Hooray! We found ${total} images.`);
  },
};
