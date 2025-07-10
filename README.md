Here's your `README.md` in proper Markdown format:

```markdown
# 🚀 Health Tracker API (Water, Gym & Food Motivation)

This is a **FastAPI-based backend** that provides **motivational health guidance** using Groq's LLMs. It analyzes input data for water intake, gym routines, and food habits, then returns short, personalized advice powered by a Groq-hosted model like `deepseek-r1-distill-llama-70b`.

---

## 🧠 Features

- 📦 Accepts structured health-related data as JSON
- 💬 Returns a short (≤ 25 words) motivational message
- 🔒 Reads API key securely from `.env`
- 🌐 CORS-enabled for use with mobile/web clients
- ⚡ Powered by LLMs from Groq API

---

## 📁 Project Structure

```

.
├── main.py              # FastAPI app with 3 endpoints: /water, /gym, /food
├── .env                 # Store your Groq API key securely (not tracked in Git)
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation

````

---

## ✅ Requirements

- Python 3.9 or newer
- Groq API key (get yours at [https://console.groq.com/](https://console.groq.com/))
- Internet connection (for LLM queries)

---

## 🔧 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/health-tracker-api.git
cd health-tracker-api
````

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
# Activate it:
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> Or manually:

```bash
pip install fastapi uvicorn groq python-dotenv
```

---

## 🔐 Setup `.env` File

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_groq_api_key_here
```

**Never commit your `.env` to GitHub.** Add `.env` to `.gitignore`.

---

## 🚀 Running the Server

Run the FastAPI development server with:

```bash
uvicorn main:app --reload
```

Once running, open:

* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🔄 Endpoints

### `POST /water`

Returns advice based on water intake data.

```json
{
  "weight": 70,
  "activity_level": "moderate"
}
```

---

### `POST /gym`

Returns advice based on gym performance data.

```json
{
  "days_attended": 4,
  "intensity": "high",
  "goal": "muscle gain"
}
```

---

### `POST /food`

Returns advice based on food intake data.

```json
{
  "meals": ["breakfast", "snack", "lunch"],
  "calories": 1800,
  "diet_type": "vegetarian"
}
```

---

## 🧪 Example with `curl` (on Windows CMD)

```cmd
curl -X POST http://127.0.0.1:8000/water -H "Content-Type: application/json" -d "{\"weight\": 70, \"activity_level\": \"moderate\"}"
```

On PowerShell or Linux/macOS:

```bash
curl -X POST http://127.0.0.1:8000/water -H "Content-Type: application/json" -d '{"weight": 70, "activity_level": "moderate"}'
```

---

## 💡 Future Improvements

* ✅ Add authentication
* 🩺 Add validation with Pydantic models
* 📊 Log health data for progress tracking
* 📱 Connect to mobile app or frontend

---

## 🛡️ License

MIT License

---

## 🙋‍♂️ Author

**Siddhartha Khandelwal**
Made with ❤️ for health-tech and AI.

```

Let me know if you'd like to include screenshots or API docs export!
```
