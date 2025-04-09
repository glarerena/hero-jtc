🧠 Capstone MVP – RAG Chatbot (Local Setup)
This project is a barebones prototype for a single-turn Retrieval-Augmented Generation (RAG) chatbot with no memory. It includes:

A NestJS backend (api/)

A FastAPI microservice (python-llm-service/)

A Next.js frontend (sites/chatbot/)

Static context files stored in context/

🛠️ How to Run Locally
1. Clone the repo (if not already)
bash
Copy
Edit
git clone https://github.com/your-username/chatbot.git
cd chatbot
2. Start the Python FastAPI microservice
bash
Copy
Edit
cd python-llm-service
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
uvicorn app:app --reload --port 8000
✅ Leave this running in a terminal tab

3. Start the NestJS backend
Open a new terminal tab:

bash
Copy
Edit
cd api
yarn install
yarn start
The NestJS server runs on http://localhost:3000

4. Start the Next.js frontend
Open a third terminal tab:

bash
Copy
Edit
cd sites/chatbot
yarn install
yarn dev
Visit http://localhost:3000 to chat with the bot

📄 Notes
Static RAG context lives in context/affordable-housing.md

API route: POST /chatbot

Microservice route: POST /generate
