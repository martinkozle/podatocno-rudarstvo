import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv


def getSongFeatures(trackID):
    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    data = []
    # FETCHING TRACK NAME AND ARTIST NAME
    try:

        # FETCHING ARTIST DETAILS
        respTrack = sp.track(trackID)

        artistID = respTrack['artists'][0]['id']

        artistFetched = respTrack['artists'][0]['name']
        trackFetched = respTrack['name']

        respArtist = sp.artist(artistID)
        # data.append(respArtist['popularity'])

        # FETCHING AUDIO FEATURES

        respFeature = sp.audio_features(trackID)
        featureFields = list(respFeature[0].keys())

        for key in featureFields:
            if key in {'type', 'track_href', 'uri', 'id', 'analysis_url'}:
                pass
            else:
                data.append(respFeature[0][key])

        # FETCHING AUDIO ANALYSIS

        respAnalysis = sp.audio_analysis(trackID)
        chorusHit = respAnalysis['sections'][2]['start']
        sections = len(respAnalysis['sections'])
        data.append(chorusHit)
        data.append(sections)

    except:
        print("Error in fetching " + trackID)

    return data


load_dotenv()

lz_uri = 'spotify:artist:6ltzsmQQbmdoHHbLZ4ZN25'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
# results = spotify.artist_top_tracks(lz_uri)
artist = spotify.artist(lz_uri)
s = "King Park"
a = "La Dispute"
test = spotify.search(q='artist:' + a + ' track:' + s)['tracks']['items']

for t in test:
    print(spotify.track(t['id'])['name'])
    print(spotify.track(t['id'])['artists'][0]["name"])
    print(t['id'])
    ...
print(test)
# print(spotify.album('2guirTSEqLizK7j9i1MTTZ'))
print(getSongFeatures("2YodwKJnbPyNKe8XXSE9V7"))
print(spotify.track("7uvcuAl1IvSqok1JM6IBjX"))
