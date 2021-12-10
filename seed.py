"""Seed File"""

from models import Pet, db 
from app import app 

# Create all tables 
db.drop_all()
db.create_all()

# If table isn't empty, empty it 
Pet.query.delete()

# Add pets 
pet1 = Pet(name="Rhys", species="Mini Aussie", photo_url="https://www.akc.org/wp-content/uploads/2017/11/Australian-Shepherd.1.jpg", age="2", notes="Great Dog")

pet2 = Pet(name="Peggie", species="Mini Aussie", photo_url="https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F47%2F2020%2F08%2F15%2Fblack-tan-australian-shepherd-1000483560-2000.jpg", age="4", notes="Great Dog")

# Add new objects to session
db.session.add(pet1)
db.session.add(pet2)

db.session.commit()