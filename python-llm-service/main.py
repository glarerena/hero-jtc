import uvicorn
from app import app
import os

if __name__ == "__main__":
    # Get port from environment variable (Render sets PORT)
    port = int(os.environ.get("PORT", 8000))
    
    # Run the app
    uvicorn.run(
        "app:app",
        host="0.0.0.0",  # Allow external connections
        port=port,
        reload=False  # Disable reload in production
    ) 