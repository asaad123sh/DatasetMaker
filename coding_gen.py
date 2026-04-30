import random

SYSTEM_PROMPTS = [
    "You are an expert software engineer assistant.",
    "You are a coding tutor. Provide clear and concise code.",
    "You are a senior developer helping a junior. Offer clean solutions."
]

CODING_TASKS = [
    (
        "Write a python function to reverse a string.",
        "Sure! You can reverse a string in Python using slicing:\n\n```python\ndef reverse_string(s):\n    return s[::-1]\n```"
    ),
    (
        "How do I sort a list of dictionaries by a specific key in Python?",
        "You can use the `sorted()` function or the `.sort()` method with a lambda function as the key.\n\n```python\nmy_list = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]\nsorted_list = sorted(my_list, key=lambda x: x['age'])\n```"
    ),
    (
        "What is the difference between let and const in JavaScript?",
        "`const` is used to declare variables whose bindings cannot be reassigned. `let` is used to declare variables that can be reassigned later. Both are block-scoped."
    ),
    (
        "Write a basic Express server in Node.js.",
        "Here is a minimal Express server:\n\n```javascript\nconst express = require('express');\nconst app = express();\n\napp.get('/', (req, res) => {\n  res.send('Hello World!');\n});\n\napp.listen(3000, () => {\n  console.log('Server is running on port 3000');\n});\n```"
    ),
    (
        "What does CSS stand for?",
        "CSS stands for Cascading Style Sheets. It is used to style and layout web pages."
    ),
    (
        "Explain what a Promise is in JavaScript.",
        "A Promise in JavaScript is an object representing the eventual completion or failure of an asynchronous operation. It can be in one of three states: pending, fulfilled, or rejected."
    )
]

def generate_coding():
    system = random.choice(SYSTEM_PROMPTS)
    u, a = random.choice(CODING_TASKS)
    
    return {
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": u},
            {"role": "assistant", "content": a}
        ],
        "difficulty": random.choice(["easy", "medium"]),
        "tags": ["coding", "programming"]
    }
