import lyricsgenius

genius = lyricsgenius.Genius('KhbzXSfMiwjd81r_gG1-27YTaPPKFJmP_yZzNjIwBHKBGgbbc2zJEBbfI2mJ8xsw')

#stores the lyrics provided by the API into folder songs/artist_name/album_name_index_ 
def download_lyrics(songs, artist_name, album_name):
    for i in range(len(songs)):
        song = genius.search_song(songs[i], artist_name)
        lyrics = song.lyrics
        with open('songs/{}/{}_{}_{}.txt'.format('_'.join(artist_name.split(' ')), i+1, album_name, '-'.join(''.join(songs[i].split('\'')).split(' '))), 'w', encoding='utf-8') as f:
            f.writelines(lyrics.split('\\n'))


if __name__=='__main__':
    songs = ['Stan', 'Not Afraid', 'Lose Yourself', 'The Real Slim Shady', 
                'White America', 'My Name Is', 'Without Me', 'Till I Collapse',
                'Love The Way You Lie', 'Godzilla', 'Rap God', 'Mockingbird', 
                'The Monster', 'Brain Damage', 'No Love', 'Cinderella Man', 
                'Like Toy Soldiers', 'Berzerk', 'Just Lose It', 'We Made You']
    download_lyrics(songs, 'Eminem', '')