import uuid
import chromadb
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from loader import load_and_split_documents

directory_path = "data"

# 1. Load Documents
docs = load_and_split_documents(directory_path)

# 2. Set Up Embedding Function
embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# 3. Create ChromaDB Client
client = chromadb.HttpClient(host='172.20.132.45', port=8000)

# 4. Create/Get Collection
collection_name = "my_collection"

# Check if the collection exists
collections = client.list_collections()
if collection_name in [col.name for col in collections]:
    # If it exists, get the collection
    collection = client.get_collection(collection_name)
else:
    # If it doesn't exist, create it
    collection = client.create_collection(collection_name)

# 5. Add Documents to ChromaDB
for doc in docs:
    collection.add(
        ids=[str(uuid.uuid1())],
        metadatas=[doc.metadata], 
        documents=[doc.page_content], 
    )

# 6. Create LangChain Chroma VectorStore
db = Chroma(
    client=client,
    collection_name="my_collection",
    embedding_function=embedding_function,
)

#---Sanity Check---#
"""
# 7. Query and Retrieve Results
query = "Minicom"
docs = db.similarity_search(query)

# 8. Print Results (If found)
if docs:
    print(docs[0].page_content)
else:
    print("No relevant documents found.")
"""