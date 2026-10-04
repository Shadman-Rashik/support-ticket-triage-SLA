from config import CATEGORIES, PRIORITY_KEYWORDS

def classify(subject, description):
    text = f"{subject} {description}".lower()
    best, best_hits = "General", 0
    for category, words in CATEGORIES.items():
        hits = sum(1 for w in words if w in text)
        if hits > best_hits:
            best, best_hits = category, hits
    return best

def prioritize(subject, description):
    text = f"{subject} {description}".lower()
    for level in ("P1", "P2", "P3"):
        if any(w in text for w in PRIORITY_KEYWORDS[level]):
            return level
    return "P4"