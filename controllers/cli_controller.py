from datetime import datetime

from flask import Blueprint

from init import db, bcrypt
from models.users import User
from models.reviews import Review
from models.status import Status
from models.types import Type
from models.ratings import Rating
from models.genres import Genre
from models.reviews_genres import ReviewsGenres

db_commands = Blueprint('db', __name__)

@db_commands.cli.command('create')
def create_tables():
    db.create_all()
    print("Tables created")

@db_commands.cli.command('drop')
def drop_tables():
    db.drop_all()
    print("Tables dropped")

@db_commands.cli.command('seed')
def seed_tables():
    users = [
        User(
            username="admin",
            password=bcrypt.generate_password_hash('toor').decode('utf-8'),
            is_admin=True
        ),
        User(
            username="user1",
            password=bcrypt.generate_password_hash('password').decode('utf-8'),
        )
    ]

    db.session.add_all(users)

    status = [
        Status(
            status="Plan to watch"
        ),
        Status(
            status="Watching"
        ),
        Status(
            status="Completed"
        ),
        Status(
            status="Re-watching"
        ),
        Status(
            status="On hold"
        ),
        Status(
            status="Dropped"
        ),
    ]

    db.session.add_all(status)

    types = [
        Type(
            type="Series"
        ),
        Type(
            type="Movie"
        ),
    ]

    db.session.add_all(types)

    ratings = [
        Rating(
            rating="1 Star"
        ),
        Rating(
            rating="2 Star"
        ),
        Rating(
            rating="3 Star"
        ),
        Rating(
            rating="4 Star"
        ),
        Rating(
            rating="5 Star"
        )
    ]

    db.session.add_all(ratings)

    genres = {
        Genre(
            genre="Action"
        ),
        Genre(
            genre="Adventure"
        ),
        Genre(
            genre="Comedy"
        ),
        Genre(
            genre="Dark"
        ),
        Genre(
            genre="Drama"
        ),
        Genre(
            genre="Fanstasy"
        ),
        Genre(
            genre="Historical"
        ),
        Genre(
            genre="Horror"
        ),
        Genre(
            genre="Isekai"
        ),
        Genre(
            genre="Mystery"
        ),
        Genre(
            genre="Post-Apocalypic"
        ),
        Genre(
            genre="Psychological"
        ),
        Genre(
            genre="Romance"
        ),
        Genre(
            genre="Sci-fi"
        ),
        Genre(
            genre="Seinen"
        ),
        Genre(
            genre="Shoujo"
        ),
        Genre(
            genre="Shounen"
        ),
        Genre(
            genre="Slice of life"
        ),
        Genre(
            genre="Supernatural"
        ),
        Genre(
            genre="Thriller"
        ),
        Genre(
            genre="Tragedy"
        ),
    }

    db.session.add_all(genres)

    reviews = [
        Review(
            user=users[0],
            title="Anime 1",
            status=status[2],
            type=types[0],
            rating=ratings[4],
            eps_watched=10,
            eps_total=24,
            date_started=datetime(2024, 1, 12),
            recom=0,
            fav=1,
            com="It was pretty good, but didn't finish"
        ),
        Review(
            user=users[1],
            title="Anime 2",
            status=status[0],
            type=types[1],
            eps_total=1,
            recom=1,
            com="I've heard it's good."
        ),
        Review(
            user=users[1],
            title="Anime 3",
            status=status[5],
            type=types[0],
            eps_total=12,
            com="Haven't gotten back around to watching this yeat."
        )
    ]

    db.session.add_all(reviews)

    db.session.commit()

    print("Tables seeded")