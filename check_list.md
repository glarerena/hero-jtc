# 🚧 Capstone MVP Build Checklist (Solo Prototype)

## 🟩 Day 1: Backend + Microservice Setup

### 🧱 Project Setup
- [ ] Create new repo: `capstone-chatbot-prototype`
- [ ] Add folder structure from `structure.txt`
- [ ] Add `.env` file with placeholders for service URLs
- [ ] Add `README.md`, `agile_plan.md`, and `ethics_disclaimer.md`

### 🛠️ NestJS Backend
- [ ] Scaffold NestJS in `api/`
- [ ] Create `chatbot.controller.ts` with POST `/chatbot` route
- [ ] Create `chatbot.service.ts` that sends user input to Python microservice

### 🧠 Python Microservice (FastAPI)
- [ ] Create `app.py` with POST `/generate` endpoint
- [ ] Create `rag_utils.py` to search static files in `context/`
- [ ] Return a basic or mock response

### 🔗 Connect Backend to Python
- [ ] Use Axios or `node-fetch` in NestJS to call Python service
- [ ] Test the full backend flow using Postman or curl
- [ ] Log response from Python service in NestJS

---

## 🟦 Day 2: Frontend + RAG Prompt Polishing

### 💻 Next.js Frontend
- [ ] Scaffold Next.js in `sites/chatbot/`
- [ ] Create `pages/index.tsx` with a form to input questions
- [ ] Create `ChatBox.tsx` component
- [ ] Style ChatBox with `ChatBox.module.css`

### 🔁 Connect UI → NestJS
- [ ] POST form input to `/chatbot`
- [ ] Display chatbot response on the page
- [ ] Handle errors and loading states

### 📄 Add RAG Context Files
- [ ] Add markdown or JSON files to `context/`
- [ ] Update `rag_utils.py` to return relevant content
- [ ] Inject content into LLM-style prompt before response

### ✅ Final Polish
- [ ] Add comments and cleanup unused code
- [ ] Push to GitHub and verify repo works on a fresh clone
- [ ] Update `README.md` with instructions and architecture overview
- [ ] (Optional) Add LM Studio integration or sample `.env.example`

---

This 2-day plan ensures a working MVP prototype with clean modular structure, testable RAG logic, and a responsive frontend.

