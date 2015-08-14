import fresh_tomatoes
import media


# specific instances of my favorite movies using media.Movie

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that comes to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # noqa
                        "https://youtu.be/KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on a alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",  # noqa
                     "https://youtu.be/5PSNL1qE6VY")

godfather = media.Movie("The Godfather",
                        "Mafia",
                        "https://upload.wikimedia.org/wikipedia/en/c/c4/Godfather_Sdtk.jpg",  # noqa
                        "https://youtu.be/sY1S34973zA")

star_wars = media.Movie("Star Wars",
                        "Star Wars",
                        "http://img3.wikia.nocookie.net/__cb20140311211533/starwars/images/a/a9/Ep4_OST.png",  # noqa
                        "https://youtu.be/367FSjWvNB4?t=16s")

rounders = media.Movie("Rounders",
                       "Rounders",
                       "http://ia.media-imdb.com/images/M/MV5BMTc4OTcxNDY2Nl5BMl5BanBnXkFtZTgwNDg0MzkxMDE@._V1_SX214_AL_.jpg",  # noqa
                       "https://youtu.be/sV5f97wqeW4")

swingers = media.Movie("Swingers",
                       "Swingers",
                       "http://2tax3i7eqir13il3d49l65b3.wpengine.netdna-cdn.com/wp-content/uploads/2012/08/8940.jpg",  # noqa
                       "https://youtu.be/nWCct8XbQD0")

movies = [toy_story, avatar, godfather, star_wars, rounders, swingers]
fresh_tomatoes.open_movies_page(movies)
