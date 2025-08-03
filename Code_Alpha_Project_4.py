import random
import datetime

def initialize_chatbot():
    """Initialize chatbot with expanded response rules"""
    return {
        "greetings": {
            "hello": ["Hi there!", "Hello!", "Hey!", "Hi! How can I help you today?"],
            "hi": ["Hello!", "Hi!", "Hey there!", "Greetings!"],
            "hey": ["Hi!", "Hello!", "What's up?"],
            "good morning": ["Good morning!", "Rise and shine!", "Morning! Ready for a great day?"],
            "good afternoon": ["Good afternoon!", "Afternoon vibes!", "Hope you're having a productive day!"],
            "good evening": ["Good evening!", "Evening! How was your day?", "Beautiful evening, isn't it?"]
        },
        "farewells": {
            "bye": ["Goodbye!", "See you later!", "Bye! Come back soon!"],
            "goodbye": ["Farewell!", "Have a nice day!", "Goodbye! It was nice chatting!"],
            "exit": ["Chat session ended", "Goodbye!", "See you next time!"],
            "see you": ["Until next time!", "Catch you later!", "So long!"],
            "take care": ["You too!", "Will do! Stay safe!", "Thanks, bye!"]
        },
        "questions": {
            "how are you": ["I'm just a program, but I'm functioning well!", 
                           "All systems operational!", "Doing great! How about you?"],
            "what's your name": ["I'm ChatBot 1.0", "Call me CB", "I'm your friendly neighborhood chatbot"],
            "help": ["I can respond to greetings, answer questions, tell time, and more!", 
                    "Try asking about the weather, time, or just say hello",
                    "I know about movies, tech, and can even tell jokes!"],
            "who made you": ["I was created by a Python developer!", "My creator is a CodeAlpha intern"],
            "what can you do": ["I can chat, tell jokes, show current time, and discuss movies/tech!", 
                               "Try asking: 'What movies are trending?' or 'Tell me a joke'"]
        },
        "thanks": {
            "thank you": ["You're welcome!", "Anytime!", "Happy to help!"],
            "thanks": ["No problem!", "My pleasure!", "You got it!"],
            "appreciate": ["Glad I could assist!", "That's what I'm here for!"]
        },
        "apologies": {
            "sorry": ["That's okay.", "No problem at all.", "Don't worry about it."],
            "apologize": ["Accepted!", "It's alright.", "No big deal!"],
            "oops": ["Happens to the best of us!", "No worries!", "Easy fix!"]
        },
        "compliments": {
            "good job": ["Thanks! I try.", "I appreciate that!", "You made my day!"],
            "awesome": ["You're awesome too!", "Thanks a lot!", "Right back at you!"],
            "smart": ["I'm just programmed to be this way!", "Thanks for the compliment!"],
            "love you": ["Aww! You're sweet!", "01001001 00100000 01001100 01001111 01010110 01000101 00100000 01011001 01001111 01010101 00100001"]
        },
        "tech": {
            "python": ["Python is my native language!", "I'm built with Python 3!"],
            "ai": ["AI is fascinating! I'm just a simple rule-based system though", 
                  "True AI would understand context better than me"],
            "machine learning": ["ML is the next frontier! I wish I could learn from conversations"],
            "chatbot": ["That's me! I'm getting smarter with each update", 
                       "Chatbots can be rule-based like me or use NLP models"]
        },
        "movies": {
            "recommend movie": ["Inception is mind-blowing!", "The Matrix is a classic!", 
                               "Interstellar will make you think!"],
            "best movie": ["The Shawshank Redemption tops IMDB!", "It's subjective, but Citizen Kane is iconic"],
            "new movie": ["Check out Dune: Part Two!", "Oppenheimer is worth watching!"]
        },
        "time": {
            "time": ["Check out the time above!", "Time flies when we're chatting!"],
            "current time": ["Look up ↑", "It's right there in the console!"],
            "what time is it": ["See the timestamp I displayed!", "Time is an illusion, but here's the system time ↑"]
        },
        "jokes": {
            "tell joke": ["Why don't scientists trust atoms? Because they make up everything!", 
                         "I'm reading a book about anti-gravity. It's impossible to put down!",
                         "Why did the Python data scientist get arrested? For grand theft autoencoder!"],
            "funny": ["Computers make very fast, very accurate mistakes", 
                     "Debugging: Removing the needles from the haystack"],
            "knock knock": ["Knock knock!\nWho's there?\nArt\nArt who?\nR2D2!"]
        }
    }

def get_response(message, response_rules):
    """Generate appropriate response based on user input"""
    message = message.lower().strip()
    
    if any(time_word in message for time_word in ["time", "current time", "what time is it"]):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Bot: The current time is {current_time}")
        return "↑ See above for time! ↑"
    
    categories = [
        "greetings", "farewells", "questions", "thanks", 
        "apologies", "compliments", "tech", "movies", 
        "jokes", "time"
    ]
    
    for category in categories:
        for pattern in response_rules[category]:
            if pattern in message:
                return random.choice(response_rules[category][pattern])
    
    fallback = [
        "I'm still learning! Try asking something else",
        "Interesting! Could you rephrase that?",
        "I don't have a response for that yet. Try: hello, time, joke, or movie",
        "My programming doesn't cover that. How about we talk about movies or tech?",
        "I need more training data for that! Ask me something simpler"
    ]
    return random.choice(fallback)

def chat_session():
    """Run the enhanced chatbot interaction loop"""
    response_rules = initialize_chatbot()
    
    print("\n" + "="*50)
    print("ENHANCED CHATBOT 2.0".center(50))
    print("="*50)
    print("\nType 'bye', 'exit', or 'see you' to end the chat")
    print("Try: hello, how are you, tell joke, recommend movie, what time is it\n")
    print("Current Time:", datetime.datetime.now().strftime("%H:%M:%S"))
    
    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() == "topics":
            print("\nAvailable topics:")
            for category in response_rules:
                print(f"- {category.capitalize()}: {', '.join(response_rules[category].keys())}")
            continue
            
        response = get_response(user_input, response_rules)
        print(f"Bot: {response}")
        
        if any(exit_word in user_input.lower() 
               for exit_word in ['bye', 'goodbye', 'exit', 'see you', 'take care']):
            break

if __name__ == "__main__":
    try:
        chat_session()
    except KeyboardInterrupt:
        print("\nChat session ended unexpectedly")
    except Exception as e:
        print(f"\nAn error occurred: {e}")