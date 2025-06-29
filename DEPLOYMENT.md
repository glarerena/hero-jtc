# HERO Deployment Guide

This guide will help you deploy the HERO chatbot without any LLM dependencies using only hardcoded responses.

## Architecture

- **Frontend**: Next.js app deployed on Vercel
- **Backend**: NestJS API deployed on Render
- **Python Service**: FastAPI service deployed on Render (no LLM dependencies)

## Deployment Steps

### 1. Python FastAPI Service (Render)

1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure the service:
   - **Name**: `hero-python-api`
   - **Root Directory**: `python-llm-service`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python main.py`
   - **Plan**: Free

5. Add environment variables:
   - `PYTHON_VERSION`: `3.11`

6. Deploy and note the URL (e.g., `https://hero-python-api.onrender.com`)

### 2. NestJS Backend (Render)

1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure the service:
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
4. Configure the project:
   - **Framework Preset**: Next.js
   - **Root Directory**: `sites/chatbot`
   - **Build Command**: `npm run build`
   - **Output Directory**: `.next`

5. Add environment variables:
   - `NEXT_PUBLIC_API_URL`: `https://hero-nestjs-api.onrender.com` (from step 2)

6. Deploy

## Environment Variables Summary

### Python Service
- `PORT`: Set automatically by Render
- `PYTHON_VERSION`: `3.11`

### NestJS Backend
- `NODE_ENV`: `production`
- `PYTHON_API_URL`: URL of your Python service

### Next.js Frontend
- `NEXT_PUBLIC_API_URL`: URL of your NestJS backend

## Testing the Deployment

1. **Test Python Service**: Visit `https://hero-python-api.onrender.com/docs` for FastAPI docs
2. **Test NestJS Backend**: Visit `https://hero-nestjs-api.onrender.com` for API health check
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

- **Render**: Check service logs in the Render dashboard
- **Vercel**: Check deployment logs in the Vercel dashboard

## Cost

- **Render**: Free tier (2 services)
- **Vercel**: Free tier
- **Total**: $0/month

## Maintenance

- No LLM costs or dependencies
- Static responses ensure consistent behavior
- Easy to update by modifying hardcoded responses in `rag_utils.py` 