import json
import os

PATTERN_FILE = "patterns.json"

def load_patterns():
    if not os.path.exists(PATTERN_FILE):
        return []
    with open(PATTERN_FILE, "r") as f:
        return json.load(f)

def save_patterns(patterns):
    with open(PATTERN_FILE, "w") as f:
        json.dump(patterns, f, indent=2)

def analyze_review(review_text, rating):
    text = review_text.lower()

    length = "short" if len(text) < 80 else "medium" if len(text) < 200 else "long"

    sentiment = "positive" if rating >= 4 else "neutral" if rating == 3 else "negative"

    signals = []
    if "food" in text: signals.append("food")
    if "service" in text: signals.append("service")
    if "atmosphere" in text or "ambience" in text: signals.append("atmosphere")
    if "recommend" in text: signals.append("recommendation")
    if "again" in text or "back" in text: signals.append("return_intent")

    return {
        "length": length,
        "sentiment": sentiment,
        "signals": signals,
        "rating": rating
    }

def store_pattern(pattern, restaurant):
    patterns = load_patterns()
    patterns.append({"restaurant": restaurant, "pattern": pattern})
    save_patterns(patterns)

def find_similar_pattern(pattern, restaurant):
    patterns = load_patterns()

    for p in reversed(patterns):
        if p["restaurant"] != restaurant:
            continue

        if (
            p["pattern"]["sentiment"] == pattern["sentiment"]
            and p["pattern"]["length"] == pattern["length"]
        ):
            return p["pattern"]

    return None

def get_response_strategy(pattern):
    sentiment = pattern["sentiment"]
    length = pattern["length"]
    signals = pattern["signals"]

    strategy = {
        "tone": "",
        "structure": "",
        "focus": "",
        "cta": ""
    }

    if sentiment == "positive":
        strategy["tone"] = "warm, grateful, enthusiastic"
        strategy["cta"] = "invite the guest again"
    elif sentiment == "neutral":
        strategy["tone"] = "balanced and appreciative"
        strategy["cta"] = "encourage another visit"
    else:
        strategy["tone"] = "empathetic and apologetic"
        strategy["cta"] = "rebuild trust"

    if length == "short":
        strategy["structure"] = "expand emotionally"
    elif length == "medium":
        strategy["structure"] = "balanced"
    else:
        strategy["structure"] = "detailed and personalized"

    focus = []
    if "food" in signals: focus.append("food quality")
    if "service" in signals: focus.append("service")
    if "atmosphere" in signals: focus.append("ambience")

    strategy["focus"] = ", ".join(focus) if focus else "overall experience"

    return strategy