# from datetime import datetime -REMOVING TEST ONLY 
from flask import (Flask, render_template, abort, jsonify, request, 
                    redirect, url_for)


from model import db, save_db

app = Flask(__name__)

@app.route("/") #becomes a view function. assigns a url to our function
def welcome():
    return render_template('welcome.html', 
    cards=db)

@app.route("/card<int:index>") #unique url for each card
def card_view(index):
    try: #we are using try in order since we are doing some error handling
        card = db[index]
        return render_template("card.html", 
                                card=card,
                                index=index,
                                max_index=len(db)-1) #assigning the value to the last number of the max index
    except IndexError: 
        abort (404) #abort is the word to use when you want to give a 404 error

@app.route('/add_card', methods=["GET", "POST"])
def add_card():
    if request.method == "POST":
        # form has been submitted, process data
        card = {"question": request.form['question'],
                "answer": request.form['answer']}
        db.append(card)
        save_db()
        return redirect(url_for('card_view', index=len(db)-1))
    else:
        return render_template("add_card.html")

@app.route('/remove_card', )


@app.route('/remove_card/<int:index>', methods=["GET", "POST"])
def remove_card(index):
    try:
        if request.method == "POST":
            del db[index]
            save_db()
            return redirect(url_for('welcome'))
        else:
            return render_template("remove_card.html", card=db[index])
    except IndexError:
        abort(404)



def api_card_list():
    return jsonify(db)


@app.route("/api/card/<int:index>")
def api_card_detail(index):
    try:
        return db[index]
    except IndexError:
        abort(404)

#REMOVING - TEST ONLY
# @app.route("/date")
# def date():
#     return "This page was served at" + str(datetime.now())

# counter = 0

# @app.route("/count_views")
# def count_views():
#     global counter #use the global keyword to get the counter var
#     counter += 1
#     return "This page was viewed " +str(counter) + "times"



