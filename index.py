from flask import Flask, render_template
from random import randint
import os

app = Flask(__name__, static_folder='public', static_url_path='')

songs = []

for path in os.listdir("./public/static/css/music/"):
    # check if current path is a file
    if os.path.isfile(os.path.join("./public/static/css/music/", path)):
        songs.append(path.replace('.mp3', ''))

def get_random_song_info():
    song = str(songs[randint(0, len(songs) - 1)]).replace('.mp3', '').split(' - ')
    return song

def get_track_song(track_no):
    try:
        song = str(songs[track_no]).replace('.mp3', '').split(' - ')
        return song
    except:
        song = str(songs[-1]).replace('.mp3', '').split(' - ')
        return song


@app.route('/')
def index():
    song = get_random_song_info()
    return render_template('index.html', TrackNo=song[0], Artist=song[1], Title=song[2], Picture='static/css/images/'+song[2]+".png", File='static/css/music/'+songs[int(song[0])-1]+".mp3")

@app.route('/songs/<int:track_no>/')
def track(track_no):
    song = get_track_song(track_no-1)
    return render_template('index.html', TrackNo=song[0], Artist=song[1], Title=song[2], Picture='static/css/images/'+song[2]+".png", File='static/css/music/'+songs[int(song[0])-1]+".mp3")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(port='8005', host='0.0.0.0')