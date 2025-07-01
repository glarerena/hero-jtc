# HERO Chatbot  
**Housing Essential Resource Organization**

<img src="images/purple_house.png" alt="HERO Favicon" width="48" />

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
# Terminal 1: Python Service
cd python-llm-service
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload --port 8000

# Terminal 2: NestJS Backend
cd api
yarn install
yarn start

# Terminal 3: Frontend
cd sites/chatbot
yarn install
yarn dev
```

Visit: `http://localhost:3000`
