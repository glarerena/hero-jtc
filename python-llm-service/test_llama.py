from llama_cpp import Llama

# Load the model from the models directory
llm = Llama(model_path="models/tinyllama.gguf", n_ctx=512)

# Ask a test question
output = llm("Q: What is affordable housing?\nA:", max_tokens=100)

# Print the model's response
print(output["choices"][0]["text"].strip())

