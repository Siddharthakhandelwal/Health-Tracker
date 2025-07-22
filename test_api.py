import requests

BASE_URL = "http://localhost:8000"

endpoints = ["water", "gym", "food"]
sample_data = {
    "water": {"amount_liters": 2, "time": "2024-06-01T10:00:00"},
    "gym": {"activity": "running", "duration_minutes": 45},
    "food": {"meal": "lunch", "food": "i had a one glass of milk and bread in breakfast"}
}

for endpoint in endpoints:
    url = f"{BASE_URL}/{endpoint}"
    data = sample_data[endpoint]
    response = requests.post(url, json=data)
    print(f"Response from /{endpoint}: {response.status_code}")
    print(response.json()) 