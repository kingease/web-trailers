from media import Movie
from fresh_tomatoes import open_movies_page

finding_nemo = Movie("Finding Nemo",
                     "https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg",
                     "https://www.youtube.com/watch?v=wZdpNglLbt8")

shool_rock = Movie("School of Rock",
                   "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                   "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

Hermano = Movie("Hermano",
                "https://upload.wikimedia.org/wikipedia/en/4/4e/Hermano.jpg",
                "https://www.youtube.com/watch?v=noDyc2JocB4")


movies = [finding_nemo, shool_rock, Hermano]
open_movies_page(movies)