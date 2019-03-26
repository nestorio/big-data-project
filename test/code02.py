from flask import Flask, request
app = Flask(__name__)
@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    if request.method == 'GET':
        # afficher le formulaire
        pass
    else:
        # traiter le formulaie
        # afficher: merci de m'avoir laissé un message
        pass

if __name__ == "__main__":
    app.run(debug=True)