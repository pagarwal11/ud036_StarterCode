import media
import fresh_tomatoes

godfather = media.Movie("The Godfather",
                        "Story of Italian-American crime family of " +
                        "Don Vito Corleone",
                        "https://m.media-amazon.com/images/M/MV5BM2MyNjYxNm" +
                        "UtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGde" +
                        "QXVyNzkwMjQ5NzM@._V1_UY268_CR3,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=sY1S34973zA")
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9G" +
                     "cTqnjSY4XjHDaFH4bWWeE3L3P6CyI4li0LHyZbqnBum3GS-iADwSQ",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

ratatouille = media.Movie("Ratatouille",
                          "Remy, a rat, aspires to become a renowned French" +
                          " chef",
                          "https://i.pinimg.com/originals/fd/d1/35/fdd135" +
                          "60c71adf6103a435ec44f88e56.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

interstellar = media.Movie("Interstellar",
                           "Ex-NASA pilot on a planet exploration mission" +
                           " to report which planet can sustain life",
                           "https://2.bp.blogspot.com/-bflZ1PDgwg0/VWtmJE" +
                           "SI_SI/AAAAAAAAHzE/H_s6rLmUIrU/s1600/Interstel" +
                           "lar-Main-One-Sheet-QUAD.jpg",
                           "https://www.youtube.com/watch?v=zSWdZVtXT7E")

the_dark_knight = media.Movie("The Dark Knight",
                              "Dent and Batman begin an assault on Gotham's " +
                              "organised crime",
                              "http://t0.gstatic.com/images?q=tbn:ANd9GcSY" +
                              "2Tsn17pqz9OMpWv5Y_v5ni2yN-ymmdwS_mRaOUeYJDG" +
                              "0eU7A",
                              "https://www.youtube.com/watch?v=yQ5U8suTUw0")

dunkirk = media.Movie("Dunkirk",
                      "Dunkirk evacuation(1940) in World War II",
                      "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9G" +
                      "cTaI_fYkgKQAFgpAHFbngJZ5IsbOKebH15QaCezWrFVwYV6wXm9",
                      "https://www.youtube.com/watch?v=F-eMt3SrfFU")


movies = [godfather, avatar, ratatouille,
          interstellar, the_dark_knight, dunkirk]

fresh_tomatoes.open_movies_page(movies)
