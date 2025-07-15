#Kaleb Davis
#7/10/2025
import re

def extract_candidate_numbers(text: str) -> list[int | str]:
    lines = text.strip().splitlines()
    candidates = []

    # Get top and bottom lines
    check_lines = lines[:5] + lines[-5:]

    for line in check_lines:
        line = line.strip()
        # Check for standalone Arabic numerals
        if re.fullmatch(r'\d{1,4}', line):
            candidates.append(int(line))
        # Check for uppercase Roman numerals (up to M)
        elif re.fullmatch(r'[IVXLCDM]{1,7}', line):
            candidates.append(line)

    return candidates

def infer_page_numbers(pages: list[tuple[int, str]]) -> dict[int, str | int]:
    page_number_map = {}
    last_value = None

    for index, text in pages:
        candidates = extract_candidate_numbers(text)

        # Find the first candidate that’s greater than the previous
        selected = None
        for cand in candidates:
            if isinstance(cand, int):
                if last_value is None or cand > last_value:
                    selected = cand
                    break
            elif isinstance(cand, str):  # assume Roman numeral
                selected = cand  # For now, don't compare order
                break

        if selected is not None:
            page_number_map[index] = selected
            if isinstance(selected, int):
                last_value = selected

    return page_number_map
