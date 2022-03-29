import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import pyplot as plt

df = pd.read_parquet("app/dataset/lastfm_processed_final.parquet")


def cargar_datos():
    global df
    print(df.info(verbose=True, null_counts=True))
    print("##################Datos Cargados####################")


def getDataUser(user_id):
    global df
    print(df[df['user_id'] == user_id].loc[0])
    gender = df[df['user_id'] == user_id].gender.loc[0]
    country = df[df['user_id'] == user_id].country.loc[0]
    age = df[df['user_id'] == user_id].age.loc[0]

    if gender == 'M':
        gender = "Hombre"
    elif gender == 'F':
        gender = "Mujer"
    else:
        gender = "No identificado"

    if country == "nan":
        country = "No identificado"

    if age == "nan":
        age = "No identificado"

    dataframe = {"gender": gender, "country": country, "age": age}

    return dataframe

def isUser(user_id):
    try:
        if user_id in df.user_id.values:
            return True
        else:
            return False
    except:
        return False


def getUsurioArtists(user_id):
    global df
    mas_escuchados_artistas_count = df[df['user_id'] == user_id].groupby("artist_name").count()
    mas_escuchados_artistas_count = mas_escuchados_artistas_count.sort_values('user_id', ascending=False)
    mas_escuchados_artistas_count = mas_escuchados_artistas_count.iloc[:5]
    mas_escuchados_artistas_count["valores"] = mas_escuchados_artistas_count.index
    plt.figure(figsize=(16, 10))
    sns.barplot(x="valores", y="user_id", data=mas_escuchados_artistas_count.head(20))
    plt.xticks(rotation=70)
    plt.savefig('static/img/usaurio_artistas.png')


def getUsurioTracks(user_id):
    global df
    mas_escuchados_artistas_count = df[df['user_id'] == user_id].groupby("track_name").count()
    mas_escuchados_artistas_count = mas_escuchados_artistas_count.sort_values('user_id', ascending=False)
    mas_escuchados_artistas_count = mas_escuchados_artistas_count.iloc[:5]
    mas_escuchados_artistas_count["valores"] = mas_escuchados_artistas_count.index
    plt.figure(figsize=(16, 10))
    sns.barplot(x="valores", y="user_id", data=mas_escuchados_artistas_count.head(20))
    plt.xticks(rotation=70)
    plt.savefig('static/img/usaurio_tracks.png')


def bestArtist():
    global df
    # Descripción variable artista
    artist_name = pd.DataFrame(df['artist_name'].value_counts())
    artist_name["index"] = artist_name.index
    artist_name.rename(columns={'index': 'artist_name', 'artist_name': 'valores'}, inplace=True)
    plt.figure(figsize=(16, 10))
    sns.barplot(x="artist_name", y="valores", data=artist_name.head(20))
    plt.xticks(rotation=70)
    plt.savefig('static/img/reproducciones.png')


def getBestTrack():
    global df
    # Descripción variable canción (sin limpieza)
    track_name = pd.DataFrame(df['track_name'].value_counts())
    track_name["index"] = track_name.index
    track_name.rename(columns={'index': 'track_name', 'track_name': 'valores'}, inplace=True)
    plt.figure(figsize=(16, 10))
    sns.barplot(x="track_name", y="valores", data=track_name.head(20))
    plt.xticks(rotation=70)
    plt.savefig('static/img/canciones.png')
