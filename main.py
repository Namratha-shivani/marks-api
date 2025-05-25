from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json
from typing import List

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load list of student records from JSON file
with open("q-vercel-python.json") as f:
    students_list = json.load(f)

# Convert to a dictionary: { "name": marks }
marks_data = {student["name"]: student["marks"] for student in students_list}

@app.get("/api")
def get_marks(name: List[str] = Query(...)):
    # Retrieve marks in order of query
    return {"marks": [marks_data.get(n, None) for n in name]}
