from flask import Flask, render_template
from random import randint
import os

app = Flask(__name__, static_folder='static')

def get_songs() -> list:
    songs = []

    for path in os.listdir("./static/media/"):
        # check if current path is a file
        if os.path.isfile(os.path.join("./static/media/", path)) and path.endswith('.mp3'):
            songs.append(path.replace('.mp3', ''))

    #sort songs by track number
    songs.sort(key=lambda x: int(x.split('-')[0]))
    print(songs)
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
    print(song)
    return render_template('index.html', TrackNo=song[0], Artist=song[1], Title=song[2], Picture='/media/'+song[2].replace(" ", "_")+".png", File='https://github.com/Sas2k/SongTrack/raw/main/static/media/'+songs[int(song[0])-1].replace("[", "%5B").replace("]", "%5D")+".mp3")

@app.route('/songs/<int:track_no>/')
def track(track_no):
    songs = get_songs()
    song = get_track_song(track_no-1)
    print(song)
    return render_template('index.html', TrackNo=song[0], Artist=song[1], Title=song[2], Picture='/media/'+song[2].replace(" ", "_")+".png", File='https://github.com/Sas2k/SongTrack/raw/main/static/media/'+songs[int(song[0])-1].replace("[", "%5B").replace("]", "%5D")+".mp3")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()