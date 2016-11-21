import fresh_tomatoes
import media

the_matrix = media.Movie("The Matrix",
                         "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BMDMyMmQ5YzgtYWMxOC00OTU0LWIwZjEtZWUwYTY5MjVkZjhhXkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_SY1000_CR0,0,723,1000_AL_.jpg",
                         "https://www.youtube.com/watch?v=m8e-FF8MsqU")
#print (the_matrix.storyline)
#the_matrix.show_trailer()

the_matrix_reloaded = media.Movie("The Matrix Reloaded",
                                  "Neo and the rebel leaders estimate that they have 72 hours until 250,000 probes discover Zion and destroy it and its inhabitants. During this, Neo must decide how he can save Trinity from a dark fate in his dreams.",
                                  "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA0NDM5MDY2OF5BMl5BanBnXkFtZTcwNzg5OTEzMw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                                  "https://www.youtube.com/watch?v=kYzz0FSgpSU")
#print (the_matrix_reloaded.storyline)
#the_matrix_reloaded.show_trailer()

the_matrix_revolutions = media.Movie("The Matrix Revolutions",
                                     "The human city of Zion defends itself against the massive invasion of the machines as Neo fights to end the war at another front while also opposing the rogue Agent Smith.",
                                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTkyNjc4NTQzOV5BMl5BanBnXkFtZTcwNDYzMTQyMQ@@._V1_.jpg",
                                     "https://www.youtube.com/watch?v=hMbexEPAOQI")
#print (the_matrix_revolutions.storyline)
#the_matrix_revolutions.show_trailer()

movies = [the_matrix, the_matrix_reloaded, the_matrix_revolutions]
#fresh_tomatoes.open_movies_page(movies)
print (media.Movie.VALID_RATINGS)
