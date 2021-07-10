def tracklist(**listing):
    for artist, albums in listing.items():
        print(artist)
        for album, track in albums.items():
            print(f"ALBUM: {album} TRACK: {track}")
