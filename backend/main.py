from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path

from services.dictionary_service import fetch_word_data

app=FastAPI() 

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR / "frontend"

#API ROUTES
#---------------------
@app.get("/api/get/{word}")
def get_word(word:str):
    result=fetch_word_data(word)

    if not result:
        raise HTTPException(status_code=404,detail="Word not Found")
    
    return result

#-----------------------------

#FRONTEND ROUTES
app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

@app.get("/")
def serve_home():
    return FileResponse(FRONTEND_DIR / "index.html")
