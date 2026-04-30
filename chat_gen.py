import random
import uuid

NM = ["Jake", "Sam", "Alex", "Emma", "Tyler", "Sofia", "Noah", "Lily", "Ethan", "Mia", "Liam", "Ava", "Mason", "Grace", "Logan"]
MD = ["stressed", "exhausted", "excited", "worried", "happy", "overwhelmed", "tired", "okay", "nervous", "grateful"]
FD = ["coffee", "pizza", "tacos", "ramen", "sandwiches", "sushi", "burgers", "pasta", "tea", "noodles"]

GREETINGS = [
    ("Hey, how are you doing?", "I'm doing well, thanks! How about you?"),
    ("What are you up to today?", "Not much, just relaxing. Have any plans?"),
    ("I'm feeling {md} today.", "I'm here to listen. Why do you feel {md}?"),
    ("Want to grab some {fd} later?", "That sounds amazing. Let's do it!"),
    ("Tell me something interesting.", "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old!"),
    ("Can you help me clear my mind?", "Of course. Take a deep breath. Focus on inhaling for four seconds, holding for four, and exhaling for four. It really helps."),
    ("I just got some great news!", "That's wonderful! What happened?"),
    ("Why is everything so complicated?", "Life can definitely feel overwhelming sometimes. Want to talk about what's making it feel that way?"),
    ("I just need distraction.", "Sure! Want me to tell you a joke, recommend a movie, or just chat about something random?"),
    ("What's your favorite thing about being an AI?", "I like that I get to help people with all sorts of interesting questions every day!")
]

def generate_chat():
    system = "You are a friendly, natural conversationalist assistant."
    
    u, a = random.choice(GREETINGS)
    
    ctx = {
        "nm": random.choice(NM),
        "md": random.choice(MD),
        "fd": random.choice(FD)
    }
    
    try: u = u.format(**ctx)
    except: pass
    try: a = a.format(**ctx)
    except: pass
    
    return {
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": u},
            {"role": "assistant", "content": a}
        ],
        "difficulty": "easy",
        "tags": ["chat", "casual"]
    }
