import browse_best_movies
import media
#1. 1st Movie
baahubali_2 = media.Movie("Baahubali 2: The Conclusion", "IMDB: 9.2","Shiva, the son of Bahubali, begins to search for answers after he learns about his heritage.","https://www.desiretrees.in/wp-content/uploads/2017/01/Bahubali-2-Posters.jpg","https://www.youtube.com/watch?v=qD-6d8Wo3do")
#2. The __init__ function from media.py that has class movie gets called.

#3. 2nd Movie
star_wars = media.Movie("Star Wars", "IMDB: 8.7","After Princess Leia, the leader of the Rebel Alliance, is held hostage by Darth Vader, Luke and Han Solo must free her and destroy the powerful weapon created by the Galactic Empire.","https://lumiere-a.akamaihd.net/v1/images/Star-Wars-New-Hope-IV-Poster_c217085b.jpeg?region=49%2C43%2C580%2C914&width=480","https://www.youtube.com/watch?v=367FSjWvNB4")

#4. 3rd Movie
the_imitation_game = media.Movie("The Imitation Game", "IMDB: 8.1","British mathematician Alan Turing builds a machine, which is a prototype of the modern computer, to decipher German codes. This helps to save millions of lives during the Second World War.","http://t0.gstatic.com/images?q=tbn:ANd9GcQQ5vi9xgRkP0nk5aRn8tcGEGRnOQyM-aAS1ldqfQSi_69V1yfU","https://www.youtube.com/watch?v=S5CjKEFb-sM")

#5. 4th Movie
moana = media.Movie("Moana", "IMDB: 7.7","A spirited teenager who sails out on a daring mission to prove herself a master wayfinder and fulfill her ancestors' unfinished quest.","http://t3.gstatic.com/images?q=tbn:ANd9GcTJOaSVrzlgewVqmUgUz4W5ty2KUeHH6s-aYSIr_Qw8v2EBrtCS","https://www.youtube.com/watch?v=LKFuXETZUsI")

#6. 5th Movie
american_history_x = media.Movie("American History X", "IMDB: 8.5","A former neo-nazi skinhead tries to prevent his younger brother from going down the same wrong path that he did after he was sent to prison for three years.","http://onesheetdesign.com/wp-content/uploads/American_History_X.jpg","https://www.youtube.com/watch?v=XfQYHqsiN5g")

#7. 6th Movie
pineapple_express = media.Movie("Pineapple Express", "IMDB: 7","Dale, a pot-smoking process server, and his drug dealer Saul must run for their lives after Dale drops his stash at the spot where they witness a corrupt cop and a drug lord murder an Asian man.","http://www.gstatic.com/tv/thumb/movieposters/176350/p176350_p_v8_ao.jpg","https://www.youtube.com/watch?v=BWZt4v6b1hI")

#8. 7th Movie
toy_story = media.Movie("Toy Story", "IMDB: 8.3","Andy's favourite toy, Woody, is worried that after Andy receives his birthday gift, a new toy called Buzz Lightyear, his importance may get reduced. He thus hatches a plan to eliminate Buzz.","http://www.impawards.com/1995/posters/toy_story_ver1.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")

#9. 8th Movie
now_you_see_me_2 = media.Movie("Now You See You Me 2", "IMDB: 6.5","After fleeing from a stage show, the illusionists (Jesse Eisenberg, Woody Harrelson) known as the Four Horsemen find themselves in more trouble in Macau, China.","http://t3.gstatic.com/images?q=tbn:ANd9GcRjYRoNdaikER28TpUic4eKek-asQ0VN3335De6sAZOD7RJoXOl","https://www.youtube.com/watch?v=4I8rVcSQbic")

#10. 9th Movie
the_godfather = media.Movie("The Godfather", "IMDB: 9.2","Don Vito Corleone, head of a mafia family, decides to hand over his empire to his youngest son Michael. However, his decision unintentionally puts the lives of his loved ones in grave danger.","http://keyartdesigns.com/wp-content/uploads/2010/09/the-godfather-movie-poster-1020243893.jpg","https://www.youtube.com/watch?v=sY1S34973zA")

#11. 10th Movie
gangs_of_wasseypur = media.Movie("Gangs of Wasseypur", "IMDB: 8.3","A gangster (Manoj Bajpayee) clashes with the ruthless, coal-mining kingpin (Tigmanshu Dhulia) who killed his father (Jaideep Ahlawat).","http://t0.gstatic.com/images?q=tbn:ANd9GcRI4ibSpGKvC3IauCpoBJmiqwYyYcNTZl6RU2k4IDCpLaACqdxW","https://www.youtube.com/watch?v=9ZpPQdrHfl8")

#12. 11th Movie
to_kill_a_mockingbird = media.Movie("To Kill a Mockingbird", "IMDB: 8.3","Atticus Finch, a lawyer living in a racist town, sets out to defend a black man, who is accused of raping a white woman. Will Atticus succeed in changing the views of the townspeople?","https://images-na.ssl-images-amazon.com/images/I/51P2YBBDVEL.jpg","https://www.youtube.com/watch?v=KR7loA_oziY")

#13. 12th Movie
taxi_driver = media.Movie("Taxi Driver", "IMDB: 8.3","Travis, an ex-marine and Vietnam veteran who works as a taxi driver in New York City, is driven to save a preadolescent prostitute from her pimp in an effort to clean the city of its sleaze.","http://www.impawards.com/1976/posters/taxi_driver_ver4.jpg","https://www.youtube.com/watch?v=cujiHDeqnHY")

movies = [baahubali_2, star_wars, the_imitation_game, moana, american_history_x, pineapple_express, toy_story, now_you_see_me_2, the_godfather, gangs_of_wasseypur, to_kill_a_mockingbird, taxi_driver]                   
browse_best_movies.open_movies_page(movies)                   
