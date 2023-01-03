let audio = document.getElementById('audio');
let progress = document.getElementById('progress');
let stopper = document.getElementById('stopper');
let current = document.getElementById('current');
let duration = document.getElementById('duration');

function play() {
    if (audio.paused) {
        audio.play();
        stopper.classList.remove('fa-play');
        stopper.classList.add('fa-pause');
    } else {
        audio.pause();
        stopper.classList.remove('fa-pause');
        stopper.classList.add('fa-play');
    }
}

function updateProgress(Return) {
    progress.value = (audio.currentTime / audio.duration) * 100;
    let min = Math.floor(audio.currentTime / 60);
    let sec = Math.floor(audio.currentTime % 60);
    if (sec < 10) {
        sec = `0${sec}`;
    }
    current.innerHTML = `${min}:${sec}`;
    let durationMin = Math.floor(audio.duration / 60);
    let durationSec = Math.floor(audio.duration % 60);
    if (durationSec < 10) {
        durationSec = `0${durationSec}`;
    }
    duration.innerHTML = `${durationMin}:${durationSec}`;
    if (Return) {
        return progress.value;
    }
}

progress.addEventListener('click', function (e) {
    let width = this.clientWidth;
    let clickX = e.offsetX;
    let duration = audio.duration;
    audio.currentTime = (clickX / width) * duration;
});

audio.addEventListener('timeupdate', updateProgress);

audio.addEventListener('ended', function () {
    stopper.classList.remove('fa-pause');
    stopper.classList.add('fa-play');
    progress.value = 0;
    document.getElementById('current').innerHTML = '0:00';
});