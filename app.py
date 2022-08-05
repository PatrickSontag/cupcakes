"""Flask app for Cupcakes"""

from flask import Flask, request, redirect, render_template, jsonify
# from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "SECRET!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# debug = DebugToolbarExtension(app)

connect_db(app)



# @app.route('/')
# def home_page():
#     """Shows home page"""

#     cupcakes = Cupcake.query.all()
    
#     return render_template('home.html')

@app.route('/api/cupcakes')
def all_cupcakes():
    """Shows all cupcakes."""

    cupcakes = Cupcake.query.all()
    serialized = [serialize_cupcake(cc) for cc in cupcakes]
    
    return jsonify(cupcakes=serialized)

@app.route('/api/cupcakes/<int:cup_id>')
def single_cupcake(cup_id):
    """Shows cupcake page"""

    cupcake = Cupcake.query.get_or_404(cup_id)
    serialized = serialize_cupcake(cupcake)
    
    return jsonify(cupcake=serialized)
    
@app.route('/api/cupcakes', methods=["POST"])
def add_cupcake():
    """Add new cupcake"""

    data = request.json

    cupcake = Cupcake(
        flavor=data['flavor'],
        rating=data['rating'],
        size=data['size'],
        image=data['image'] or None)

    db.session.add(cupcake)
    db.session.commit()
    
    return (jsonify(cupcake=cupcake.serialize_cupcake()), 201)