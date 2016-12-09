import fresh_tomatoes
import media


def create_movies():
    wall_e = media.Movie("WALL-E",
                         "A Love Story of Robots",
                         "https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg",
                         "https://www.youtube.com/watch?v=8-_9n5DtKOc")
    shawshank = media.Movie("The Shawshank Redemption",
                            "Nobody else but you who can save yourself",
                            "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                            "https://www.youtube.com/watch?v=6hB3S9bIaco")
    spirited_away = media.Movie("Spirited Away",
                                "A magical travel of the ten years old girl",
                                "https://upload.wikimedia.org/wikipedia/en/3/30/Spirited_Away_poster.JPG",
                                "https://www.youtube.com/watch?v=ByXuk9QqQkk")
    movies = [wall_e, shawshank, spirited_away]
    return movies


fresh_tomatoes.open_movies_page(create_movies())
