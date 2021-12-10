from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet 
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SQLALCHEMY'] = True 
app.config['SECRET_KEY'] = 'anothersecretanothersession'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False 
app.config['TESTING'] = True 
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def get_homepage():
    """Gets Homepage"""
    # Get the pets from the database 
    pets = Pet.query.all()
    
    return render_template("home.html", pets=pets)
    
@app.route('/add', methods=["GET", "POST"])
def get_add_form():
    """Gets Add Pet Form"""
    form = AddPetForm()
    
    if form.validate_on_submit():
        # Get values from form 
        name = form.name.data 
        species = form.species.data 
        photo_url = form.photo_url.data 
        age = form.age.data 
        notes = form.notes.data
        
        # Create Pet Intance object 
        newPet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        
        # Add to database 
        db.session.add(newPet)
        db.session.commit()
        
        return redirect("/")
    else:
        return render_template("add_pet_form.html", form=form)
        
@app.route('/<petId>', methods=["GET", "POST"])
def pet_details_edit_page(petId):
    """Get Pet Details Page"""
    # Get Pet from database 
    pet = Pet.query.get(petId)
    
    # Create form instance 
    form = EditPetForm()
    
    # Get values from form 
    if form.validate_on_submit():
        photo_url = form.photo_url.data 
        notes = form.notes.data 
        available = form.available.data
        
        if photo_url:
            pet.photo_url = photo_url 
        if notes:
            pet.notes = notes 
        pet.available = available  
        
        # Save updated pet in db session 
        db.session.add(pet)
        db.session.commit()
        
        return redirect("/")
    else:
        return render_template("pet-details.html", pet=pet, form=form)
    
    