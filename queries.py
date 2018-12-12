# coding=utf-8

# 1 - imports
from datetime import date
from src.model.base import Session, Base, engine
from src.model.movies import Movie


Base.metadata.create_all(engine)


# 2 - extract a session
session = Session()


bourne_identity = Movie("The Bourne Identity", date(2002, 10, 11))
furious_7 = Movie("Furious 7", date(2015, 4, 2))
pain_and_gain = Movie("Pain & Gain", date(2013, 8, 23))


# 9 - persists data
session.add(bourne_identity)
session.add(furious_7)
session.add(pain_and_gain)


session.commit()
session.close()


session = Session()
# 3 - extract all movies
movies = session.query(Movie).all()



# 4 - print movies' details
print('\n### All movies:')
for movie in movies:
    print(f'{movie.title} was released on {movie.release_date}')
print('')
