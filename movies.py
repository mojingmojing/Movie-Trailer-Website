import media
import fresh_tomatoes

# Creat movie instances

# Toy Story movie: movie title, storyline, poster image and movie trailer
toy_story = media.Movie(
  "Toy Story",
  "A story of a boy and his toys that come to life",
  "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
  "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# Beauty and The Beast movie: movie title, storyline, poster
# image and movie trailer
beauty_and_beast = media.Movie(
  "Beauty and The Beast",
  "A love story about a girl and a beast in the castle",
  "https://upload.wikimedia.org/wikipedia/en/d/d6/Beauty_and_the_Beast_2017_poster.jpg",  # NOQA
  "https://www.youtube.com/watch?v=e3Nl_TCQXuw")

# Avatar movie: movie title, storyline, poster image and movie trailer
avatar = media.Movie(
  "Avatar",
  "A marine on an alien planet",
  "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
  "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# Despicable Me movie: movie title, storyline, poster image and movie trailer
despicable_me = media.Movie(
  "Despicable Me",
  "Gru with his three girls and cute minnions",
  "https://upload.wikimedia.org/wikipedia/en/d/db/Despicable_Me_Poster.jpg",
  "https://www.youtube.com/watch?v=zzCZ1W_CUoI")

# Zootopia movie: movie title, storyline, poster image and movie trailer
zootopia = media.Movie(
  "Zootopia",
  "Story of a brave bunny police",
  "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",
  "https://www.youtube.com/watch?v=jWM0ct-OLsM")

# Finding Nemo movie: movie title, storyline, poster image and movie trailer
finding_nemo = media.Movie(
  "Finding Nemo",
  "Story about a father clownfish finding his son Nemo",
  "https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg",
  "https://www.youtube.com/watch?v=wZdpNglLbt8")

# Put movie instances in a list
# Set the movies that will be passed to the media file
movies = [
  toy_story,
  beauty_and_beast,
  avatar,
  despicable_me,
  zootopia,
  finding_nemo
  ]

# Call open_movies_page function in fresh_tomatoes.py file
# Open the HTML file in a webbrowser via the fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
