playState = false;
sound = document.getElementById('audio');

function play(){
    if(playState == false){
        playState = true;
        document.getElementById("stopper").classList.remove("fa-play");
        document.getElementById("stopper").classList.add("fa-pause");

        sound.play();
    } else {
        playState = false;
        document.getElementById("stopper").classList.remove("fa-pause");
        document.getElementById("stopper").classList.add("fa-play");

        sound.pause();
    };
};

sound.onended = function() {
    playState = false;
    document.getElementById("stopper").classList.remove("fa-pause");
    document.getElementById("stopper").classList.add("fa-play");
    sound.currentTime = 0;
}