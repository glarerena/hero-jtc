# HERO Deployment Guide

This guide will help you deploy the HERO chatbot without any LLM dependencies using only hardcoded responses.

## Architecture

- **Frontend**: Next.js app deployed on Vercel
- **Backend**: NestJS API deployed on Railway
- **Python Service**: FastAPI service deployed on Railway (no LLM dependencies)

## Deployment Steps

### 1. Python FastAPI Service (Railway)

1. Go to [Railway Dashboard](https://railway.app/dashboard)
2. Click "New Project" → "Deploy from GitHub repo"
3. Connect your GitHub repository
4. Configure the service:
   - **Root Directory**: `python-llm-service`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python main.py`

5. Deploy and note the URL (e.g., `https://hero-python-api.railway.app`)

### 2. NestJS Backend (Railway)

1. Go to [Railway Dashboard](https://railway.app/dashboard)
2. Click "New Project" → "Deploy from GitHub repo"
3. Connect your GitHub repository
4. Configure the service:
   - **Root Directory**: `api`
   - **Build Command**: `npm install && npm run build`
   - **Start Command**: `npm run start:prod`

5. Add environment variable:
   - `PYTHON_API_URL`: `https://hero-python-api.railway.app` (from step 1)

6. Deploy and note the URL (e.g., `https://hero-nestjs-api.railway.app`)

### 3. Next.js Frontend (Vercel)

1. Go to [Vercel Dashboard](https://vercel.com/dashboard)
2. Click "New Project"
3. Import your GitHub repository
4. Configure the project:
   - **Framework Preset**: Next.js
   - **Root Directory**: `sites/chatbot`
   - **Build Command**: `npm run build`
   - **Output Directory**: `.next`

5. Add environment variable:
   - `NEXT_PUBLIC_API_URL`: `https://hero-nestjs-api.railway.app` (from step 2)

6. Deploy

## Environment Variables Summary

### Python Service
- `PORT`: Set automatically by Railway

### NestJS Backend
- `PYTHON_API_URL`: URL of your Python service

### Next.js Frontend
- `NEXT_PUBLIC_API_URL`: URL of your NestJS backend

## Testing the Deployment

1. **Test Python Service**: Visit `https://your-python-service.railway.app/health` for health check
2. **Test NestJS Backend**: Visit `https://your-nestjs-service.railway.app` for API health check
3. **Test Frontend**: Visit your Vercel URL and try the chatbot

## Features Available

The deployed version includes:
- ✅ Hardcoded responses with hyperlinks
- ✅ Housing listings from static data
- ✅ Application information
- ✅ AMI calculations
- ✅ Document requirements
- ✅ General housing resources
- ✅ No LLM dependencies

## Troubleshooting

### Common Issues

1. **Python service not starting**: Check if `main.py` exists and has correct permissions
2. **NestJS can't connect to Python**: Verify `PYTHON_API_URL` environment variable
3. **Frontend can't connect to backend**: Verify `NEXT_PUBLIC_API_URL` environment variable

### Logs

- **Railway**: Check service logs in the Railway dashboard
- **Vercel**: Check deployment logs in the Vercel dashboard

## Cost

- **Railway**: Free tier (2 projects)
- **Vercel**: Free tier
- **Total**: $0/month

## Maintenance

- No LLM costs or dependencies
- Static responses ensure consistent behavior
- Easy to update by modifying hardcoded responses in `rag_utils.py` 