from llama_index.core import SimpleDirectoryReader

docs = SimpleDirectoryReader("../data", recursive=True).load_data()
for d in docs:
    if "AMI" in d.text:
        print("✅ Found AMI:")
        print(d.text[:200])
