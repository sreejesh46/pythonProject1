import random

def get_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "I'm reading a book about anti-gravity. It's impossible to put down!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I used to play piano by ear, but now I use my hands.",
        "Why don't skeletons fight each other? They don't have the guts!"
    ]
    return random.choice(jokes)

def main():
    joke = get_joke()
    print(joke)

if __name__ == "__main__":
    main()
