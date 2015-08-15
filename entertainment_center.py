import fresh_tomatoes
import media


# specific instances of my favorite movies using media.Movie
# shortened urls with lit.ly
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that comes to life",
                        "http://bit.ly/1UJnhS7",
                        "https://youtu.be/KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on a alien planet",
                     "http://bit.ly/1MsW9FC",
                     "https://youtu.be/5PSNL1qE6VY")

godfather = media.Movie("The Godfather",
                        "Mafia",
                        "http://bit.ly/1JiuIxN",  # noqa
                        "https://youtu.be/sY1S34973zA")

star_wars = media.Movie("Star Wars",
                        "Star Wars",
                        "http://bit.ly/1PqJvW4",  # noqa
                        "https://youtu.be/367FSjWvNB4?t=16s")

rounders = media.Movie("Rounders",
                       "Rounders",
                       "http://bit.ly/1DRqyLa",  # noqa
                       "https://youtu.be/sV5f97wqeW4")

swingers = media.Movie("Swingers",
                       "Swingers",
                       "http://bit.ly/1IRVyr0",  # noqa
                       "https://youtu.be/nWCct8XbQD0")

movies = [toy_story, avatar, godfather, star_wars, rounders, swingers]
fresh_tomatoes.open_movies_page(movies)
