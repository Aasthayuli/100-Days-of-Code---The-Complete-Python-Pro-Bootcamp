from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, PrimaryKeyConstraint
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250),nullable=False)
    year = db.Column(db.Integer, nullable = False)
    description = db.Column(db.String(500), nullable = False)
    rating = db.Column(db.String, nullable = False)
    ranking = db.Column(db.Integer, nullable = False)
    review = db.Column(db.String, nullable = False)
    img_url = db.Column(db.String, nullable = False)

# Create tables if they don't exist yet
with app.app_context():
    db.create_all()

# with app.app_context():
#     if not Movie.query.filter_by(title="Phone Booth").first():
#         db.session.add(Movie(
#             title="Phone Booth",
#             year=2002,
#             description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle...",
#             rating=7.3,
#             ranking=10,
#             review="My favourite character was the caller.",
#             img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
#         ))
#
#     if not Movie.query.filter_by(title="Avatar The Way of Water").first():
#         db.session.add(Movie(
#             title="Avatar The Way of Water",
#             year=2022,
#             description="Set more than a decade after the events of the first film...",
#             rating=7.3,
#             ranking=9,
#             review="I liked the water.",
#             img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
#         ))
#
#     db.session.commit()

class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")

# New Find Movie Form
class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")

@app.route("/")
def home():
    result = db.session.execute(db.select(Movie))
    all_movies = result.scalars()
    return render_template("index.html", movies=all_movies)

# New Add Route
@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = FindMovieForm()
    return render_template("add.html", form=form)


# Adding the Update functionality
@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)

@app.route("/delete")
def delete_movie():
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
