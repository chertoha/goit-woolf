import Player from '@vimeo/player';
import throttle from 'lodash.throttle';

const TIME_STORAGE_KEY = 'videoplayer-current-time';

const player = new Player('vimeo-player', {
  id: 19231868,
  width: 640,
});

const currentTime = localStorage.getItem(TIME_STORAGE_KEY) || 0;
player.setCurrentTime(currentTime).catch(console.log);

player.on('timeupdate', throttle(updateStorage, 1000));

function updateStorage() {
  player
    .getCurrentTime()
    .then(time => {
      localStorage.setItem(TIME_STORAGE_KEY, time);
    })
    .catch(console.log);
}
