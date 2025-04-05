from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core.node_parser import SentenceSplitter

# 🧠 Set your local Ollama model for both LLM and embeddings (Gemma instead of Mistral)
Settings.llm = Ollama(model="gemma:2b", request_timeout=120)
Settings.embed_model = OllamaEmbedding(model_name="gemma:2b")


# 📄 Load documents
print("\n📄 Loading documents...")
documents = SimpleDirectoryReader("../data", recursive=True).load_data()

for d in documents:
    if "AMI" in d.text:
        print("✅ Found AMI in:", d.metadata.get('file_name', 'unknown'))
        print(d.text[:150])

print(f"\n📄 Loaded {len(documents)} document(s).")
for i, doc in enumerate(documents):
    print(f"\n--- Document {i+1} Preview ---")
    print(doc.text[:300])
    print("-------------------------")

# 🧩 Chunk the docs
splitter = SentenceSplitter(chunk_size=300, chunk_overlap=50)
nodes = splitter.get_nodes_from_documents(documents)

print(f"\n🧩 Created {len(nodes)} chunks from all docs.\n")
for i, node in enumerate(nodes[:3]):
    print(f"Chunk {i+1}:\n{node.text}")
    print(f"Token estimate: {len(node.get_content().split())} words (rough)")
    print("-------------------------")


# 📈 Show embedding vector
# embed_model = Settings.embed_model
# embedding_vector = embed_model.get_text_embedding(nodes[0].text)
# print(f"\n📈 Embedding vector (first 10 values): {embedding_vector[:10]}...")
# print(f"Vector length: {len(embedding_vector)}")

# 🧠 Build the vector index
print("\n🧠 Building index...")
index = VectorStoreIndex.from_documents(documents)

# 🔍 Set up the query engine
query_engine = index.as_query_engine(response_mode="refine")

# 💬 Chat loop
print("\n💬 Ready to chat with your housing data! Type 'exit' to quit.\n")
while True:
    q = input("You: ")
    if q.lower() in ["exit", "quit"]:
        break

    response = query_engine.query(q)

    print(f"\n🤖 {response.response}\n")

    print("\n📄 Source Chunks Used:\n")
    for i, source in enumerate(response.source_nodes):
        print(
            f"🔹 Chunk {i+1} (score: {source.score:.2f}):\n{source.node.text[:250]}\n{'-'*60}")
