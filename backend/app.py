from fastapi import FastAPI

app = FastAPI(
    title="MedFlow AI Agent",
    description="AI-driven healthcare workflow automation platform",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "message": "MedFlow AI Agent is running",
        "status": "ok"
    }

@app.get("/health")
def health_check():
    return {
        "service": "medflow-ai-agent",
        "health": "healthy"
    }

