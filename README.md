# Bloom Assist Chatbot

A single-turn Retrieval-Augmented Generation (RAG) chatbot designed to assist frontline workers and individuals in accessing affordable housing resources.

## 💻 Technologies and Frameworks Used

* **Frontend:** Next.js (sites/chatbot)
* **Backend:** NestJS (api/)
* **Microservice:** FastAPI (python-llm-service/)
* **Database:** ChromaDB (for vector storage)
* **Other:** Markdown-based static content, Yarn, Python 3.x

## ✨ Features

* Conversational UI for housing-related questions
* Static RAG context integration from markdown files
* Microservice architecture
* Framework integration

## 🛠️ Installation and Setup Instructions

1. Clone the repository
```bash
git clone https://github.com/your-username/jtc-capstone-2025.git
cd jtc-capstone-2025
```

2. Go into python-llm-service folder and create/activate a virtual environment (optional)
```bash
cd python-llm-service
python3 -m venv venv
source venv/bin/activate
```

3. Go into python-llm-service folder and install requirements
```bash
cd python-llm-service
pip install -r requirements.txt
uvicorn app:app --reload --port 8000
```
👍 Leave this running in a terminal tab
Open a new terminal to start the next step.

4. Start the NestJS backend
```bash
cd api
yarn install
yarn start
```
👍 Leave this running in a terminal tab
Open a new terminal to start the next step.

5. Start the Next.js frontend
```bash
cd sites/chatbot
yarn install
yarn dev
```
👍 Leave this running in a terminal tab
Visit: `http://localhost:3000`

## ▶️ Usage Example

Once all three services are running, visit `http://localhost:3000` and interact with the chatbot by asking affordable housing questions.

## 📊 Project Structure

```
.
├── agile_plan.md
├── api/
│   ├── dist/
│   ├── eslint.config.mjs
│   ├── nest-cli.json
│   ├── node_modules/
│   ├── package.json
│   ├── README.md
│   ├── src/
│   ├── test/
│   ├── tsconfig.build.json
│   ├── tsconfig.json
│   └── yarn.lock
├── check_list.md
├── completed_check_list.md
├── context/
│   └── affordable-housing.md
├── contributing.md
├── ethics_disclaimer.md
├── initial-issues.md
├── python-llm-service/
│   ├── __pycache__/
│   ├── app.py
│   ├── rag_utils.py
│   ├── requirements.txt
│   └── venv/
├── README.md
├── sites/
│   └── chatbot/
└── structure.txt
```

## 📄 License

This project is open source and available under the MIT License.