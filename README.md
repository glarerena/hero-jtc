# HERO Chatbot  
**Housing Essential Resource Organization**

<img src="purple_house.png" alt="HERO Favicon" width="48" />

A user-focused chatbot to help frontline workers and individuals find affordable housing resources in the Bay Area.

## 💻 Tech Stack

- **Frontend:** Next.js (`sites/chatbot`) - Deployed on Vercel
- **Backend:** NestJS (`api/`) - Deployed on Render
- **Python Service:** FastAPI (`python-llm-service/`) - Deployed on Render
- **No LLM Dependencies** - All responses are hardcoded with hyperlinks

## ✨ Key Features

- Hardcoded responses with proper hyperlinks
- Live housing listings from static data
- Application information and links
- AMI calculations for income requirements
- Document requirements and tips
- No external API dependencies

## 🚀 Deployment Instructions

### 1. Python FastAPI Service (Render)

1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name**: `hero-python-api`
   - **Root Directory**: `python-llm-service`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python main.py`
   - **Plan**: Free

5. Add environment variable:
   - `PYTHON_VERSION`: `3.11`

6. Deploy and note the URL (e.g., `https://hero-python-api.onrender.com`)

### 2. NestJS Backend (Render)

1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name**: `hero-nestjs-api`
   - **Root Directory**: `api`
   - **Environment**: `Node`
   - **Build Command**: `npm install && npm run build`
   - **Start Command**: `npm run start:prod`
   - **Plan**: Free

5. Add environment variables:
   - `NODE_ENV`: `production`
   - `PYTHON_API_URL`: `https://hero-python-api.onrender.com` (from step 1)

6. Deploy and note the URL (e.g., `https://hero-nestjs-api.onrender.com`)

### 3. Next.js Frontend (Vercel)

1. Go to [Vercel Dashboard](https://vercel.com/dashboard)
2. Click "New Project"
3. Import your GitHub repository
4. Configure:
   - **Framework Preset**: Next.js
   - **Root Directory**: `sites/chatbot`
   - **Build Command**: `npm run build`
   - **Output Directory**: `.next`

5. Add environment variable:
   - `NEXT_PUBLIC_API_URL`: `https://hero-nestjs-api.onrender.com` (from step 2)

6. Deploy

## ⚙️ Local Development

1. **Start Python Service**
   ```bash
   cd python-llm-service
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python main.py
   ```

2. **Start NestJS Backend**
   ```bash
   cd api
   yarn install
   yarn start
   ```

3. **Run Frontend**
   ```bash
   cd sites/chatbot
   yarn install
   yarn dev
   ```

Then visit: `http://localhost:3000`

## 🗂️ Folder Structure

```
api/                  # NestJS backend
python-llm-service/   # FastAPI service (no LLM)
sites/chatbot/        # Next.js frontend
assets/               # Screenshots & flowcharts
```

## 📄 License

MIT License — free to use, modify, or extend.
