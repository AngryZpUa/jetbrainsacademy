def tracklist(**tracks):
    for key, value in tracks.items():
        print(key)
        for item in value.items():
            print('ALBUM: {} TRACK: {}'.format(item[0], item[1]))
