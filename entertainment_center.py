import media
import fresh_tomatoes

limitless = media.Movie("Limitless",
                        "Story of a pill which grants limitless intellectual capabilities.",
                        "https://ia.media-imdb.com/images/M/MV5BYmViZGM0MGItZTdiYi00ZDU4LWIxNDYtNTc1NWQ5Njc2N2YwXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UY1200_CR100,0,630,1200_AL_.jpg",
                        "https://www.youtube.com/watch?v=4TLppsfzQH8")

venom = media.Movie("Venom",
                    "Story of an alien symbiote which parasitizes a human and grants superpowers.",
                    "https://upload.wikimedia.org/wikipedia/en/0/05/Venom_poster.jpg",
                    "https://www.youtube.com/watch?v=u9Mv98Gr5pY")

avengers = media.Movie("Avengers: Infinity War",
                       "Story of Marvel superheroes uniting to defend their universe against Thanos",
                       "https://vignette.wikia.nocookie.net/movie-ideas2293/images/4/45/Avengers-_Infinity_War.jpg/revision/latest?cb=20170106112109",
                       "https://www.youtube.com/watch?v=QwievZ1Tx-8")
                    
wanted = media.Movie("Wanted",
                     "Story of a man who joins an elite group of vigilantes in order to escape",
                     "https://vignette.wikia.nocookie.net/scratchpad/images/3/3a/2008_-_Wanted_Movie_Poster.jpg/revision/latest?cb=20140306191008",
                     "https://www.youtube.com/watch?v=edpEspHOeVU")
                    

movies = [limitless, venom, avengers, wanted]
fresh_tomatoes.open_movies_page(movies)



                    
