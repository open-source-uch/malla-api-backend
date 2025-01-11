from fastapi import FastAPI
import json
import os

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}  

@app.get("/fcfm/{version}/mallas/{major}")
async def major(version: str, major: str):
    version_path = f"data/fcfm/{version}"
    if not os.path.exists(version_path):
        return {
            "status": "error",
            "message": f"Version {version} not found",
            "code": 404,
        }
    major_path = version_path + f"/mallas/{major}/index.json"
    if not os.path.exists(major_path):
        return {
            "status": "error",
            "message": f"Major {major} not found",
            "code": 404,
        }
    
    with open(major_path, "r") as f:
        return json.load(f)