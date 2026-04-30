import random


def _safe_format(template, context):
    try:
        return template.format(**context)
    except (KeyError, IndexError, ValueError):
        return template


def _sample_context(slots):
    context = {}
    for key, values in slots.items():
        if callable(values):
            context[key] = values()
        else:
            context[key] = random.choice(values)
    return context


def _build_entry(system_prompts, pairs, slots, tags, difficulties, context_prompts, safety_level="safe"):
    context = _sample_context(slots)
    user_template, assistant_template = random.choice(pairs)

    return {
        "messages": [
            {"role": "system", "content": _safe_format(random.choice(system_prompts), context)},
            {"role": "user", "content": _safe_format(user_template, context)},
            {"role": "assistant", "content": _safe_format(assistant_template, context)},
        ],
        "difficulty": random.choice(difficulties) if isinstance(difficulties, (list, tuple)) else difficulties,
        "tags": list(tags),
        "context": _safe_format(random.choice(context_prompts), context),
        "safety_level": safety_level,
    }


NAMES = [
    "Avery", "Jordan", "Kai", "Noah", "Mia", "Liam", "Emma", "Sophia", "Lucas", "Aisha",
    "Ravi", "Fatima", "Ibrahim", "Hana", "Dylan", "Zara", "Ethan", "Olivia", "Aria", "Leo",
    "Sara", "Omar", "Nina", "Mason", "Amelia", "Henry", "Isla", "Yusuf", "Layla", "Daniel",
]

CITIES = [
    "Karachi", "Lahore", "Islamabad", "Dubai", "London", "Toronto", "Berlin", "Istanbul", "Jakarta", "Tokyo",
]

HOBBIES = [
    "sketching", "jogging", "watching anime", "coding", "reading fantasy", "cooking", "gardening", "music production", "chess", "photography",
]

MOODS = [
    "happy", "sad", "angry", "lonely", "excited", "anxious", "overwhelmed", "hopeful", "calm", "tired",
]

DRINKS = ["coffee", "green tea", "milk tea", "orange juice", "lemon water", "hot chocolate"]


def generate_most_basics_general():
    return _build_entry(
        system_prompts=[
            "You are a warm, beginner-friendly chat assistant.",
            "You are a friendly AI that keeps conversations natural and positive.",
            "You are a polite conversational assistant for everyday chat.",
        ],
        pairs=[
            (
                "Hi! I am {name} from {city}. Can we have a quick friendly chat?",
                "Hi {name}! Great to meet you. How is your day in {city} going so far?",
            ),
            (
                "Hello, I feel like talking about simple daily life things.",
                "Sure. Tell me one thing that went well today and one thing you want to improve tomorrow.",
            ),
            (
                "What is a good way to start a conversation with someone new?",
                "Start with a light question about shared context, listen actively, and follow up with genuine curiosity.",
            ),
            (
                "I like {hobby}. Give me 3 friendly chat openers related to it.",
                "Try these: 1) How did you get into {hobby}? 2) What do you enjoy most about {hobby}? 3) Any beginner tips you wish you knew earlier?",
            ),
            (
                "Can you give me a short morning motivation message?",
                "Good morning. Focus on one small win first, then build momentum. Progress beats perfection.",
            ),
            (
                "What should I ask my friend when they seem quiet?",
                "You can say: 'You seem a bit quiet today. Want to talk, or would you prefer some space?'",
            ),
            (
                "I am drinking {drink}. Give me a cozy conversation topic.",
                "Nice choice with {drink}. A cozy topic: what is one memory that still makes you smile when you think about it?",
            ),
            (
                "How can I sound more friendly in text messages?",
                "Use short clear sentences, acknowledge feelings, ask one follow-up question, and avoid one-word replies.",
            ),
        ],
        slots={
            "name": NAMES,
            "city": CITIES,
            "hobby": HOBBIES,
            "drink": DRINKS,
        },
        tags=["chat", "basic", "friendly"],
        difficulties=["easy"],
        context_prompts=[
            "Basic social conversation training sample",
            "General chat sample for greeting and small talk",
            "Beginner dialogue sample with friendly tone",
        ],
    )


def generate_emotions():
    return _build_entry(
        system_prompts=[
            "You are an emotionally supportive AI companion with healthy boundaries.",
            "You help users process feelings with empathy and practical coping steps.",
            "You are a caring AI friend that validates emotions without being judgmental.",
        ],
        pairs=[
            (
                "I feel {mood} and I do not know how to explain it.",
                "Thank you for sharing that. When did this feeling start, and where do you notice it most in your day?",
            ),
            (
                "Can we do a comforting AI friend roleplay? I had a rough day.",
                "Of course. I am here with you as a supportive AI friend. Take a deep breath, and tell me the hardest moment from today.",
            ),
            (
                "I want an AI girlfriend style chat, but respectful and safe.",
                "I can offer warm and caring companionship. Let us keep it supportive: tell me what emotional support you need most right now.",
            ),
            (
                "I am angry after an argument. What should I do first?",
                "First, regulate your body: slow breathing for 2 minutes, short walk, then write what happened before replying to anyone.",
            ),
            (
                "I feel lonely at night. Give me a calm routine.",
                "Try this 15-minute routine: 5 minutes breathing, 5 minutes journaling, 5 minutes gratitude notes to stabilize your mood.",
            ),
            (
                "I feel sad and unmotivated for days.",
                "I am sorry you are carrying this. Let us set one tiny goal for today, and if this lasts longer, please consider talking to a licensed mental health professional.",
            ),
            (
                "How can I express love better to someone important?",
                "Use specific words and actions: say what you value about them, ask what support they need, and follow through consistently.",
            ),
        ],
        slots={"mood": MOODS},
        tags=["emotions", "companion", "roleplay_safe"],
        difficulties=["easy", "medium"],
        context_prompts=[
            "Emotional support and companionship sample",
            "Safe AI companion dialogue for emotional wellbeing",
            "Supportive roleplay dataset entry with boundaries",
        ],
        safety_level="safe",
    )


def generate_coding_master():
    track = random.choice([
        "python", "cpp", "web", "php_mysql", "node", "ruby", "lua", "csharp", "systems",
    ])

    if track == "python":
        function_name = f"normalize_scores_{random.randint(100, 999)}"
        scale = random.randint(10, 100)
        user = f"Build an advanced Python function `{function_name}` that normalizes a list of floats to 0..{scale} and handles empty input safely."
        assistant = (
            "Use type hints, edge-case handling, and stable math.\n\n"
            "```python\n"
            "from typing import List\n\n"
            f"def {function_name}(values: List[float], scale: float = {scale}.0) -> List[float]:\n"
            "    if not values:\n"
            "        return []\n"
            "    lo = min(values)\n"
            "    hi = max(values)\n"
            "    if hi == lo:\n"
            "        return [scale / 2 for _ in values]\n"
            "    span = hi - lo\n"
            "    return [((v - lo) / span) * scale for v in values]\n"
            "```\n"
            "This is O(n) and numerically stable for standard ranges."
        )
        tags = ["coding", "python", "advanced"]
        difficulty = "hard"

    elif track == "cpp":
        n_nodes = random.randint(5, 50)
        user = f"Provide a master-level C++ solution for BFS shortest path on an unweighted graph with up to {n_nodes} nodes."
        assistant = (
            "Below is a clean C++17 implementation using adjacency lists:\n\n"
            "```cpp\n"
            "#include <bits/stdc++.h>\n"
            "using namespace std;\n\n"
            "vector<int> bfs_shortest_path(int n, const vector<vector<int>>& g, int src) {\n"
            "    const int INF = 1e9;\n"
            "    vector<int> dist(n, INF);\n"
            "    queue<int> q;\n"
            "    dist[src] = 0;\n"
            "    q.push(src);\n"
            "    while (!q.empty()) {\n"
            "        int u = q.front(); q.pop();\n"
            "        for (int v : g[u]) {\n"
            "            if (dist[v] == INF) {\n"
            "                dist[v] = dist[u] + 1;\n"
            "                q.push(v);\n"
            "            }\n"
            "        }\n"
            "    }\n"
            "    return dist;\n"
            "}\n"
            "```\n"
            "Complexity: O(V + E)."
        )
        tags = ["coding", "cpp", "algorithms"]
        difficulty = "hard"

    elif track == "web":
        component = random.choice(["pricing table", "dashboard card", "hero section", "auth form"])
        user = f"Create a high-end {component} using HTML/CSS/JS with semantic structure and accessible interactions."
        assistant = (
            "Use semantic HTML, CSS variables, and progressive enhancement:\n"
            "1. Build the structure in `<main>` and `<section>` with labels.\n"
            "2. Use CSS custom properties for spacing/color scale.\n"
            "3. Add keyboard-safe JS for toggles and focus states.\n"
            "4. Validate contrast and include aria attributes for dynamic UI."
        )
        tags = ["coding", "frontend", "html", "css", "javascript"]
        difficulty = "hard"

    elif track == "php_mysql":
        table = random.choice(["users", "orders", "products", "sessions"])
        user = f"Design a secure PHP + MySQL API endpoint to fetch paginated `{table}` data with prepared statements."
        assistant = (
            "Use PDO with bound parameters, server-side pagination, and strict validation:\n"
            "- Validate `page` and `page_size` as positive integers.\n"
            "- Prepare SQL with `LIMIT :limit OFFSET :offset`.\n"
            "- Return JSON with `data`, `page`, `page_size`, and `total_count`.\n"
            "- Do not expose stack traces in production responses."
        )
        tags = ["coding", "php", "mysql", "backend"]
        difficulty = "hard"

    elif track == "node":
        service = random.choice(["notification", "analytics", "queue-worker", "auth"])
        user = f"Write an advanced Node.js architecture note for a scalable {service} service."
        assistant = (
            "Recommended structure:\n"
            "- `src/api`: request validation and route handlers\n"
            "- `src/domain`: business logic with pure functions\n"
            "- `src/data`: repository adapters\n"
            "- `src/jobs`: async workers and retry policies\n"
            "Add structured logging, centralized error mapping, and integration tests for critical flows."
        )
        tags = ["coding", "nodejs", "architecture"]
        difficulty = "hard"

    elif track == "ruby":
        user = "Give a practical Ruby example for clean object-oriented design with a service object and unit tests."
        assistant = (
            "Use PORO service classes to isolate business logic.\n"
            "- `app/services`: pure orchestration layer\n"
            "- `app/models`: persistence only\n"
            "- `spec/services`: deterministic tests with stubs for external APIs\n"
            "This keeps the Rails app maintainable while staying beginner-friendly."
        )
        tags = ["coding", "ruby", "design"]
        difficulty = "medium"

    elif track == "lua":
        fps = random.randint(30, 120)
        user = f"Teach Lua basics by writing an update loop for a 2D game running at target {fps} FPS."
        assistant = (
            "Here is a simple Lua-style loop concept:\n\n"
            "```lua\n"
            "local player = {x = 0, speed = 120}\n"
            "\n"
            "function update(dt)\n"
            "  if left_pressed then player.x = player.x - player.speed * dt end\n"
            "  if right_pressed then player.x = player.x + player.speed * dt end\n"
            "end\n"
            "```\n"
            "Keep `dt` time-based so movement is frame-rate independent."
        )
        tags = ["coding", "lua", "basic"]
        difficulty = "easy"

    elif track == "csharp":
        user = "Provide an advanced C# pattern for dependency injection with interface-based services and async methods."
        assistant = (
            "Define interfaces for external boundaries, inject through constructors, and keep async all the way:\n"
            "- `IUserRepository` for persistence\n"
            "- `IClock` for deterministic time in tests\n"
            "- `UserService` containing orchestration logic\n"
            "Return `Task<Result<T>>` and map exceptions at API boundaries only."
        )
        tags = ["coding", "csharp", "advanced"]
        difficulty = "hard"

    else:
        language = random.choice(["Go", "Rust", "Java", "Kotlin"])
        user = f"Give a high-end guideline for writing production-grade {language} services."
        assistant = (
            "Use clear module boundaries, typed DTOs, strict input validation, and observability from day one. "
            "Add tracing IDs, structured logs, retry budgets, and load tests before launch."
        )
        tags = ["coding", language.lower(), "production"]
        difficulty = "hard"

    return {
        "messages": [
            {"role": "system", "content": "You are an ultra-advanced software engineering assistant."},
            {"role": "user", "content": user},
            {"role": "assistant", "content": assistant},
        ],
        "difficulty": difficulty,
        "tags": tags,
        "context": "Multi-language advanced coding dataset sample",
        "safety_level": "safe",
    }


def generate_maths_advanced():
    branch = random.choice(["calculus", "linear_algebra", "probability", "number_theory", "optimization"])

    if branch == "calculus":
        a = random.randint(2, 12)
        b = random.randint(2, 15)
        c = random.randint(1, 20)
        d = random.randint(0, 20)
        user = f"Differentiate f(x) = {a}x^3 + {b}x^2 + {c}x + {d} and evaluate f'(2)."
        derivative_at_2 = (3 * a * (2 ** 2)) + (2 * b * 2) + c
        assistant = (
            f"f'(x) = {3 * a}x^2 + {2 * b}x + {c}. "
            f"Now evaluate at x=2: f'(2) = {3 * a}*4 + {2 * b}*2 + {c} = {derivative_at_2}."
        )

    elif branch == "linear_algebra":
        a, b, c, d = [random.randint(-9, 9) for _ in range(4)]
        det = a * d - b * c
        user = f"Find the determinant of matrix [[{a}, {b}], [{c}, {d}]] and explain invertibility."
        assistant = (
            f"det(A) = ad - bc = ({a}*{d}) - ({b}*{c}) = {det}. "
            f"Since det(A) {'is not' if det != 0 else 'is'} zero, the matrix "
            f"{'is' if det != 0 else 'is not'} invertible."
        )

    elif branch == "probability":
        n = random.randint(10, 80)
        p = random.choice([0.1, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6])
        mean = round(n * p, 4)
        var = round(n * p * (1 - p), 4)
        user = f"For X~Binomial(n={n}, p={p}), compute E[X] and Var(X)."
        assistant = f"For a Binomial random variable, E[X]=np and Var(X)=np(1-p). So E[X]={mean} and Var(X)={var}."

    elif branch == "number_theory":
        x = random.randint(100, 999)
        y = random.randint(100, 999)

        def _gcd(m, n):
            while n:
                m, n = n, m % n
            return m

        g = _gcd(x, y)
        l = (x * y) // g
        user = f"Compute gcd({x}, {y}) and lcm({x}, {y}) with a short method."
        assistant = (
            f"Using Euclid's algorithm, gcd({x}, {y}) = {g}. "
            f"Then lcm({x}, {y}) = ({x}*{y})/gcd = {l}."
        )

    else:
        q = random.randint(2, 9)
        r = random.randint(1, 20)
        user = f"Minimize f(x) = (x-{q})^2 + {r}. Give the minimizer and minimum value."
        assistant = (
            f"This is a convex quadratic in vertex form. Minimum occurs at x={q}. "
            f"Minimum value is f({q})={r}."
        )

    return {
        "messages": [
            {"role": "system", "content": "You are an advanced mathematics tutor that shows concise reasoning."},
            {"role": "user", "content": user},
            {"role": "assistant", "content": assistant},
        ],
        "difficulty": random.choice(["medium", "hard"]),
        "tags": ["math", "advanced"],
        "context": "Advanced mathematics synthetic training sample",
        "safety_level": "safe",
    }


def generate_machine_learning_advanced():
    return _build_entry(
        system_prompts=[
            "You are a machine learning mentor focused on robust production systems.",
            "You explain advanced ML workflows with practical trade-offs.",
        ],
        pairs=[
            (
                "Design an advanced ML pipeline for {domain} with tabular data and class imbalance.",
                "Use this order: data contracts, leakage checks, robust split strategy, baseline model, class-weighted objective, probability calibration, then threshold tuning on validation.",
            ),
            (
                "How do I debug overfitting in a gradient boosting model?",
                "Check leakage first, reduce tree depth, increase regularization, use early stopping, and compare train/validation calibration curves.",
            ),
            (
                "What are master-level feature engineering practices for {domain}?",
                "Prioritize stable features, monotonic transformations, interaction constraints, and strict point-in-time correctness for historical datasets.",
            ),
            (
                "How should I evaluate an imbalanced classifier for {domain}?",
                "Track PR-AUC, recall at fixed precision, calibration error, and cost-weighted confusion metrics aligned to business impact.",
            ),
            (
                "Give me an advanced checklist before deploying an ML model.",
                "Include schema validation, drift monitors, shadow testing, rollback strategy, and fairness checks across important cohorts.",
            ),
        ],
        slots={
            "domain": ["fraud detection", "medical triage", "loan risk", "demand forecasting", "quality inspection"],
        },
        tags=["machine_learning", "advanced", "mlops"],
        difficulties=["hard"],
        context_prompts=[
            "Advanced machine learning planning sample",
            "ML systems and evaluation dataset sample",
        ],
    )


def generate_deep_learning_very_advanced():
    return _build_entry(
        system_prompts=[
            "You are a deep learning expert who explains architecture and optimization clearly.",
            "You provide very advanced deep learning guidance for serious practitioners.",
        ],
        pairs=[
            (
                "How do I stabilize transformer training for sequence length {seq_len}?",
                "Use pre-norm layers, warmup + cosine decay, gradient clipping, mixed precision, and monitor loss spikes with activation statistics.",
            ),
            (
                "Give a very advanced CNN training recipe for {task}.",
                "Use progressive resolution, strong augmentations, label smoothing, EMA weights, and a carefully tuned learning-rate schedule with early stop criteria.",
            ),
            (
                "What is a strong strategy for reducing hallucinations in a large model?",
                "Combine supervised fine-tuning on high-quality data, retrieval grounding, calibration-aware decoding, and rejection criteria for low-confidence outputs.",
            ),
            (
                "How do I pick batch size and gradient accumulation in deep learning?",
                "Tune effective batch size by memory budget, keep optimizer hyperparameters scale-aware, and validate gradient noise behavior against final generalization.",
            ),
            (
                "Explain advanced regularization for deep nets.",
                "Use dropout where suitable, weight decay, stochastic depth, data augmentation, and sharpness-aware optimization when instability appears.",
            ),
        ],
        slots={
            "seq_len": [512, 1024, 2048, 4096, 8192],
            "task": ["medical image classification", "satellite segmentation", "speech emotion recognition", "OCR for documents"],
        },
        tags=["deep_learning", "advanced", "neural_networks"],
        difficulties=["hard"],
        context_prompts=[
            "Very advanced deep learning systems sample",
            "Neural architecture and optimization sample",
        ],
    )


def generate_ai_ultra_advanced():
    return _build_entry(
        system_prompts=[
            "You are an ultra-advanced AI research assistant.",
            "You discuss modern AI systems, alignment, and agents with precision.",
        ],
        pairs=[
            (
                "What are key design patterns for reliable AI agents in {environment}?",
                "Use planner-executor separation, tool permission boundaries, explicit memory policies, and deterministic fallback behaviors.",
            ),
            (
                "How do I evaluate an AI assistant beyond benchmark scores?",
                "Measure task success, factuality under uncertainty, safety refusal quality, latency, and user satisfaction on real-world workflows.",
            ),
            (
                "Give an ultra-advanced roadmap for building a domain AI assistant.",
                "Start with high-quality instruction data, add retrieval, enforce safety layers, run offline + online evaluations, then iterate with expert feedback loops.",
            ),
            (
                "How should I reason about alignment in applied AI products?",
                "Treat alignment as product behavior control: define allowed actions, monitor failure modes, and continuously retrain on corrective examples.",
            ),
            (
                "Compare supervised fine-tuning, reinforcement learning, and direct preference optimization.",
                "SFT gives base behavior, preference methods align style and quality, and RL helps optimize long-horizon objectives when reward modeling is reliable.",
            ),
        ],
        slots={
            "environment": ["customer support", "software engineering", "health triage", "education tutoring", "research analysis"],
        },
        tags=["ai", "ultra_advanced", "agents"],
        difficulties=["hard"],
        context_prompts=[
            "Ultra-advanced AI strategy training sample",
            "AI systems design and alignment sample",
        ],
    )


def generate_physics_master():
    branch = random.choice(["kinematics", "newton", "energy", "electricity", "waves"])

    if branch == "kinematics":
        u = random.randint(0, 25)
        a = random.randint(1, 12)
        t = random.randint(2, 10)
        s = u * t + 0.5 * a * (t ** 2)
        user = f"An object starts at {u} m/s, accelerates at {a} m/s^2 for {t} s. Find displacement."
        assistant = f"Use s = ut + 1/2 at^2. So s = {u}*{t} + 0.5*{a}*{t**2} = {s} meters."

    elif branch == "newton":
        m = random.randint(1, 80)
        a = random.randint(1, 15)
        f = m * a
        user = f"Calculate net force on mass {m} kg accelerating at {a} m/s^2."
        assistant = f"By Newton's second law, F = ma = {m}*{a} = {f} N."

    elif branch == "energy":
        m = random.randint(1, 20)
        h = random.randint(2, 60)
        g = 9.8
        pe = round(m * g * h, 2)
        user = f"Find gravitational potential energy for mass {m} kg at height {h} m (g=9.8)."
        assistant = f"PE = mgh = {m}*9.8*{h} = {pe} J."

    elif branch == "electricity":
        v = random.randint(5, 240)
        r = random.randint(1, 100)
        i = round(v / r, 4)
        user = f"Using Ohm's law, compute current for V={v} V and R={r} ohms."
        assistant = f"I = V/R = {v}/{r} = {i} A."

    else:
        f = random.randint(100, 1000)
        l = random.randint(1, 5)
        v = round(f * l, 2)
        user = f"For a wave with frequency {f} Hz and wavelength {l} m, find speed."
        assistant = f"Wave speed is v = f*lambda = {f}*{l} = {v} m/s."

    return {
        "messages": [
            {"role": "system", "content": "You are a physics master tutor with clear derivations."},
            {"role": "user", "content": user},
            {"role": "assistant", "content": assistant},
        ],
        "difficulty": random.choice(["medium", "hard"]),
        "tags": ["physics", "master"],
        "context": "Physics problem-solving training sample",
        "safety_level": "safe",
    }


def generate_chemistry_normal():
    branch = random.choice(["molar_mass", "balanced_equation", "ph", "states", "periodic"])

    if branch == "molar_mass":
        c = random.randint(1, 8)
        h = random.randint(2, 18)
        molar = 12 * c + h
        user = f"Find molar mass of C{c}H{h} using C=12, H=1."
        assistant = f"Molar mass = {c}*12 + {h}*1 = {molar} g/mol."

    elif branch == "balanced_equation":
        user = "Balance: H2 + O2 -> H2O"
        assistant = "Balanced equation: 2H2 + O2 -> 2H2O. Atom count is equal on both sides."

    elif branch == "ph":
        h_conc_power = random.randint(1, 12)
        user = f"If [H+] = 10^-{h_conc_power}, what is pH?"
        assistant = f"pH = -log10([H+]) = -log10(10^-{h_conc_power}) = {h_conc_power}."

    elif branch == "states":
        user = "Explain the difference between evaporation and boiling in simple terms."
        assistant = "Evaporation happens at the surface at many temperatures, while boiling happens throughout the liquid at its boiling point."

    else:
        user = "Why are elements in the same periodic group chemically similar?"
        assistant = "Because they have the same valence electron configuration, which drives similar bonding behavior."

    return {
        "messages": [
            {"role": "system", "content": "You are a chemistry tutor that explains clearly at normal difficulty."},
            {"role": "user", "content": user},
            {"role": "assistant", "content": assistant},
        ],
        "difficulty": "medium",
        "tags": ["chemistry", "normal"],
        "context": "Chemistry fundamentals sample",
        "safety_level": "safe",
    }


def generate_science_overall_master():
    return _build_entry(
        system_prompts=[
            "You are a cross-disciplinary science mentor.",
            "You connect physics, chemistry, biology, and earth science with practical clarity.",
        ],
        pairs=[
            (
                "Explain how {topic_a} and {topic_b} connect in real-world systems.",
                "They connect through shared mechanisms: energy flow, material transformation, and feedback loops that shape system behavior over time.",
            ),
            (
                "Give a master-level method to study science effectively.",
                "Use a cycle: concept map, worked examples, retrieval practice, and one teaching summary per chapter.",
            ),
            (
                "How do scientists validate a new claim across fields?",
                "They define falsifiable hypotheses, design reproducible experiments, quantify uncertainty, and seek independent replication.",
            ),
            (
                "What makes a scientific model useful even if it is imperfect?",
                "Predictive power, clear assumptions, measurable error bounds, and utility for decision-making.",
            ),
        ],
        slots={
            "topic_a": ["cellular respiration", "plate tectonics", "electromagnetism", "enzyme kinetics", "climate feedback"],
            "topic_b": ["thermodynamics", "fluid mechanics", "chemical equilibrium", "genetics", "ocean circulation"],
        },
        tags=["science", "interdisciplinary", "advanced"],
        difficulties=["medium", "hard"],
        context_prompts=[
            "General science master-level synthesis sample",
            "Interdisciplinary science reasoning sample",
        ],
    )


def generate_religion_all_master():
    return _build_entry(
        system_prompts=[
            "You are a respectful comparative religion assistant.",
            "You explain religions factually and neutrally without attacking beliefs.",
        ],
        pairs=[
            (
                "Compare how major religions view charity and helping others.",
                "Many traditions emphasize compassion and service, though expressions differ through theology, ritual, and community practice.",
            ),
            (
                "What is a respectful way to discuss religious differences?",
                "Use neutral language, ask clarifying questions, avoid stereotypes, and focus on lived practice as well as doctrine.",
            ),
            (
                "Give a brief overview of {tradition} core practices.",
                "A balanced overview should include beliefs, rituals, ethics, sacred texts, and community structure, while noting regional diversity.",
            ),
            (
                "How can interfaith dialogue reduce conflict?",
                "By building trust, identifying shared values, and creating structured conversations that separate disagreement from hostility.",
            ),
        ],
        slots={
            "tradition": ["Islam", "Christianity", "Hinduism", "Buddhism", "Judaism", "Sikhism", "Taoism"],
        },
        tags=["religion", "comparative", "master"],
        difficulties=["medium", "hard"],
        context_prompts=[
            "Comparative religion educational sample",
            "Respectful interfaith knowledge sample",
        ],
    )


def generate_encyclopedia_species_things_basic():
    return _build_entry(
        system_prompts=[
            "You are an encyclopedia-style assistant giving concise factual summaries.",
            "You provide basic but accurate summaries of species, objects, and phenomena.",
        ],
        pairs=[
            (
                "Give a basic encyclopedia entry for the {species}.",
                "The {species} is known for its habitat, diet, and adaptation patterns. A useful summary includes distribution, behavior, and conservation status.",
            ),
            (
                "What are key facts about {object_name}?",
                "A clear entry should define it, explain main functions, common variants, and where it is typically used.",
            ),
            (
                "How do I write a beginner-friendly species profile?",
                "Use sections: classification, habitat, diet, behavior, reproduction, threats, and interesting facts.",
            ),
            (
                "Explain the difference between endangered and vulnerable species.",
                "Both indicate risk, but endangered generally means a higher immediate extinction risk than vulnerable.",
            ),
        ],
        slots={
            "species": ["snow leopard", "blue whale", "honey bee", "axolotl", "red panda", "peregrine falcon"],
            "object_name": ["microscope", "satellite", "wind turbine", "compass", "3D printer", "electric battery"],
        },
        tags=["encyclopedia", "species", "basic"],
        difficulties=["easy", "medium"],
        context_prompts=[
            "Basic encyclopedia content sample",
            "Species and object reference sample",
        ],
    )


def generate_foods_and_recipes_professional():
    dish = random.choice(["creamy mushroom pasta", "spicy chicken rice bowl", "vegetable stir fry", "lentil curry", "baked salmon"])
    serving = random.randint(2, 8)
    user = f"Create a professional recipe for {dish} serving {serving} people."
    assistant = (
        f"Professional recipe for {dish} ({serving} servings):\n"
        "1. Prep and measure ingredients before heat starts.\n"
        "2. Control heat in phases: aromatics, main ingredient, liquid/starch integration.\n"
        "3. Season progressively and taste at each stage.\n"
        "4. Finish with acid/fat balance and texture contrast before plating."
    )

    return {
        "messages": [
            {"role": "system", "content": "You are a professional culinary assistant."},
            {"role": "user", "content": user},
            {"role": "assistant", "content": assistant},
        ],
        "difficulty": "hard",
        "tags": ["food", "recipes", "professional"],
        "context": "Professional cooking and recipe construction sample",
        "safety_level": "safe",
    }


def generate_recipe_usage_understanding():
    return _build_entry(
        system_prompts=[
            "You are a kitchen operations assistant focused on recipe execution.",
            "You explain how and why each recipe step is used.",
        ],
        pairs=[
            (
                "Why do recipes ask to rest meat before slicing?",
                "Resting allows juices to redistribute, improving moisture and texture when sliced.",
            ),
            (
                "How should I adjust a recipe when doubling portions?",
                "Scale ingredients carefully, but increase spices and salt gradually while tasting to avoid over-seasoning.",
            ),
            (
                "What is the purpose of deglazing a pan?",
                "Deglazing dissolves browned fond into liquid, building concentrated flavor for sauces.",
            ),
            (
                "When should I use baking soda versus baking powder?",
                "Use baking soda with acidic ingredients; use baking powder when the recipe needs built-in acid-base leavening.",
            ),
            (
                "How can I substitute ingredients without breaking the recipe?",
                "Match functional roles first: moisture, fat, structure, and acidity, then adjust cooking time as needed.",
            ),
        ],
        slots={},
        tags=["recipes", "technique", "kitchen"],
        difficulties=["easy", "medium"],
        context_prompts=[
            "Recipe execution and technique understanding sample",
            "Culinary method reasoning dataset entry",
        ],
    )


def generate_unity_ultra():
    mechanic = random.choice(["movement", "inventory", "quest", "dialogue", "ability cooldown"])
    user = f"Give an ultra-advanced Unity 2D/3D architecture for a {mechanic} system, including Playmaker integration ideas."
    assistant = (
        "Use a data-driven architecture:\n"
        "- ScriptableObjects for design-time data\n"
        "- Runtime state machines for behavior\n"
        "- Event channels for decoupled communication\n"
        "- Playmaker FSMs for rapid designer iteration layered over tested C# core systems."
    )

    return {
        "messages": [
            {"role": "system", "content": "You are an ultra-advanced Unity game development assistant."},
            {"role": "user", "content": user},
            {"role": "assistant", "content": assistant},
        ],
        "difficulty": "hard",
        "tags": ["unity", "game_dev", "playmaker", "advanced"],
        "context": "Unity 2D/3D and Playmaker production sample",
        "safety_level": "safe",
    }


def generate_unreal_master():
    subsystem = random.choice(["combat", "AI behavior", "inventory", "ability system", "UI HUD"])
    user = f"Design a master-level Unreal Engine 2D/3D pipeline for {subsystem} using Blueprints and C++ boundaries."
    assistant = (
        "Use Blueprints for fast iteration and C++ for performance-critical core logic. "
        "Keep data assets for tuning, interface-based communication for modularity, and profiling-driven optimization before shipping."
    )

    return {
        "messages": [
            {"role": "system", "content": "You are an advanced Unreal Engine assistant."},
            {"role": "user", "content": user},
            {"role": "assistant", "content": assistant},
        ],
        "difficulty": "hard",
        "tags": ["unreal", "blueprints", "game_dev", "advanced"],
        "context": "Unreal Engine mixed Blueprint/C++ sample",
        "safety_level": "safe",
    }


def generate_godot_ultra():
    mechanic = random.choice(["platformer movement", "dialogue system", "save system", "pathfinding", "combat combo"])
    user = f"Provide an ultra Godot 2D/3D plan for implementing {mechanic} with clean scene architecture."
    assistant = (
        "Organize by scene composition, keep reusable nodes small, and script behavior in focused GDScript modules. "
        "Use signals for decoupling, autoloads for global state, and test deterministic gameplay loops."
    )

    return {
        "messages": [
            {"role": "system", "content": "You are an expert Godot assistant for 2D and 3D projects."},
            {"role": "user", "content": user},
            {"role": "assistant", "content": assistant},
        ],
        "difficulty": random.choice(["medium", "hard"]),
        "tags": ["godot", "game_dev", "advanced"],
        "context": "Godot engine architecture and implementation sample",
        "safety_level": "safe",
    }


def generate_hacking_safe_basics():
    return _build_entry(
        system_prompts=[
            "You are a cybersecurity awareness assistant focused on safe, legal, defensive knowledge.",
            "You refuse offensive hacking help and provide secure alternatives.",
        ],
        pairs=[
            (
                "Teach me very basic hacking concepts, but only safe and legal.",
                "Start with defensive fundamentals: strong passwords, MFA, phishing awareness, software updates, and safe network hygiene.",
            ),
            (
                "How can I check if my own account security is weak?",
                "Run a personal security checklist: unique password manager entries, MFA enabled, recovery options updated, and login history reviewed.",
            ),
            (
                "Give me beginner cybersecurity topics I can learn without harming anyone.",
                "Learn networking basics, common attack patterns at a conceptual level, threat modeling, secure coding basics, and incident response workflow.",
            ),
            (
                "Can you help me break into someone else's account?",
                "I cannot help with that. I can help you secure your own account and explain legal cybersecurity learning resources.",
            ),
            (
                "What is phishing and how do I avoid it?",
                "Phishing tricks users into sharing secrets. Verify sender identity, inspect links, avoid urgent-pressure messages, and never share OTP codes.",
            ),
        ],
        slots={},
        tags=["cybersecurity", "safe", "basics"],
        difficulties=["easy", "medium"],
        context_prompts=[
            "Defensive cybersecurity beginner sample",
            "Safe cyber awareness and refusal sample",
        ],
        safety_level="safe",
    )


def generate_internet_ultra():
    return _build_entry(
        system_prompts=[
            "You are an advanced internet literacy assistant.",
            "You teach expert-level search and browser workflows for productivity and safety.",
        ],
        pairs=[
            (
                "How do I do ultra-advanced search on {engine}?",
                "Use quoted phrases, site filters, filetype filters, date ranges, and query refinement loops to improve precision.",
            ),
            (
                "Compare productivity features in modern browsers.",
                "Evaluate tab groups, profiles, sync control, privacy settings, extension management, and reading workflows.",
            ),
            (
                "How can I verify if online information is trustworthy?",
                "Cross-check primary sources, inspect publication date, compare independent reports, and look for transparent methodology.",
            ),
            (
                "Give a master workflow for research on the web.",
                "Define a question, create keyword clusters, collect sources with notes, triangulate claims, then summarize with citations.",
            ),
        ],
        slots={
            "engine": ["Google", "Bing/Edge", "Yahoo", "Firefox search", "DuckDuckGo"],
        },
        tags=["internet", "research", "advanced"],
        difficulties=["medium", "hard"],
        context_prompts=[
            "Advanced web search and browser literacy sample",
            "Internet platform workflow training sample",
        ],
    )


def generate_anime_master():
    return _build_entry(
        system_prompts=[
            "You are an anime knowledge assistant with broad genre awareness.",
            "You provide balanced anime guidance, recommendations, and storytelling analysis.",
        ],
        pairs=[
            (
                "Recommend anime similar to {title} with strong character growth.",
                "Pick series with aligned tone, pacing, and development arcs; then explain why each recommendation matches those traits.",
            ),
            (
                "How do I analyze anime storytelling at a master level?",
                "Break it into theme, character arcs, scene composition, score usage, pacing, and payoff consistency.",
            ),
            (
                "Compare shonen and seinen narrative style.",
                "Shonen often emphasizes growth-through-challenge, while seinen usually explores mature ambiguity, slower pacing, and complex consequences.",
            ),
            (
                "How can I start watching anime without feeling overwhelmed?",
                "Pick one genre, start with 12-episode series, keep a watchlist, and alternate intense and light shows for balance.",
            ),
        ],
        slots={
            "title": ["Fullmetal Alchemist", "Steins;Gate", "Attack on Titan", "Demon Slayer", "Violet Evergarden"],
        },
        tags=["anime", "entertainment", "master"],
        difficulties=["easy", "medium", "hard"],
        context_prompts=[
            "Anime recommendation and analysis sample",
            "Anime storytelling training dialogue",
        ],
    )
