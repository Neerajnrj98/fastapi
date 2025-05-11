from fastapi import FastAPI, Request
import google.generativeai as genai
import os
from dotenv import load_dotenv
from fastapi.staticfiles import StaticFiles

# Load environment variables (if using .env)
load_dotenv()

# Set your GEMINI API Key directly
GEMINI_API_KEY = "google api- AIzaSyAproCEH8GkirbYPJUCEjPfml2G98pcVVY"

# Initialize FastAPI app
app = FastAPI()

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# Mount static files (if any)
app.mount("/", StaticFiles(directory="static", html=True), name="static")

# Home route (get request)
@app.get("/")
async def root():
    return {"message": "Shringaristan Gemini Chatbot is running."}

# Chat route (post request)
@app.post("/chat")
async def chat(request: Request):
    body = await request.json()
    user_input = body.get("message", "")
    response = model.generate_content(user_input)
    return {"response": response.text}
