from fastapi import FastAPI, Request
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("google api- AIzaSyAproCEH8GkirbYPJUCEjPfml2G98pcVVY")

app = FastAPI()

genai.configure(api_key=google api- AIzaSyAproCEH8GkirbYPJUCEjPfml2G98pcVVY)
model = genai.GenerativeModel('gemini-pro')

@app.get("/")
def root():
    return {"message": "Shringaristan Gemini Chatbot is running."}

@app.post("/chat")
async def chat(request: Request):
    body = await request.json()
    user_input = body.get("message", "")
    response = model.generate_content(user_input)
    return {"response": response.text}
