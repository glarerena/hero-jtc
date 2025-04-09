✅ Capstone MVP: Build Checklist (Days 1 & 2)
This checklist documents the major milestones completed during the 2-day solo prototype sprint for the Capstone MVP project — a single-turn RAG chatbot with no memory.

🟩 Day 1 – Backend + Microservice Setup
✅ Project Structure & Planning
 Created GitHub repo: chatbot

 Set up folders: api/, python-llm-service/, context/, sites/chatbot/, shared-helpers/

 Added .gitignore, .env, README.md, ethics_disclaimer.md, agile_plan.md

 Added placeholder files for planning and structure

✅ NestJS Backend
 Scaffolded NestJS inside api/

 Deleted default controller and service

 Created chatbot.controller.ts with a POST /chatbot route

 Created chatbot.service.ts to forward requests to FastAPI

 Installed and configured axios for HTTP requests

✅ FastAPI Microservice
 Created python-llm-service/app.py and rag_utils.py

 Installed FastAPI, Uvicorn, and created a Python virtual environment (venv)

 Built POST /generate route to receive input and return mock RAG response

 Created context/affordable-housing.md with seed data

 Fixed relative path issues using os.path.abspath()

✅ Full Backend Flow Test
 Successfully tested /generate directly with curl

 Successfully tested full flow:

bash
Copy
Edit
User → NestJS `/chatbot` → FastAPI `/generate` → Returns RAG response
🟦 Day 2 – Frontend + Chat UI Setup
✅ Next.js App Setup
 Scaffolded Next.js app with TypeScript using create-next-app inside sites/chatbot/

 Chose CSS Modules (no Tailwind)

 Disabled Turbopack (used Webpack for stability)

✅ Chat UI Build
 Created pages/index.tsx with question form and fetch logic

 Created components/ChatBox.tsx to display chatbot responses

 Styled response box using ChatBox.module.css

 Handled loading and error states in the UI

✅ Frontend → Backend Integration
 Connected frontend form to NestJS /chatbot route

 Displayed chatbot reply in real-time using local dev server

✅ Final Functional Test
 Launched frontend on localhost:3000

 Typed a question

 Saw chatbot respond with context from Markdown file via full stack pipeline

🎉 Result: MVP Prototype Complete!
You now have a fully working Capstone MVP with:

✅ Functional RAG chatbot logic

✅ Modular architecture

✅ Clean backend + microservice separation

✅ Frontend UI and UX with real-time feedback

✅ Clean repo and scalable codebase for future improvements