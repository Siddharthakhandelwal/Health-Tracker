# FastAPI Health Tracker: Workflow & Dataflow

## Workflow
1. **Client Request**: A client sends a POST request to one of the endpoints (`/water`, `/gym`, `/food`) with JSON data in the request body.
2. **API Receives Data**: FastAPI receives the request and parses the JSON payload.
3. **Processing**: The endpoint function calls a helper (`send_to_gen_ai`) to process or forward the data.
4. **Gen AI Integration**: The helper function (currently a placeholder) would send the data to the Gen AI API and receive a response.
5. **Response**: The API returns the Gen AI response (or a placeholder) to the client as JSON.

## Dataflow
```mermaid
graph TD
    Client["Client (e.g., test_api.py)"] -->|POST JSON| API["FastAPI Endpoint (/water, /gym, /food)"]
    API -->|Extracts JSON| Process["send_to_gen_ai Function"]
    Process -->|Sends to Gen AI API| GenAI["Gen AI API (external)"]
    GenAI -->|Returns response| Process
    Process -->|Returns response| API
    API -->|Returns JSON| Client
```

## Example Data
- `/water`: `{ "amount_liters": 2, "time": "2024-06-01T10:00:00" }`
- `/gym`: `{ "activity": "running", "duration_minutes": 45 }`
- `/food`: `{ "meal": "lunch", "calories": 600 }`

## Notes
- The Gen AI integration is currently a placeholder. Replace the helper with real API calls as needed.
- The endpoints are designed to be flexible for different health tracking data. 