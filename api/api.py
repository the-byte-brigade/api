from flask import Flask, redirect, render_template, request, jsonify, flash, get_flashed_messages
from bson import ObjectId
from pymongo import MongoClient


app = Flask(__name__)

app.secret_key = 'mysecretkey'


client = MongoClient()
db = client.cat
collection = db.user
collection1 = db.report


@app.route('/submit', methods=['GET','POST'])
def submit():
    firstName = request.form['first-name']
    lastName = request.form['last-name']
    email = request.form['email']
    address= request.form['address']
    city=request.form['city']
    state=request.form['state']
    country=request.form['country']
    phoneNumber=request.form['phone-number']
    animalPreference=request.form['animal-preference']
    color=request.form['color']
    gender=request.form['gender']
    breed=request.form['breed']
    follow_up_reports=request.form['follow-up-reports']
    re_home_pet=request.form['re-home-pet']

    data = {'first-name': firstName, 'last-name': lastName, 'email': email, 'address': address,  'city': city, 'state': state, 'country': country, 'phone-number': phoneNumber, 'animal-preference':animalPreference,  'color': color, 'gender': gender, 'breed': breed, 'follow-up-reports':follow_up_reports, 're-home-pet': re_home_pet }
    collection.insert_one(data)



@app.route('/submitreport', methods=['GET','POST'])
def reportSubmit():
    location=request.form['address']
    city1=request.form['city']
    state1=request.form['state']
    country1=request.form['country']
    animalPreference1=request.form['animal-preference']
    danger=request.form['danger']
    moreDetails=request.form['other-questions']

            
    data1= {'address':location, 'city':city1, 'state': state1, 'country': country1, 'animal-preference': animalPreference1, 'danger': danger, 'other-questions': moreDetails}          
    collection1.insert_one(data1)

    results = []
    for doc in collection.find():
        doc['_id'] = str(doc['_id'])
        results.append(doc)
            
    # Convert the list of dictionaries to JSON format and return it as a response
    return jsonify(results)
    #print(data)

# create a HTML form
@app.route('/adopt')
def adopt():
    submit()

@app.route('/report')
def report():
    reportSubmit()

if __name__ == '__main__':
    app.run(debug=True)
