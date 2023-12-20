import random
def chatbot(x):
    while True:
        a=input("Hey {}, Wanna talk or ask me to tell a joke:".format(x))
        if "tell" in a.lower() or "joke" in a.lower() or "funny" in a.lower():
            jokes = (
            "Why don't scientists trust atoms? Because they make up everything!",
            "Parallel lines have so much in common. It’s a shame they’ll never meet.",
            "Why don't skeletons fight each other? They don't have the guts.",
            "I told my wife she was drawing her eyebrows too high. She looked surprised.",
            "What did one hat say to the other? Stay here, I'm going on ahead!",
            "Why don't oysters donate to charity? Because they are shellfish.",
            "I used to play piano by ear, but now I use my hands and fingers.",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "I only know 25 letters of the alphabet. I don't know y.",
            "What do you call fake spaghetti? An impasta!",
            "Why did the math book look sad? Because it had too many problems.",
            "I used to be a baker because I kneaded dough.",
            "Why do we never tell secrets on a farm? Because the potatoes have eyes and the corn has ears!",
            "What do you get when you cross a snowman and a vampire? Frostbite!",
            "Parallel lines have so much in common. It’s a shame they’ll never meet.",
            "Why did the bicycle fall over? Because it was two-tired!",
            "I told my wife she was drawing her eyebrows too high. She looked surprised.",
            "How does a penguin build its house? Igloos it together!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "I used to play piano by ear, but now I use my hands and fingers.")
            while True:
                rand_joke=random.choice(jokes)
                print(rand_joke)
                tell_joke=input("Do you want to say me another one?")
                if "no" in tell_joke.lower() or "not" in tell_joke.lower() or "it is ok" in tell_joke.lower() or "it's ok" in tell_joke.lower():
                    break
        elif a.lower() in ("chat","talk","chitchat"):
            print("Great to hear that from you")
            while True:
                talk=input('''what shall we talk about
                        1.Food
                        2.Movie
                        3.Travel''')
                if "food" in talk.lower()or"eat" in talk.lower():
                    print("Hey, you interested to talk about food")
                    food=input("What do you like the most")
                    print("You have a great taste mate, I like %s too"%food)
                elif "movie" in talk.lower()or "cinema" in talk.lower():
                    print("Hey, you interested to talk about movie")
                    movie=input("Which movie do you like the most")
                    print("You have a great taste mate, I like %s too"%movie)
                    hero=input("Who's your favourite hero/heroine mate?")
                    print("Your's is {} but I love Tripti....".format(hero))
                elif "travel" in talk.lower()or "place" in talk.lower():
                    print("Hola! Travel it is...Interesting")
                    travel=input("Do you travel frequently ")
                    if "yes" or "yeah" in travel.lower():
                        print("Wohooo Travel man")
                    elif "no" or "not so" in travel.lower():
                        print("Ohh i see you love to but prolly you don't find enough time")
                    place=input("Where do you love to travel the most?")
                    print("So {} is your favorite place".format(place))
                else:
                    print("Sorry didn't get you. Can you repeat please...")
                    continue
                reply=input("Do you like to go through the menu again")
                if "no" in reply.lower() or "not" in reply.lower() or "it is ok" in reply.lower() or "it's ok" in reply.lower():
                    break
        else:
            print("Sorry didn't get you. Can you repeat please...")
            continue
        again=input("Do you want to go start over mate?")
        if "no" in again.lower() or "not" in again.lower() or "it is ok" in again.lower() or "it's ok" in again.lower():
            break






print("Hey buddy! How r u doing")
name=input("Pleae enter your name:")
chatbot(name)
