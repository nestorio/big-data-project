from flask import Flask, request
app = Flask(__name__)

@app.route('/discussion/page/<num_page>')
def discussion(num_page):
    try:
        num_page = int(num_page)
    except:
        print("BAD REQUEST")
    first_msg = 1 + 50 * (num_page-1)
    second_msg = first_msg + 50
    return "Affichage des messages {} {}".format(first_msg, second_msg)
     
if __name__ == "__main__":
    app.run(debug=True)