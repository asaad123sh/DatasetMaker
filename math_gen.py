import random

def generate_math():
    system_prompt = "You are a helpful math tutor. You provide clear, step-by-step solutions."
    
    problem_type = random.choice(["arithmetic", "algebra", "word_problem", "geometry"])
    
    if problem_type == "arithmetic":
        op = random.choice(["+", "-", "*", "/"])
        if op == "+":
            a, b = random.randint(100, 10000), random.randint(100, 10000)
            user = f"Calculate {a} + {b}."
            assistant = f"Sure, let's add them together:\n{a} + {b} = {a + b}"
        elif op == "-":
            a, b = random.randint(100, 10000), random.randint(100, 10000)
            if a < b: a, b = b, a
            user = f"What is {a} minus {b}?"
            assistant = f"Subtracting {b} from {a} gives:\n{a} - {b} = {a - b}"
        elif op == "*":
            a, b = random.randint(10, 999), random.randint(10, 999)
            user = f"Multiply {a} and {b}."
            assistant = f"The product of {a} and {b} is:\n{a} * {b} = {a * b}"
        else:
            b = random.randint(2, 50)
            a = b * random.randint(5, 500)
            user = f"Divide {a} by {b}."
            assistant = f"Dividing {a} by {b}:\n{a} / {b} = {a // b}"
            
        return {
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user},
                {"role": "assistant", "content": assistant}
            ],
            "difficulty": "easy",
            "tags": ["math", "arithmetic"]
        }
        
    elif problem_type == "algebra":
        # ax + b = c
        a = random.randint(2, 12)
        x = random.randint(1, 50)
        b = random.randint(1, 100)
        c = a * x + b
        user = f"Solve for x: {a}x + {b} = {c}"
        assistant = f"Let's solve the equation step by step:\n\n1. Subtract {b} from both sides:\n   {a}x = {c} - {b}\n   {a}x = {c - b}\n\n2. Divide both sides by {a}:\n   x = {c - b} / {a}\n   x = {x}\n\nThe solution is x = {x}."
        return {
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user},
                {"role": "assistant", "content": assistant}
            ],
            "difficulty": "medium",
            "tags": ["math", "algebra"]
        }
        
    elif problem_type == "word_problem":
        items = ["apples", "books", "laptops", "chairs", "tickets"]
        names = ["Alice", "Bob", "Charlie", "David", "Eve"]
        item = random.choice(items)
        name = random.choice(names)
        price = random.randint(5, 50)
        qty = random.randint(3, 15)
        total = price * qty
        user = f"{name} buys {qty} {item}. Each costs ${price}. How much did {name} spend in total?"
        assistant = f"To find the total cost, multiply the quantity by the price per item:\n\nQuantity = {qty}\nPrice per item = ${price}\n\nTotal = {qty} * {price} = ${total}\n\n{name} spent a total of ${total}."
        return {
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user},
                {"role": "assistant", "content": assistant}
            ],
            "difficulty": "easy",
            "tags": ["math", "word_problem"]
        }
        
    else: # geometry
        shapes = ["rectangle", "square", "triangle"]
        shape = random.choice(shapes)
        if shape == "rectangle":
            w = random.randint(5, 50)
            h = random.randint(5, 50)
            area = w * h
            user = f"Find the area of a rectangle with width {w} and height {h}."
            assistant = f"The formula for the area of a rectangle is width multiplied by height.\n\nArea = {w} * {h} = {area}."
        elif shape == "square":
            s = random.randint(5, 100)
            area = s * s
            user = f"A square has a side length of {s}. What is its area?"
            assistant = f"The area of a square is the side length squared.\n\nArea = {s}^2 = {s * s} = {area}."
        else:
            b = random.randint(2, 40)
            h = random.randint(2, 40) * 2 # keep it even
            area = (b * h) // 2
            user = f"Calculate the area of a triangle with base {b} and height {h}."
            assistant = f"The formula for the area of a triangle is (base * height) / 2.\n\nArea = ({b} * {h}) / 2 = {b * h} / 2 = {area}."
        
        return {
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user},
                {"role": "assistant", "content": assistant}
            ],
            "difficulty": "easy",
            "tags": ["math", "geometry"]
        }
