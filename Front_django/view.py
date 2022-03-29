from app.main import bestArtist, getBestTrack, getUsurioArtists, getUsurioTracks, isUser, getDataUser, getPredicciones
from django.shortcuts import render


userIDGlobal: str = ""

def getBestArtistView(request):
    bestArtist()
    return render(request, '../templates/bestArtist.html')


def getBestTrackView(request):
    getBestTrack()
    return render(request, '../templates/bestArtist.html')


def loginView(request):
    return render(request, '../templates/login.html')


def recomendacionesView(request):
    global userIDGlobal
    getUsurioArtists(userIDGlobal)
    getUsurioTracks(userIDGlobal)
    predicciones = getPredicciones(userIDGlobal)
    return render(request, '../templates/recomendaciones.html', {"predicciones" : predicciones})


def popularesView(request):
    bestArtist()
    getBestTrack()
    return render(request, '../templates/populares.html')


def accesoView(request):
    global userIDGlobal
    userIDGlobal = request.GET["user_id"]
    passwordIDGlobal = request.GET["password"]
    print(userIDGlobal)
    print(passwordIDGlobal)
    if isUser(userIDGlobal) and userIDGlobal == passwordIDGlobal:
        return render(request, '../templates/recomendaciones.html')
    else:
        return render(request, '../templates/login.html')


def registroView(request):
    return render(request, '../templates/registro.html')

def perfilView(request):
    global userIDGlobal
    getDataTemp = getDataUser(userIDGlobal)
    return render(request, '../templates/perfil.html', getDataTemp)