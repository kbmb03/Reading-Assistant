
# analyze_style.py
# Kaleb Davis 7/6/2025

import re
import statistics
from typing import Dict

def analyze_text_style(text: str) -> Dict[str, float]:
    """
    Analyze text style to extract statistics useful for tuning chunking behavior.
    Returns a dict with computed metrics:
      - avg_sentence_length
      - avg_paragraph_length
      - punctuation_density
      - long_sentence_ratio
      - ellipsis_usage
    """

    # Clean and split text
    paragraphs = re.split(r'\n\s*\n', text.strip())
    sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z])', text)

    # Remove empty items
    paragraphs = [p for p in paragraphs if p.strip()]
    sentences = [s for s in sentences if s.strip()]

    # Sentence lengths
    sentence_lengths = [len(s.split()) for s in sentences]
    avg_sentence_length = statistics.mean(sentence_lengths) if sentence_lengths else 0
    long_sentence_ratio = sum(1 for l in sentence_lengths if l > 30) / len(sentence_lengths) if sentence_lengths else 0

    # Paragraph lengths
    paragraph_lengths = [len(p.split()) for p in paragraphs]
    avg_paragraph_length = statistics.mean(paragraph_lengths) if paragraph_lengths else 0

    # Punctuation density
    punct_count = len(re.findall(r'[.,;:!?\-]', text))
    punct_density = punct_count / len(text) if text else 0

    # Ellipsis usage
    ellipsis_usage = len(re.findall(r'\.\.\.', text)) / len(text) if text else 0

    return {
        "avg_sentence_length": round(avg_sentence_length, 2),
        "avg_paragraph_length": round(avg_paragraph_length, 2),
        "punctuation_density": round(punct_density, 4),
        "long_sentence_ratio": round(long_sentence_ratio, 3),
        "ellipsis_usage": round(ellipsis_usage, 4)
    }


# Later this will be passed into a tuning function to dynamically set max_tokens and overlap_tokens
