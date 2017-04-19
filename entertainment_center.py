import media
import fresh_tomatoes
##Creating instances of media.Movie with some of my favorite movies.

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://www.cinesift.com/#/?id=114709",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "1h 21m",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

wall_e = media.Movie("Wall-e",
                     "A robot falls in love",
                     "http://www.cinesift.com/#/?id=910970",
                     "http://www.gamershell.com/static/boxart/large/17870.jpg",
                     "1h 44m",
                     "https://www.youtube.com/watch?v=ZisWjdjs-gM")

zootopia = media.Movie("Zootopia",
                       "The first rabbit police officer comes to terms with her narrow mindedness while trying to solve her first case",
                       "http://www.cinesift.com/#/?id=4865928",
                       "https://lh3.googleusercontent.com/qlxBnASxAN35_JMRPT94NZA37BgpvxveC1WzjUjFigPMN3WNqAaYKF9FY8KRJpbIl9c=w300",
                       "1h 50m",
                       "https://www.youtube.com/watch?v=jWM0ct-OLsM")

tropic_thunder = media.Movie("Tropic Thunder",
                                "A group of actors set out to film the most expensive war film ever made",
                                "http://www.cinesift.com/#/?id=942385",
                                "http://vgboxart.com/boxes/MOVIE/21756-tropic-thunder.png?t=1219716340",
                                "2h 1m",
                                "https://www.youtube.com/watch?v=T-6YhRZowgc")

old_school = media.Movie("Old School",
                         "A group of middle age men become founders of the most popular fraternity in town",
                         "http://www.cinesift.com/#/?id=302886",
                         "https://s-media-cache-ak0.pinimg.com/736x/e3/01/5c/e3015c798366e5344e3cc765a8c1ef9d.jpg",
                         "1h 33m",
                         "https://www.youtube.com/watch?v=VqtymOtKr48")

intersteller = media.Movie("Intersteller",
                           "A team of explorers travel through a wormhole to attempt to find habitable planets for the sake of humanity",
                           "http://www.cinesift.com/#/?id=816692",
                           "https://images-na.ssl-images-amazon.com/images/I/51CP2Vlm8%2BL.jpg",
                           "2h 49m",
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA")

gone_girl = media.Movie("Gone Girl",
                        "A man's wife goes missing on their fifth wedding aniversery, and he's the number one suspect",
                        "http://www.cinesift.com/#/?id=2267998",
                        "http://resizing.flixster.com/JpCcarCquFsa_wVQQpGr3Oz4SLo=/800x1200/v1.bTsxMTE4OTI1OTtqOzE3MzI4OzIwNDg7ODAwOzEyMDA",
                        "2h 29m",
                        "https://www.youtube.com/watch?v=Ym3LB0lOJ0o")

there_will_be_blood = media.Movie("There Will be Blood",
                           "Chronicles of an oil tycoon",
                           "http://www.cinesift.com/#/?id=469494",
                           "http://cdn.collider.com/wp-content/uploads/there_will_be_blood_movie_poster_rolling_roadshow_2010_olly_moss.jpg",
                           "2h 38m",
                           "https://www.youtube.com/watch?v=FeSLPELpMeM")

city_of_god = media.Movie("City of God",
                          "The story of a photographer that is documenting a voilent gang war on the streets of Rio De Janeiro",
                          "http://www.cinesift.com/#/?id=317248",
                          "https://lh6.ggpht.com/hbO9T7Aaa00CuIBmX7Evg_0y8wdhcS88m5UaEFV_HxKXTghywF9fK4g_OWPrSZCw9wcI=w300",
                          "2h 15m",
                          "https://www.youtube.com/watch?v=ioUE_5wpg_E")



movies = [toy_story, wall_e, zootopia, tropic_thunder, old_school, intersteller, gone_girl, there_will_be_blood, city_of_god]

fresh_tomatoes.open_movies_page(movies)
