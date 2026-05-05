from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from app.core.config import settings
from app.api.v1 import api_v1_router
from app.core.database import Base, engine

# Create Tables
Base.metadata.create_all(bind=engine)
# Create FastAPI app instance
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug,
)

# Add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["localhost", "127.0.0.1"]
)

# Include routers
app.include_router(api_v1_router)

# Root endpoint
@app.get("/")
def root():
    return {
        "message": "Welcome to Task Management Service v1",
        "version": settings.app_version,
        "docs": "/docs",
        "openapi": "/openapi.json"
    }

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug
    )
