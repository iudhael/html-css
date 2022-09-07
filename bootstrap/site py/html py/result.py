"""
la ligne suivante n'est utiliser qu'en developpemet
l'enlever ou le mettre en commentaire lorsque le site est en ligne

    Activation du mode debuggue
"""
cgitb.enable()

# recuperation des données par la creation d'un form
form = cgi.FieldStorage()

# toujours filtrer les champs de formulaire
# verifier si le champs 'username' existe


    # definir l'entete
print("Content-type: text/html; charset=utf-8\n")

html = """ <!DOCTYPE html>
<head>
    <meta charset="utf-8">
    <title>www.MonCV.com</title>
</head>
<body>
    <h1>Page de resultat</h1>
"""
print(html)


try:
    if form.getvalue("username"):
        # si le champs existe
        username = form.getvalue("name")
        print(f"<p>Bonjour {username} !</p>")

        # print("<script>alert('ok')</script>")

    else:
        raise Exception("Nom non transmis")
except:
    print("<p>Nom non transmis</>")
"""
try:
    if form.getvalue("surname"):
        # si le champs existe
        surname = form.getvalue("surname")
        print(f"<p>Bonjour {surname} !</p>")

        # print("<script>alert('ok')</script>")

    else:
        raise Exception("Prénom non transmis")
except:
    print("<p>Prénom non transmis</>")


try:
    if form.getvalue("username"):
        # si le champs existe
        username = form.getvalue("username")
        print(f"<p>Bonjour {username} !</p>")

        # print("<script>alert('ok')</script>")

    else:
        raise Exception("Pseudo non transmis")
except:
    print("<p>Pseudo non transmis</>")

"""




html = """

</body>
</html>
"""

print(html)


