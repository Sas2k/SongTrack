from flask import Flask, render_template, url_for
from random import randint

app = Flask(__name__, static_folder='static')

def get_songs() -> list:
    
    songs = [
        "1-Omori_[Pedro_Silva]-172._Duet",
        "2-Omori_[Jami_Lynne]-177._Good_Morning",
        "3-Super_Mario_Galaxy_[Koji_Kondo]-Gusty_Garden_Galaxy",
        "4-The_Legend_of_Zelda_[Koji_Kondo]-Main_Theme_Medley_(25th_Anniversary)",
        "5-Spirited_Away_[Joe_Hisaishi]-One_Summer's_Day",
        "6-Super_Mario_Odyssey_[Koji_Kondo]-Steam_Gardens",
        "7-Super_Smash_Bros._Ultimate[Hideki_Sakamoto]-Lifelight",
        "8-Megalovania_[Toby_Fox]-100._Megalovania",
        "9-Super_Mario_Kart_[Soyo_Oka]-Rainbow_Road_(1992)",
        "10-Mario_Kart_Wii_[Asuka_Ota]-Coconut_Mall",
        "11-Mario_Kart_Wii_[Asuka_Ota_And_Ryo_Nagamatsu]-Rainbow_Road_(2008)",
        "12-Pokemon_Red_And_Blue_[Junichi_Masuda]-Title_Screen_Theme",
        "13-Pokemon_Sword_And_Shield_[Go_Ichinose]-Title_Intro_Theme",
        "14-The_Legend_of_Zelda_Ocarina_of_Time[Koji_Kondo]-Gerudo_Valley",
        "15-The_Legend_of_Zelda_Breath_of_the_Wild_[Manaka_Kataoka,_Yasuaki_Iwata_and_Hajime_Wakai]-Main_Theme",
        "16-Super_Mario_3D_World_[Koji_Kondo]-Title_Theme",
        "17-Kirby_and_The_forgotten_Land_[Yuta_Ogasawara_and_Hirokazu_Ando]-Title_Screen_Theme",
        "18-Howl's_Moving_Castle_[Joe_Hisaishi]-Merry-Go-Round_of_Life",
    ]

    songs.sort(key=lambda x: int(x.split('-')[0]))
    return songs

def get_random_song_info() -> list:
    songs = get_songs()
    song = str(songs[randint(0, len(songs) - 1)]).replace("_", " ").split('-', 2)
    return song

def get_track_song(track_no) -> list:
    songs = get_songs()
    try:
        song = str(songs[track_no]).replace("_", " ").split('-', 2)
        return song
    except:
        song = str(songs[0]).replace("_", " ").split('-', 2)
        return song


@app.route('/')
def index():
    songs = get_songs()
    song = get_random_song_info()
    # print(song)
    return render_template('index.html', TrackNo=song[0], Artist=song[1], Title=song[2], Tracks=len(songs), File='https://raw.githubusercontent.com/Sas2k/SongTrack/main/static/media/'+songs[int(song[0])-1].replace("(", "%28").replace(")", "%29").replace("[", "%5B").replace("]", "%5D")+".mp3", Picture='https://raw.githubusercontent.com/Sas2k/SongTrack/main/static/media/'+str(song[0])+'-'+song[2].replace(" ", "_").replace("(", "%28").replace(")", "%29").replace("[", "%5B").replace("]", "%5D")+".png")

#For Production
#File='https://raw.githubusercontent.com/Sas2k/SongTrack/main/static/media/'+songs[int(song[0])-1].replace("(", "%28").replace(")", "%29").replace("[", "%5B").replace("]", "%5D")+".mp3", Picture='https://raw.githubusercontent.com/Sas2k/SongTrack/main/static/media/'+str(song[0])+'-'+song[2].replace(" ", "_").replace("(", "%28").replace(")", "%29").replace("[", "%5B").replace("]", "%5D")+".png"

#For Local Testing
#File=url_for('static', filename='/media/'+songs[int(song[0])-1]+".mp3"), Picture=url_for('static' , filename='/media/'+str(song[0])+'-'+song[2].replace(" ", "_")+".png")

@app.route('/songs/<int:track_no>/')
def track(track_no):
    songs = get_songs()
    song = get_track_song(track_no-1)
    # print(song)
    return render_template('song.html', TrackNo=song[0], Artist=song[1], Title=song[2], Tracks=len(songs), File='https://raw.githubusercontent.com/Sas2k/SongTrack/main/static/media/'+songs[int(song[0])-1].replace("(", "%28").replace(")", "%29").replace("[", "%5B").replace("]", "%5D")+".mp3", Picture='https://raw.githubusercontent.com/Sas2k/SongTrack/main/static/media/'+str(song[0])+'-'+song[2].replace(" ", "_").replace("(", "%28").replace(")", "%29").replace("[", "%5B").replace("]", "%5D")+".png")

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/list/')
def list():
    raw_songs = get_songs()
    songs = []
    for song in raw_songs:
        song = song.split('-', 2)
        songs.append(song)

    songs.sort(key=lambda x: int(x[0]))
    return render_template('list.html', Songs=songs)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()