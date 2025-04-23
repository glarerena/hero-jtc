# Bloom Assist Chatbot

A conversational Retrieval-Augmented Generation (RAG) chatbot designed to help frontline workers and individuals access affordable housing resources.

## 💻 Technologies

* **Frontend:** Next.js (sites/chatbot)
* **Backend:** NestJS (api/)
* **Microservice:** FastAPI (python-llm-service/)
* **Database:** ChromaDB (vector storage)
* **Other:** Markdown-based static content, Yarn, Python 3.x

## ✨ Features

* Intuitive conversational interface for housing-related inquiries
* Static RAG context integration from markdown files
* Microservice architecture for scalability
* Seamless framework integration

## 🛠️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/glarerena/jtc-capstone-2025.git
cd jtc-capstone-2025
```

2. **Set up Python LLM service**
```bash
cd python-llm-service
python3 -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --reload --port 8000
```
Leave this running in a terminal tab.

3. **Start the NestJS backend**
In a new terminal:
```bash
cd api
yarn install
yarn start
```
Leave this running in a terminal tab.

4. **Launch the Next.js frontend**
In a new terminal:
```bash
cd sites/chatbot
yarn install
yarn dev
```
When all services are running, visit: `http://localhost:3000`

## ▶️ Usage

Visit `http://localhost:3000` in your browser and interact with the chatbot by asking questions about affordable housing. The system uses RAG technology to provide accurate, context-aware responses based on housing resource information.

## 📊 Project Structure

```
.
├── api/                          # NestJS backend service
│   ├── src/                      # Source code
│   ├── test/                     # Testing files
│   └── ...
├── context/                      # Knowledge base markdown files
│   └── affordable-housing.md     # Housing resources information
├── python-llm-service/           # FastAPI microservice for LLM integration
│   ├── app.py                    # Main application file
│   ├── rag_utils.py              # RAG utility functions
│   └── requirements.txt          # Python dependencies
├── sites/                        # Frontend applications
│   └── chatbot/                  # Next.js chatbot interface
├── agile_plan.md                 # Project planning documentation
├── contributing.md               # Contribution guidelines
├── ethics_disclaimer.md          # Ethics statement
└── README.md                     # This file
```


## 📄 License

This project is open source and available under the MIT License.