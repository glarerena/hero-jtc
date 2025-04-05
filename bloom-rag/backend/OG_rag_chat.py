from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding

# Set your local models
Settings.llm = Ollama(model="gemma:2b", request_timeout=120)
Settings.embed_model = OllamaEmbedding(
    model_name="gemma:2b", request_timeout=120)

# Load your documents
print("📄 Loading documents...")
documents = SimpleDirectoryReader("../data", recursive=True).load_data()

# Build the index
print("🧠 Building index...")
index = VectorStoreIndex.from_documents(documents)

# Set up the query engine
query_engine = index.as_query_engine()

# Start chat loop
print("\n💬 Ready to chat with your housing data! Type 'exit' to quit.\n")
while True:
    q = input("You: ")
    if q.lower() in ["exit", "quit"]:
        break
    response = query_engine.query(q)
    print(f"\n🤖 {response}\n")
