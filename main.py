from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import google.generativeai as genai
import uvicorn
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

# Enable CORS (for cross-platform/browser access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Helper: Create prompt based on endpoint
def build_prompt(data: dict, endpoint: str) -> str:
    if endpoint == "water":
        return (
            f"You have the following data: {data} of a person's water intake. "
            "Give the amount of water they should drink today and a motivating line. "
            "Limit response to 25 words."
        )
    elif endpoint == "gym":
        return (
            f"You have the following data: {data} of a person's gym activity. "
            "Motivate based on their routine, suggest exercise intensity, and advise healthy eating. "
            "Limit response to 25 words."
        )
    elif endpoint == "food":
        return (
            f"You have the following data: {data} of a person's food intake.A detail meal what the user ate , calculate the user calories intake and give your response. "
            "Encourage healthy meals and motivate them to eat better. "
            "Limit response to 25 words."
        )
    else:
        raise ValueError("Invalid endpoint")

# GROQ call handler
def send_to_groq(data: dict, endpoint: str) -> str:
    try:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise EnvironmentError("GROQ_API_KEY not set in environment")
        
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-2.5-flash")
        prompt = build_prompt(data, endpoint)

        response = model.generate_content(prompt)

        return response.text
    except Exception as e:
        print(f"Error communicating with Groq: {e}")
        return "Sorry, there was an error processing your request."

# Generic handler
async def handle_request(request: Request, endpoint: str):
    try:
        data = await request.json()
        response_text = send_to_groq(data, endpoint)
        return JSONResponse(content={"message": response_text})
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/water")
async def water_endpoint(request: Request):
    return await handle_request(request, "water")

@app.post("/gym")
async def gym_endpoint(request: Request):
    return await handle_request(request, "gym")

@app.post("/food")
async def food_endpoint(request: Request):
    return await handle_request(request, "food")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
