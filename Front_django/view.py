from django.shortcuts import render

from app.main import bestArtist, getBestTrack, getUsurioArtists, getUsurioTracks, isUser, getDataUser, getPredicciones

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
    print(predicciones)
    return render(request, '../templates/recomendaciones.html',
                      {"predicciones1": predicciones[0][0], "predicciones2": predicciones[1][0],
                       "predicciones3": predicciones[2][0],
                       "predicciones4": predicciones[3][0], "predicciones5": predicciones[4][0],
                       "predicciones1_value": predicciones[0][1], "predicciones2_value": predicciones[1][1],
                       "predicciones3_value": predicciones[2][1],
                       "predicciones4_value": predicciones[3][1],
                       "predicciones5_value": predicciones[4][1]})


def popularesView(request):
    bestArtist()
    getBestTrack()
    return render(request, '../templates/populares.html')


def accesoView(request):
    global userIDGlobal
    userIDGlobal = request.GET["user_id"]
    passwordIDGlobal = request.GET["password"]
    if isUser(userIDGlobal) and userIDGlobal == passwordIDGlobal:
        getUsurioArtists(userIDGlobal)
        getUsurioTracks(userIDGlobal)
        predicciones = getPredicciones(userIDGlobal)

        return render(request, '../templates/recomendaciones.html',
                      {"predicciones1": predicciones[0][0], "predicciones2": predicciones[1][0],
                       "predicciones3": predicciones[2][0],
                       "predicciones4": predicciones[3][0], "predicciones5": predicciones[4][0],
                       "predicciones1_value": predicciones[0][1], "predicciones2_value": predicciones[1][1],
                       "predicciones3_value": predicciones[2][1],
                       "predicciones4_value": predicciones[3][1],
                       "predicciones5_value": predicciones[4][1]})
    else:
        return render(request, '../templates/login.html')


def registroView(request):
    return render(request, '../templates/registro.html')


def perfilView(request):
    global userIDGlobal
    getDataTemp = getDataUser(userIDGlobal)
    return render(request, '../templates/perfil.html', getDataTemp)
