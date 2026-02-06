import subprocess

SYSTEM_PROMPT = """
You are a document assistant.
Answer ONLY using the provided context.
If the answer is not found in the context, say:
"Not found in the document."

also asked ask for title and not there you can suggest the title and give that as no title so suggested title as 

Do not use outside knowledge.
"""

def generate_answer(context, question):
    prompt = f"""
{SYSTEM_PROMPT}

Context:
{context}

Question:
{question}

Answer:
"""

    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=prompt,
        text=True,
        capture_output=True
    )

    return result.stdout.strip()
