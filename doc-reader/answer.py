from query import search
from utils.llm import generate_answer

def ask_question(question):
    # Retrieve relevant chunks from FAISS
    chunks = search(question, k=5)

    # Combine chunks into a single context
    context = "\n\n".join(chunks)

    # Generate answer using the LLM (Mistral via Ollama)
    return generate_answer(context, question)


if __name__ == "__main__":
    print("📄 Document Chatbot is running...")
    print("Type your question below.")
    print("Type 'exit' to quit.\n")

    while True:
        question = input("Ask a question: ")

        # Clean input (handles exit, exit^M, extra spaces, etc.)
        if question.strip().lower() == "exit":
            print("Goodbye 👋")
            break

        answer = ask_question(question)

        print("\nANSWER:\n")
        print(answer)
        print("\n" + "-" * 60 + "\n")
