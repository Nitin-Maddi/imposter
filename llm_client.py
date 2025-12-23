import os
from google import genai
from collections import defaultdict


def generate_words(category: str, num_players: int, used_words: set[str] = None) -> list[str]:
    """Generate a list of words related to the given category using Gemini."""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable is not set")

    client = genai.Client(api_key=api_key)

    used_words_str = ""
    if used_words:
        used_words_str = f"Do NOT use any of these previously used words: {', '.join(used_words)}. "

    prompt = (
        f"Generate a comma-separated list of {num_players} words related to the category: {category}. "
        "ONLY 1 word should be different; ALL other words must be exactly the same. "
        "Shuffle the position of the different word - do not always place it first or last. "
        "The different word should be related to the category, but noticeably distinct."
        "Ensure that the generated words are very specific to this category and is not just broad words."
        f"{used_words_str}"
        "IMPORTANT: Return only the words separated by commas, no explanations or extra text."
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    words_text = response.text.strip()
    words = [word.strip() for word in words_text.split(",")]

    validate_words(words, num_players)

    return words

def validate_words(words: list[str], num_players):
    word_counts = defaultdict(int)
    for word in words:
        word_counts[word] += 1

    if (len(words) != num_players):
        print("LLM output had different number of words than players")
        return False

    if (len(word_counts.keys()) != 2):
        print("LLM output did not result in exactly 2 different words")
        return False

    if not (1 in word_counts.values() and len(words) - 1 in word_counts.values()):
        print("LLM output did not result in 1 imposter and n-1 regular words")
        return False

    return True
