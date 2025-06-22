from llama_cpp import Llama

# Load the model from the models directory
llm = Llama(model_path="models/tinyllama.gguf", n_ctx=512)

# Load markdown file (context)
with open("context/affordable-housing.md", "r") as f:
    context = f.read()

# Your question
query = "What is affordable housing?"

# Build the full prompt with context
prompt = f"""
You are a helpful housing assistant. Use the information below to answer the question.

Context:
{context}

Q: {query}
A:"""

# Run the model
output = llm(prompt, max_tokens=300)

# Print the answer
print(output["choices"][0]["text"].strip())


