from flask import Blueprint,render_template,request,flash, jsonify
from petml import load_csv,fill_missing_values,variables,inputs,prediction, train_model
from flask import Flask, request, render_template, session, redirect, url_for
import petml as ml 
from flask_login import login_required, current_user
from .model import Review
from . import db 
import json


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/secpage',methods= ['POST', 'GET'])
def secpage():
    affection = None
    vaccinated = None
    age = None
    weight = None
    appetite = None
    injury = None
    wound = None
    
    if request.method == 'POST':
        data = load_csv()
        fill_missing_values(data)
        # X,y = variables()
        # model = model_train(X,y)
        model = train_model()
        affection = request.form.get('affection')
        vaccinated = request.form.get('vaccination')
        age = request.form.get('age')
        weight = request.form.get('weight')
        appetite =request.form.get('appetite')
        injury= request.form.get('injury')
        wound=request.form.get('wound')
        #input()
        prediction = ml.prediction(affection,vaccinated,age,weight,appetite,injury,wound)
         # Store the prediction in the session
        session['prediction'] = prediction
        
        # Redirect to the results page
        return redirect(url_for('views.results'))
    return render_template("secpage.html")

@views.route('/results')
def results():
    # Get the prediction from the session
    prediction = session.get('prediction', None)
    
    return render_template('results.html', prediction=prediction)

@views.route('/health_tips')
def health_tips():
    return render_template("health_tips.html")

@views.route('/reviews')
def reviews():
    return render_template("reviews.html")

@views.route('/contact')
def contact():
    return render_template("contact.html")

@views.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")

@views.route('/petsday')
def petsday():
    return render_template("petsday.html")

@views.route('/appointment')
def appointment():
    return render_template("appointment.html")

@views.route('/write', methods=['GET','POST'])
@login_required
def reviews():
    if request.method == 'POST':
        review = request.form.get('review')
        pet = request.form.get('animal')

        if len(review)<=1:
            flash('Review is too short!', category='error')
        else:
            new_review=Review(pet=pet, data=review, user_id=current_user.id)
            db.session.add(new_review)
            db.session.commit()
            flash('Review added successfully!', category='success')


    return render_template("write.html", user=current_user)

@views.route('delete-review', method=['POST'])
def delete_review():
    review = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    review = review['reviewId']
    review = Review.query.get(reviewId)
    if review:
        if review.user_id == current_user.id:
            db.session.delete(review)
            db.session.commit()

    return jsonify({})