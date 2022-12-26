from flask import Flask, render_template
from random import randint
import os

app = Flask(__name__, static_folder='static')

def get_songs() -> list:
    songs = []

    for path in os.listdir("./static/music/"):
        # check if current path is a file
        if os.path.isfile(os.path.join("./static/music/", path)):
            songs.append(path.replace('.mp3', ''))

    #sort songs by track number
    songs.sort(key=lambda x: int(x.split('-')[0]))
    return songs

def get_random_song_info() -> list:
    songs = get_songs()
    song = str(songs[randint(0, len(songs) - 1)]).replace("_", " ").split('-')
    return song

def get_track_song(track_no) -> list:
    songs = get_songs()
    try:
        song = str(songs[track_no]).replace("_", " ").split('-')
        return song
    except:
        song = str(songs[0]).replace("_", " ").split('-')
        return song


@app.route('/')
def index():
    songs = get_songs()
    song = get_random_song_info()
    return render_template('index.html', TrackNo=song[0], Artist=song[1], Title=song[2], Picture='/images/'+song[2].replace(" ", "_")+".png", File='/music/'+songs[int(song[0])-1]+".mp3")

@app.route('/songs/<int:track_no>/')
def track(track_no):
    songs = get_songs()
    song = get_track_song(track_no-1)
    return render_template('index.html', TrackNo=song[0], Artist=song[1], Title=song[2], Picture='/images/'+song[2].replace(" ", "_")+".png", File='/music/'+songs[int(song[0])-1]+".mp3")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()