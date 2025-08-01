# 🏥 Health Tracker API

A beginner-friendly health tracking application that provides personalized motivational advice for your water intake, gym activities, and food habits using Google's Gemini AI.

## 📖 What is this project?

The Health Tracker API is a web service (like a digital assistant) that helps you stay motivated with your health goals. You send it information about your daily activities, and it responds with personalized advice and encouragement.

**Think of it as your personal health coach that:**
- Reminds you to drink enough water based on your activity level
- Motivates you to keep up with your gym routine
- Gives you feedback on your eating habits

## ✨ Features

- 💧 **Water Tracking**: Get personalized hydration advice based on your weight and activity
- 🏋️ **Gym Motivation**: Receive workout encouragement and intensity suggestions
- 🍎 **Food Guidance**: Get nutritional feedback and healthy eating motivation
- 🤖 **AI-Powered**: Uses Google Gemini AI for intelligent, personalized responses
- 🔒 **Secure**: Your API key is stored safely in environment variables
- 🌐 **Cross-Platform**: Works with web browsers, mobile apps, and other applications
- ⚡ **Fast**: Built with FastAPI for quick response times

## 🔧 Prerequisites

Before you start, make sure you have:

1. **Python 3.9 or newer** installed on your computer
   - Check by opening Command Prompt/Terminal and typing: `python --version`
   - If you don't have Python, download it from [python.org](https://www.python.org/downloads/)

2. **Google Gemini API Key**
   - Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Sign in with your Google account
   - Click "Create API Key" and copy it (you'll need this later)

3. **Internet Connection** (required for AI responses)

4. **Text Editor** (like Notepad, VS Code, or any code editor)

## 📋 System Requirements

- **Operating System**: Windows, macOS, or Linux
- **RAM**: At least 2GB available
- **Storage**: 100MB free space
- **Python**: Version 3.9 or higher

## 🚀 Installation Guide

Follow these steps carefully - don't worry if you're new to programming!

### Step 1: Download the Project

If you have the project files already, skip to Step 2. Otherwise:

1. Download all project files to a folder on your computer
2. Make sure you have these files:
   - `main.py`
   - `requirements.txt`
   - `test_api.py`
   - `.env` (you might need to create this)

### Step 2: Open Command Prompt/Terminal

**On Windows:**
- Press `Windows key + R`
- Type `cmd` and press Enter

**On macOS:**
- Press `Cmd + Space`
- Type `Terminal` and press Enter

**On Linux:**
- Press `Ctrl + Alt + T`

### Step 3: Navigate to Your Project Folder

In the command prompt, type:
```bash
cd path/to/your/health-tracker-folder
```

Replace `path/to/your/health-tracker-folder` with the actual path where you saved the project files.

### Step 4: Create a Virtual Environment (Recommended)

This keeps your project dependencies separate from other Python projects:

```bash
python -m venv health-tracker-env
```

**Activate the virtual environment:**

**On Windows:**
```bash
health-tracker-env\Scripts\activate
```

**On macOS/Linux:**
```bash
source health-tracker-env/bin/activate
```

You should see `(health-tracker-env)` at the beginning of your command prompt.

### Step 5: Install Required Packages

```bash
pip install -r requirements.txt
```

This will install all the necessary software packages. It might take a few minutes.

## 🔐 Setting Up Your API Key

### Step 1: Create the .env File

In your project folder, create a file named `.env` (note the dot at the beginning).

**On Windows:**
- Right-click in the folder → New → Text Document
- Name it `.env` (delete the .txt extension)

**On macOS/Linux:**
- Use any text editor to create a file named `.env`

### Step 2: Add Your API Key

Open the `.env` file and add this line:

```
GEMINI_API_KEY=your_actual_api_key_here
```

Replace `your_actual_api_key_here` with the API key you got from Google AI Studio.

**Example:**
```
GEMINI_API_KEY=AIzaSyDCtqkcX4YzR8Y_LbcW1Y6PvdP184U9-rw
```

**⚠️ Important Security Notes:**
- Never share your API key with anyone
- Don't post it online or in public repositories
- The `.env` file should not be uploaded to GitHub or other code sharing sites

## 🏃‍♂️ Running the Application

### Step 1: Start the Server

In your command prompt (with the virtual environment activated), type:

```bash
python main.py
```

You should see output like:
```
INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

### Step 2: Test if it's Working

Open your web browser and go to:
- **Interactive API Documentation**: http://localhost:8000/docs
- **Alternative Documentation**: http://localhost:8000/redoc

If you see a webpage with API documentation, congratulations! Your server is running.

## 📡 API Endpoints

The Health Tracker has three main endpoints (think of them as different services):

### 1. 💧 Water Tracking - `/water`

**What it does:** Analyzes your water intake and gives hydration advice.

**How to use it:** Send a POST request with your water consumption data.

**Example data to send:**
```json
{
  "amount_liters": 2,
  "time": "2024-06-01T10:00:00"
}
```

**What you'll get back:**
```json
{
  "message": "Great hydration! Aim for 2.5L today. Keep sipping throughout the day for optimal health!"
}
```

### 2. 🏋️ Gym Tracking - `/gym`

**What it does:** Motivates you based on your workout routine.

**Example data to send:**
```json
{
  "activity": "running",
  "duration_minutes": 45
}
```

**What you'll get back:**
```json
{
  "message": "Excellent 45-min run! Keep this consistency. Add strength training twice weekly for balanced fitness."
}
```

### 3. 🍎 Food Tracking - `/food`

**What it does:** Analyzes your meals and provides nutritional guidance.

**Example data to send:**
```json
{
  "meal": "breakfast",
  "food": "i had a one glass of milk and bread in breakfast"
}
```

**What you'll get back:**
```json
{
  "message": "Good protein from milk! Add fruits or nuts to boost nutrition. Aim for 300-400 breakfast calories."
}
```

## 🧪 Testing Your API

The project includes a test script to make sure everything works correctly.

### Using the Test Script

1. Make sure your server is running (see "Running the Application" section)
2. Open a new command prompt/terminal window
3. Navigate to your project folder
4. Run the test:

```bash
python test_api.py
```

**Expected output:**
```
Response from /water: 200
{'message': 'Great hydration! Aim for 2.5L today. Keep sipping throughout the day for optimal health!'}
Response from /gym: 200
{'message': 'Excellent 45-min run! Keep this consistency. Add strength training twice weekly for balanced fitness.'}
Response from /food: 200
{'message': 'Good protein from milk! Add fruits or nuts to boost nutrition. Aim for 300-400 breakfast calories.'}
```

If you see status code `200` for all endpoints, everything is working perfectly!

### Manual Testing with Browser

You can also test using the interactive documentation:

1. Go to http://localhost:8000/docs
2. Click on any endpoint (like `/water`)
3. Click "Try it out"
4. Enter sample data in the request body
5. Click "Execute"
6. See the response below

## 🔧 Troubleshooting

### Common Issues and Solutions

#### 1. "Python is not recognized as an internal or external command"

**Problem:** Python is not installed or not in your system PATH.

**Solution:**
- Download Python from [python.org](https://www.python.org/downloads/)
- During installation, check "Add Python to PATH"
- Restart your command prompt

#### 2. "ModuleNotFoundError: No module named 'fastapi'"

**Problem:** Required packages are not installed.

**Solution:**
```bash
pip install -r requirements.txt
```

#### 3. "EnvironmentError: Gemini not set in environment"

**Problem:** Your API key is not properly configured.

**Solution:**
- Check that your `.env` file exists in the project folder
- Verify the API key is correct: `GEMINI_API_KEY=your_key_here`
- Make sure there are no extra spaces or quotes around the key

#### 4. "Address already in use" or "Port 8000 is already in use"

**Problem:** Another application is using port 8000.

**Solution:**
- Stop any other servers running on port 8000
- Or change the port in `main.py`: `uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)`

#### 5. API returns "Sorry, there was an error processing your request"

**Problem:** Issue with the Gemini AI service.

**Solutions:**
- Check your internet connection
- Verify your API key is valid and has quota remaining
- Check the Google AI Studio console for any restrictions

#### 6. "Connection refused" when testing

**Problem:** The server is not running.

**Solution:**
- Make sure you started the server with `python main.py`
- Check that you see "Uvicorn running on..." message
- Verify the server is running on http://localhost:8000

### Getting Help

If you're still having issues:

1. **Check the console output** for error messages
2. **Verify all files are in the correct location**
3. **Make sure your virtual environment is activated**
4. **Double-check your API key** in the `.env` file
5. **Try restarting the server** (Ctrl+C to stop, then `python main.py` to start)

## 🔒 Security Best Practices

### Protecting Your API Key

1. **Never commit `.env` to version control**
   - Add `.env` to your `.gitignore` file
   - Use environment variables in production

2. **Restrict API key permissions**
   - In Google AI Studio, limit your API key to only necessary services
   - Set usage quotas to prevent unexpected charges

3. **Use HTTPS in production**
   - The current setup allows all origins (`allow_origins=["*"]`)
   - In production, specify exact domains: `allow_origins=["https://yourdomain.com"]`

### Production Deployment

When deploying to a server:

1. **Set environment variables** instead of using `.env` files
2. **Use a reverse proxy** like Nginx
3. **Enable HTTPS** with SSL certificates
4. **Implement rate limiting** to prevent abuse
5. **Add authentication** for sensitive endpoints

## 📁 Project Structure

```
health-tracker/
├── main.py              # Main FastAPI application
├── requirements.txt     # Python dependencies
├── test_api.py         # Test script for all endpoints
├── .env                # Your API key (keep this secret!)
├── .gitignore          # Files to ignore in version control
└── README.md           # This documentation file
```

### File Descriptions

- **`main.py`**: The heart of the application containing all the API endpoints
- **`requirements.txt`**: Lists all Python packages needed to run the app
- **`test_api.py`**: Automated tests to verify everything works correctly
- **`.env`**: Stores your secret API key safely
- **`.gitignore`**: Tells Git which files not to upload (like your API key)

## 🚀 Advanced Usage

### Customizing Responses

You can modify the prompts in [`main.py`](main.py:22) to change how the AI responds:

- **Water prompt** (line 24-28): Modify hydration advice style
- **Gym prompt** (line 30-34): Change workout motivation approach  
- **Food prompt** (line 36-40): Adjust nutritional guidance tone

### Adding New Endpoints

To add a new health tracking category:

1. Add a new prompt in [`build_prompt()`](main.py:22)
2. Create a new endpoint function (similar to [`water_endpoint()`](main.py:72))
3. Add sample data to [`test_api.py`](test_api.py:6)

### Integration with Other Apps

This API can be integrated with:
- **Mobile apps** (React Native, Flutter)
- **Web applications** (React, Vue, Angular)
- **Desktop applications** (Electron, Tkinter)
- **IoT devices** (smart scales, fitness trackers)

## 📊 Example Use Cases

### 1. Morning Health Check-in

Send your overnight data:
```json
{
  "water": {"amount_liters": 0.5, "time": "morning"},
  "gym": {"activity": "planned", "duration_minutes": 0},
  "food": {"meal": "breakfast", "food": "oatmeal with berries"}
}
```

### 2. Post-Workout Analysis

Track your gym session:
```json
{
  "gym": {
    "activity": "weight training",
    "duration_minutes": 60,
    "intensity": "high",
    "exercises": ["squats", "bench press", "deadlifts"]
  }
}
```

### 3. Daily Nutrition Review

Log your complete meal:
```json
{
  "food": {
    "meal": "dinner",
    "food": "grilled chicken breast, quinoa, steamed broccoli, and a side salad",
    "estimated_calories": 650
  }
}
```

## 🔄 API Response Format

All endpoints return JSON in this format:

```json
{
  "message": "Your personalized advice here (25 words or less)"
}
```

**Response Codes:**
- `200`: Success - advice generated successfully
- `400`: Bad Request - invalid data format
- `500`: Server Error - issue with AI service or server

## 🎯 Tips for Best Results

### Water Tracking
- Include your weight and activity level for better hydration advice
- Mention the time of day for context-aware suggestions

### Gym Tracking  
- Be specific about exercises and duration
- Include intensity level (low, moderate, high)
- Mention your fitness goals

### Food Tracking
- Describe meals in detail for better calorie estimation
- Include portion sizes when possible
- Mention dietary restrictions or preferences

## 🤝 Contributing

Want to improve the Health Tracker? Here's how:

1. **Report bugs** by describing what went wrong
2. **Suggest features** for new health tracking categories
3. **Improve documentation** by clarifying confusing sections
4. **Test on different systems** and report compatibility issues

## 📄 License

This project is open source and available under the MIT License. You're free to use, modify, and distribute it.

## 👨‍💻 Author

**Siddhartha Khandelwal**  
Created with ❤️ for health-tech and AI enthusiasts.

---

## 🆘 Need More Help?

If you're still stuck after reading this guide:

1. **Double-check each step** in the installation guide
2. **Look at the error messages** - they often tell you exactly what's wrong
3. **Try the troubleshooting section** for common issues
4. **Test with the provided examples** before using your own data

Remember: Everyone starts somewhere! Don't be discouraged if it takes a few tries to get everything working. Programming is a skill that improves with practice.

**Happy health tracking! 🏃‍♀️💪**
