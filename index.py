import random

jokes = [
    "Why does a chicken coup have 2 doors? Because if it had 4 doors, it would be a chicken Sedan.",
    "What do get when you cross 50 female pigs with 50 male deer? One hundred sows and bucks?",
    "Overheated some milk in a lab experiment today... ...and asked the teacher if it would affect the result. Her response? \"To a degree.\"",
    "What's my New Year resolution? Well, I just got a Hi-Def TV, so it's 1920 X 1080i.",
    "What did one earthquake say to the other? Hey, it's not my fault."
]

print("Welcome to the Random Joke Generator")
input("Press enter to generate a joke: ")

play_again = True

while play_again:
    print(random.choice(jokes))
    play_again = input("Press any key to get another joke, or 'q' to quit: ")
print("Thanks for playing! See you next time")