from flask import Flask
from flask import redirect, url_for
app = Flask(__name__)

@app.route('/')
def accueil():
    mots = ["bonjour", "à", "toi,", "visiteur."]
    puces = ''.join("<li>{}</li>".format(m) for m in mots)
    return """<!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8" />
    <title>{titre}</title>
    </head>
    <body>
    <h1>{titre}</h1>
    <ul>
    {puces}
    </ul>
    </body>
    </html>""".format(titre="Bienvenue !", puces=puces)

if __name__ == '__main__':
    app.run(debug=True)
