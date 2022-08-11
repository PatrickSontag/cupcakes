"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    """User"""
    __tablename__ = "cupcakes"

    # def __repr__(self):
    #     return f"<User id={self.id}, first name={self.first_name}, last name={self.last_name}, image={self.image}>"
    def serialize_cupcake(cupcake):
        """Serialize a cupcake SQLAlchemy obj to dictionary."""

        return{
            "id": cupcake.id,
            "flavor": cupcake.flavor,
            "size": cupcake.size,
            "rating": cupcake.rating,
            "image": cupcake.image
        }

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    flavor = db.Column(db.String(),
                    nullable=False)
    size = db.Column(db.String(),
                    nullable=False)
    rating = db.Column(db.Float,
                    nullable=False)
    image = db.Column(db.String(),
                    default="https://tinyurl.com/demo-cupcake")

