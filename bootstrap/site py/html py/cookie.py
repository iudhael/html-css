# coding:utf-8
import cgi

# pour les cookies
import http.cookies
import datetime

# Lecture du cookie
import os

# ces 2 modules permettront de gerer  les accents, defauts d'affichages
import sys
import codecs

# remodifier l'encodage pour la sortie stadard
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())



    # definir l'entette du cookie toujour avant tout code

    # expiration du cookie dans 1 an avec timedelta
expiration = datetime.datetime.now()   + datetime.timedelta(days=365)
    # formatage de la date
expiration = expiration.strftime("%a, %d-%b-%Y %H:%M:%S")


my_cookie = http.cookies.SimpleCookie()
    # on fonctionne comme un dictionnaire
my_cookie["pref_lang"] = "fr"
my_cookie["pref_lang"]["expires"] =expiration
my_cookie["pref_lang"]["httponly"] = True

    # generer ou enregistrer  le cookie
print(my_cookie.output())


# definir l'entete format ---> ( nom de l'entete: type; valeur)
print("Content-type: text/html; charset=utf-8\n")

html = """ <!DOCTYPE html>
<head>
    <meta charset="utf-8">
    <title>Ma page web</title>
</head>
<body>
    <h1>Page web avec python CGI</h1>

    <h2>Cookies avec python</h2>  
"""
print(html)

# lire le cookie enregistrer
# variable d'environnement pour un cookie HTTP_COOKIE

try:
    # recuperer la langue
    user_lang = http.cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
    # envoie la valeur de pref_lang qui est fr
    print("La langue choisie par l'utilisateur est :", user_lang["pref_lang"].value)

except(http.cookies.CookieError, KeyError):
    print("Non trouvé")

html = """
</body>
</html>
"""

print(html)

