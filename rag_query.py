import chromadb
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from ollama import Client

def Extract_context(query):
    """Retrieves relevant context from the ChromaDB vector store based on the query."""
    chroma_client = chromadb.HttpClient(host='172.20.132.45', port=8000)
    embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma(
        client=chroma_client,
        collection_name="my_collection",
        embedding_function=embedding_function
    )
    docs = db.similarity_search(query)
    return '\n\n'.join([doc.page_content for doc in docs])  # Join with newlines

def get_system_message_rag(content):
        return f"""You are an expert troubleshooting technician providing assistance to assist individuals by retrieving relevant information from internal documents.

        Generate your response by following the steps below:
        1. Recursively break down the question into smaller questions.
        2. For each question/directive:
            2a. Select the most relevant information from the context in light of the conversation history.
        3. Generate a draft response using selected information.
        4. Remove duplicate content from draft response.
        5. Generate your final response after adjusting it to increase accuracy and relevance.
        6. Do not try to summarise the answers, explain it properly.
        6. Only show your final response! 
        
        Constraints:
        1. DO NOT PROVIDE ANY EXPLANATION OR DETAILS OR MENTION THAT YOU WERE GIVEN CONTEXT.
        2. Don't mention that you are not able to find the answer in the provided context.
        3. Don't make up the answers by yourself.
        4. Try your best to provide answer from the given context.

        CONTENT:
        {content}
        """

def get_ques_response_prompt(question):
    return f"""
    ==============================================================
    Based on the above context, please provide the answer to the following question:
    {question}
    """

def generate_rag_response(content,question):
    client = Client(host='http://localhost:11434') # Ollama typically runs on port 11434 verify Ollama is running by browsing to: http://localhost:11434/
    stream = client.chat(model='mistral:latest', messages=[
    {"role": "system", "content": get_system_message_rag(content)},            
    {"role": "user", "content": get_ques_response_prompt(question)}
    ], stream=True)

    print("Question:", question)
    print("Generating Answer.... ")

    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)

    print()

def main():
    """Interactive loop to get questions from the user and generate answers."""

    print("Welcome to the RAG Question Answering System!")
    print("Type 'exit' to quit.\n")
    
    while True:
        query = input("Enter your question: ")
        if query.lower() == 'exit':
            break
        context = Extract_context(query)
        if not context:
            print("No relevant information found in the documents.\n")
            continue  # Ask for the next question
        generate_rag_response(context, query)
        print("\n")

if __name__ == "__main__":
    main()