import media
import somewhat_fresh_tomatoes

# A list that stores all the movie objects
movie_list = [
    media.movie("Weird Science",
                "https://s-media-cache-ak0.pinimg.com/736x/3f/41/cd/3f41cdad752a683c6576fb73af689e6e.jpg",
                "https://youtu.be/X2T9GsH2jiw"),
    media.movie("Goonies",
                "http://farm5.static.flickr.com/4044/4651234215_b994973479_b.jpg",
                "https://youtu.be/hJ2j4oWdQtU"),
    media.movie("Lost Boys",
                "http://www.impawards.com/1987/posters/lost_boys.jpg",
                "https://youtu.be/zDQ0_lXClxc"),
    media.movie("Ferris Buellers Day Off",
                "http://img.moviepostershop.com/ferris-buellers-day-off-movie-poster-1986-1010280840.jpg",
                "https://youtu.be/D6gABQFR94U"),
    media.movie("Ghostbusters",
                "http://t3.gstatic.com/images?q=tbn:ANd9GcRJG5IBNzP5r0lNiVbjvc-V4ejuqDRWorvC9cAx8eBYQ4hb5eVY",
                "https://youtu.be/vntAEVjPBzQ"),
    media.movie("The Blues Brothers",
                "https://images-na.ssl-images-amazon.com/images/I/411REVXVNEL._SY445_.jpg",
                "https://youtu.be/2HCR4c1zPyk")
]

# function call  to render the page in browser using fresh_tomatoes
somewhat_fresh_tomatoes.open_movies_page(movie_list)
