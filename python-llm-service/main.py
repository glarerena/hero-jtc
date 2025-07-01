import uvicorn
from app import app
import os

if __name__ == "__main__":
    # Get port from environment variable (Render sets PORT)
    port = int(os.environ.get("PORT", 8000))

    # Run the app directly using the imported app object
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port,
        reload=False
    )
