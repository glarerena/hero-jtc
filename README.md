# HERO Chatbot  
**Housing Essential Resource Organization**

<img src="purple_house.png" alt="HERO Favicon" width="24" />

A rebranded, user-focused **Retrieval-Augmented Generation (RAG)** chatbot  
designed to help frontline workers and individuals quickly find  
affordable housing resources.



## 💻 Technologies

* **Frontend:** Next.js (sites/chatbot)
* **Backend:** NestJS (api/)
* **Microservice:** FastAPI (python-llm-service/)
* **Other:** Markdown-based static content, Yarn, Python 3.x

## ✨ Features

* Retrieval-Augmented Generation (RAG) using markdown-based static context  
* FastAPI-powered Python backend with LLM microservice for response generation  
* Real-time data access via Bloom Housing API (Swagger UI) for live housing listings  
* Modular architecture designed for easy scaling and seamless integration  

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

Visit `http://localhost:3000` in your browser and interact with the HERO chatbot by asking questions about affordable housing. The system uses RAG technology and AMI filtering to provide accurate, context-aware responses based on housing resource information.


## 📊 Project Structure

```
.
├── api/                          # NestJS backend service
│   ├── src/                      # Source code for API
│   ├── test/                     # Unit/integration tests
│   ├── package.json              # API dependencies and scripts
│   └── nest-cli.json, tsconfig*  # NestJS config files
├── assets/                       # Project presentation and feature screenshots
│   ├── flowchart.png
│   ├── live_listings.png
│   ├── load_chatbot.png
│   └── thank_you.png
├── context/                      # Knowledge base markdown files
│   └── affordable-housing.md     # Housing resources context file
├── python-llm-service/           # FastAPI microservice for RAG + LLM
│   ├── app.py, application.py    # Main app entry points
│   ├── ami_utils.py              # AMI filtering logic
│   ├── listings.py, listings.txt # Live listings logic and seed data
│   └── rag_utils.py              # RAG functionality
├── sites/
│   └── chatbot/                  # Next.js frontend for HERO Chatbot
├── developers_guide.md           # Dev setup guide
├── ethics_disclaimer.md          # Project ethical use policy
├── project_update.md             # Latest team progress report
├── structure.txt                 # Tree snapshot of folder structure
└── README.md                     # Project overview (this file)
```


## 📄 License

This project is open source and available under the MIT License.
