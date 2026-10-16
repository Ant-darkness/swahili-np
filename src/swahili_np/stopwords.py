
import re
from importlib.resources import files


def get_stopwords():
    """Return the baseline Swahili stopwords as a set."""
    resource = files("swahili_nlp").joinpath(
        "data/stopwords_sw.txt"
    )

    with resource.open("r", encoding="utf-8") as file:
        return {
            line.strip().lower()
            for line in file
            if line.strip()
        }


def remove_stopwords(text, stopwords=None):
    """Remove stopwords from a Swahili text."""
    if stopwords is None:
        stopwords = get_stopwords()

    tokens = re.findall(r"\b\w+\b", text.lower())

    cleaned_tokens = [
        token for token in tokens
        if token not in stopwords
    ]

    return " ".join(cleaned_tokens)
