# HERO Chatbot  
**Housing Essential Resource Organization**

A chatbot to help find affordable housing resources in the Bay Area.

## 🚀 Deploy

### 1. Python Service (Render)
- Connect GitHub repo
- Root: `python-llm-service`
- Build: `pip install -r requirements.txt`
- Start: `python main.py`
- Env: `PYTHON_VERSION=3.11`

### 2. NestJS Backend (Render)
- Connect GitHub repo  
- Root: `api`
- Build: `npm install && npm run build`
- Start: `npm run start:prod`
- Env: `PYTHON_API_URL=https://your-python-service.onrender.com`

### 3. Frontend (Vercel)
- Import GitHub repo
- Root: `sites/chatbot`
- Env: `NEXT_PUBLIC_API_URL=https://your-nestjs-service.onrender.com`

## 💻 Local Dev

```bash
# Python
cd python-llm-service && python main.py

# Backend  
cd api && yarn start

# Frontend
cd sites/chatbot && yarn dev
```

Visit: `http://localhost:3000`
