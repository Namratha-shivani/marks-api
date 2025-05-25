from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json
from typing import List

app = FastAPI()

# Load marks data once on startup
with open("q-vercel-python.json") as f:
    marks_data = json.load(f)

# Enable CORS so any origin can access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/api")
def get_marks(name: List[str] = Query(...)):
    # For each name requested, get their marks or None if not found
    results = [marks_data.get(n, None) for n in name]
    return {"marks": results}
