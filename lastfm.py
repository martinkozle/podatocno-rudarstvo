import os

import pylast
from dotenv import load_dotenv

load_dotenv()


def main():
    api_key = os.getenv('LASTFM_API_KEY')
    api_secret = os.getenv('LASTFM_API_SECRET')
    username = os.getenv('LASTFM_USERNAME')
    password_hash = pylast.md5(os.getenv('LASTFM_PASSWORD'))

    network = pylast.LastFMNetwork(
        api_key=api_key,
        api_secret=api_secret,
        username=username,
        password_hash=password_hash,
    )
    track = network.get_track('Iron Maiden', 'The Nomad')
    print('Play count:', track.get_playcount())
    print('Top tags:', track.get_top_tags())
    print(track.get_wiki_summary())
    for tag in track.get_top_tags():
        print(tag.item, tag.weight)


if __name__ == '__main__':
    main()
