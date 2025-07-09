#chunker
#Kaleb Davis 7/8/2025
import re
import tiktoken

def clean_chunk(chunk):
    chunk = chunk.strip()
    return chunk if len(chunk.split()) > 5 else None

def clean_uploaded_text(text):
    # Remove page numbers
    text = re.sub(r'^\s*\d+\s*$', '', text, flags=re.MULTILINE)
    
    # Remove section headers/footers
    text = re.sub(r'^\s*First essay\s*$', '', text, flags=re.MULTILINE)
    
    # Remove line breaks
    text = re.sub(r'(?<!\n)\n(?!\n)', ' ', text)  # single line breaks -> space
    
    #fix hyphenated words at line ends
    text = re.sub(r'-\s*\n\s*', '', text)

    # Normalize multiple new lines to paragraph breaks
    text = re.sub(r'\n{2,}', '\n\n', text)

    return text.strip()



#split by sentence, or parahraph?? lets see
def chunk_text_by_paragraph(text, max_tokens=300, overlap_tokens=50):
    enc = tiktoken.encoding_for_model("gpt-3.5-turbo")
    paragraphs = re.split(r'\n\s*\n', text.strip())
    
    chunks = []
    for para in paragraphs:
        tokens = enc.encode(para)
        if len(tokens) <= max_tokens:
            decoded = enc.decode(tokens)
            cleaned = clean_chunk(decoded)
            if cleaned:
                chunks.append(cleaned)
        else:
            # Break the paragraph further by sentence
            sentences = re.split(r'(?<=[.!?]) +', para)
            sentence_group = ""
            sentence_tokens = []
            for sentence in sentences:
                sent_tokens = enc.encode(sentence)
                if len(sentence_tokens) + len(sent_tokens) > max_tokens:
                    decoded = enc.decode(sentence_tokens)
                    cleaned = clean_chunk(decoded)
                    if cleaned:
                        chunks.append(cleaned)
                    sentence_tokens = sent_tokens
                else:
                    sentence_tokens.extend(sent_tokens)
            if sentence_tokens:
                decoded = enc.decode(sentence_tokens)
                cleaned = clean_chunk(decoded)
                if cleaned:
                    chunks.append(cleaned)

    return chunks


def Chunkify(text, max_tokens=300, overlap_tokens=50):
    cleanedText = clean_uploaded_text(text)
    return chunk_text_by_paragraph(cleanedText, max_tokens=max_tokens, overlap_tokens=overlap_tokens)


