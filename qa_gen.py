import random

QA_PAIRS = [
    ("What is the capital of France?", "The capital of France is Paris."),
    ("Who wrote 'Romeo and Juliet'?", "William Shakespeare wrote 'Romeo and Juliet'."),
    ("What is the largest species of shark?", "The largest species of shark is the whale shark."),
    ("What is the boiling point of water in Celsius?", "Water boils at 100 degrees Celsius under standard atmospheric pressure."),
    ("How many continents are there?", "There are seven continents: Africa, Antarctica, Asia, Australia, Europe, North America, and South America."),
    ("Which planet is closest to the Sun?", "Mercury is the closest planet to the Sun."),
    ("What gas do plants absorb from the atmosphere?", "Plants absorb carbon dioxide from the atmosphere during photosynthesis."),
    ("Who painted the Mona Lisa?", "Leonardo da Vinci painted the Mona Lisa."),
    ("What is the hardest natural substance on Earth?", "Diamond is the hardest naturally occurring substance on Earth."),
    ("In what year did the Titanic sink?", "The RMS Titanic sank in 1912."),
    ("What is the chemical symbol for gold?", "The chemical symbol for gold is Au."),
    ("What is the speed of light?", "The speed of light in a vacuum is approximately 299,792 kilometers per second (or about 186,282 miles per second)."),
    ("Who was the first person to walk on the moon?", "Neil Armstrong was the first person to walk on the moon in 1969."),
    ("What is the main ingredient in guacamole?", "The main ingredient in guacamole is avocado.")
]

SYSTEM_PROMPTS = [
    "You are a helpful and highly knowledgeable AI assistant.",
    "You are a concise trivia expert.",
    "Answer the user's questions accurately and directly.",
    "You are an encyclopedic AI that provides factual answers."
]

def generate_qa():
    prompt = random.choice(SYSTEM_PROMPTS)
    q, a = random.choice(QA_PAIRS)
    
    return {
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": q},
            {"role": "assistant", "content": a}
        ],
        "difficulty": "easy",
        "tags": ["qa", "general_knowledge"]
    }
