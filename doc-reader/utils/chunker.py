def chunk_text(text, chunk_size=800, overlap=100):
    chunks = []
    start = 0
    no_chunks =0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        no_chunks += 1
        start += chunk_size - overlap  
    print("The total chunks in the chunker :",no_chunks) ## update 1
    return chunks
