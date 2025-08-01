# 🚀 Health Tracker Setup Guide

A complete step-by-step setup guide for absolute beginners. No prior programming experience required!

## 📋 Pre-Installation Checklist

Before we start, make sure you have:

- [ ] A computer running Windows, macOS, or Linux
- [ ] Internet connection (required for downloads and AI responses)
- [ ] At least 2GB of free storage space
- [ ] Administrator/admin privileges on your computer
- [ ] A Google account (for getting the AI API key)
- [ ] 30-45 minutes of time to complete the setup

## 🎯 What We'll Install

1. **Python** - The programming language that runs our health tracker
2. **Project Files** - The health tracker application code
3. **Dependencies** - Additional software packages needed
4. **API Key** - Your personal key to access Google's AI service

## 🐍 Step 1: Install Python

Python is the programming language our health tracker uses. We need version 3.9 or newer.

### For Windows Users

#### Option A: Download from Python.org (Recommended)

1. **Visit the Python website**
   - Go to [https://www.python.org/downloads/](https://www.python.org/downloads/)
   - The website should automatically detect you're using Windows

2. **Download Python**
   - Click the big yellow "Download Python 3.x.x" button
   - This downloads the latest version (make sure it's 3.9 or higher)

3. **Run the installer**
   - Find the downloaded file (usually in your Downloads folder)
   - Double-click the file (it will be named something like `python-3.11.x-amd64.exe`)

4. **Important installation settings**
   - ✅ **CHECK** "Add Python to PATH" (this is crucial!)
   - ✅ **CHECK** "Install for all users" (if you have admin rights)
   - Click "Install Now"

5. **Wait for installation**
   - The installer will download and install Python
   - This may take 5-10 minutes

6. **Verify installation**
   - Press `Windows key + R`
   - Type `cmd` and press Enter
   - In the black window that opens, type: `python --version`
   - You should see something like `Python 3.11.5`

#### Option B: Microsoft Store (Alternative)

1. Open Microsoft Store
2. Search for "Python 3.11" or "Python 3.12"
3. Click "Get" to install
4. This automatically adds Python to PATH

### For macOS Users

#### Option A: Download from Python.org (Recommended)

1. **Visit the Python website**
   - Go to [https://www.python.org/downloads/](https://www.python.org/downloads/)
   - Click "Download Python 3.x.x for macOS"

2. **Run the installer**
   - Open the downloaded `.pkg` file
   - Follow the installation wizard
   - Enter your password when prompted

3. **Verify installation**
   - Press `Cmd + Space` to open Spotlight
   - Type "Terminal" and press Enter
   - In the terminal, type: `python3 --version`
   - You should see something like `Python 3.11.5`

#### Option B: Using Homebrew (For Advanced Users)

If you have Homebrew installed:
```bash
brew install python@3.11
```

### For Linux Users

#### Ubuntu/Debian:
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

#### CentOS/RHEL/Fedora:
```bash
sudo dnf install python3 python3-pip
# or for older versions:
sudo yum install python3 python3-pip
```

#### Verify installation:
```bash
python3 --version
```

## 📁 Step 2: Download Project Files

### Option A: Download ZIP File

1. **Get the project files**
   - If you received a ZIP file, extract it to a folder like:
     - Windows: `C:\Users\YourName\health-tracker`
     - macOS: `/Users/YourName/health-tracker`
     - Linux: `/home/yourusername/health-tracker`

2. **Verify you have these files:**
   - `main.py` (the main application)
   - `requirements.txt` (list of needed packages)
   - `test_api.py` (testing script)
   - `README.md` (documentation)

### Option B: Create Files Manually

If you need to create the files yourself:

1. **Create a new folder**
   - Name it `health-tracker`
   - Place it in an easy-to-find location

2. **Create the main files**
   - You'll need to create `main.py`, `requirements.txt`, and `test_api.py`
   - Copy the content from the existing project files

## 🖥️ Step 3: Open Command Line/Terminal

### Windows - Command Prompt

**Method 1: Using Windows Key**
1. Press `Windows key + R`
2. Type `cmd` and press Enter

**Method 2: Using Start Menu**
1. Click the Start button
2. Type "Command Prompt"
3. Click on "Command Prompt" when it appears

**Method 3: Using File Explorer**
1. Open File Explorer
2. Navigate to your health-tracker folder
3. Hold Shift and right-click in the folder
4. Select "Open PowerShell window here" or "Open command window here"

### macOS - Terminal

**Method 1: Using Spotlight**
1. Press `Cmd + Space`
2. Type "Terminal"
3. Press Enter

**Method 2: Using Finder**
1. Open Finder
2. Go to Applications → Utilities
3. Double-click Terminal

### Linux - Terminal

**Method 1: Keyboard Shortcut**
- Press `Ctrl + Alt + T`

**Method 2: Using Application Menu**
- Look for "Terminal" in your applications menu

## 📂 Step 4: Navigate to Your Project Folder

In your command line/terminal, you need to navigate to where you saved the health tracker files.

### Find Your Folder Path

**Windows:**
- If your folder is at `C:\Users\YourName\health-tracker`
- Type: `cd C:\Users\YourName\health-tracker`

**macOS:**
- If your folder is at `/Users/YourName/health-tracker`
- Type: `cd /Users/YourName/health-tracker`

**Linux:**
- If your folder is at `/home/yourusername/health-tracker`
- Type: `cd /home/yourusername/health-tracker`

### Verify You're in the Right Place

Type this command to see the files in your current folder:

**Windows:**
```cmd
dir
```

**macOS/Linux:**
```bash
ls
```

You should see files like `main.py`, `requirements.txt`, etc.

## 🏠 Step 5: Create Virtual Environment (Recommended)

A virtual environment keeps your project's packages separate from other Python projects.

### Create the Virtual Environment

**Windows:**
```cmd
python -m venv health-tracker-env
```

**macOS/Linux:**
```bash
python3 -m venv health-tracker-env
```

### Activate the Virtual Environment

**Windows:**
```cmd
health-tracker-env\Scripts\activate
```

**macOS/Linux:**
```bash
source health-tracker-env/bin/activate
```

### Verify Activation

You should see `(health-tracker-env)` at the beginning of your command prompt, like this:
```
(health-tracker-env) C:\Users\YourName\health-tracker>
```

## 📦 Step 6: Install Required Packages

Now we'll install all the software packages our health tracker needs.

### Install Packages

```bash
pip install -r requirements.txt
```

### What This Installs

- **FastAPI** - Web framework for creating the API
- **Uvicorn** - Web server to run the application
- **Google Generative AI** - For connecting to Google's AI service
- **Python-dotenv** - For managing environment variables
- **Requests** - For making HTTP requests (used in testing)

### Verify Installation

```bash
pip list
```

You should see a list of installed packages including fastapi, uvicorn, google-generativeai, etc.

## 🔑 Step 7: Get Your Google Gemini API Key

### Create Google AI Studio Account

1. **Visit Google AI Studio**
   - Go to [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
   - Sign in with your Google account

2. **Create API Key**
   - Click "Create API Key"
   - Choose "Create API key in new project" (recommended)
   - Copy the generated key (it looks like: `AIzaSyDCtqkcX4YzR8Y_LbcW1Y6PvdP184U9-rw`)

3. **Save Your Key Safely**
   - Write it down or save it in a secure note
   - You'll need this in the next step

### Important Notes About API Keys

- **Free Tier**: Google provides free usage up to certain limits
- **Keep it Secret**: Never share your API key publicly
- **Usage Limits**: Monitor your usage in Google AI Studio
- **Billing**: Set up billing alerts if you plan heavy usage

## 📄 Step 8: Create Environment File

### Create .env File

You need to create a special file to store your API key securely.

**Windows:**
1. In your project folder, right-click and select "New" → "Text Document"
2. Name it `.env` (delete the `.txt` extension)
3. If Windows asks about changing the file extension, click "Yes"

**macOS:**
1. In Terminal (while in your project folder), type: `touch .env`
2. Or use any text editor to create a file named `.env`

**Linux:**
1. In Terminal (while in your project folder), type: `touch .env`
2. Or use any text editor to create a file named `.env`

### Add Your API Key

1. **Open the .env file**
   - Use Notepad (Windows), TextEdit (macOS), or any text editor
   - The file should be completely empty

2. **Add this line:**
   ```
   GEMINI_API_KEY=your_actual_api_key_here
   ```

3. **Replace with your real key:**
   ```
   GEMINI_API_KEY=AIzaSyDCtqkcX4YzR8Y_LbcW1Y6PvdP184U9-rw
   ```

4. **Save the file**
   - Make sure there are no extra spaces or quotes
   - The file should contain only that one line

### Security Reminder

- ⚠️ Never upload this file to GitHub or share it publicly
- ⚠️ The `.env` file should stay on your computer only
- ⚠️ If you accidentally share it, generate a new API key immediately

## 🏃‍♂️ Step 9: Run the Health Tracker

### Start the Server

In your command line (with virtual environment activated), type:

**Windows:**
```cmd
python main.py
```

**macOS/Linux:**
```bash
python3 main.py
```

### Expected Output

You should see something like this:
```
INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

### Success Indicators

- ✅ No error messages
- ✅ "Uvicorn running on..." message appears
- ✅ Server doesn't immediately stop

## 🧪 Step 10: Test Your Installation

### Test in Web Browser

1. **Open your web browser**
2. **Go to:** `http://localhost:8000/docs`
3. **You should see:** Interactive API documentation page

### Test with Provided Script

1. **Open a NEW command line window** (keep the server running in the first one)
2. **Navigate to your project folder** (repeat Step 4)
3. **Activate virtual environment** (repeat Step 5)
4. **Run the test:**
   ```bash
   python test_api.py
   ```

### Expected Test Results

```
Response from /water: 200
{'message': 'Great hydration! Aim for 2.5L today. Keep sipping throughout the day for optimal health!'}
Response from /gym: 200
{'message': 'Excellent 45-min run! Keep this consistency. Add strength training twice weekly for balanced fitness.'}
Response from /food: 200
{'message': 'Good protein from milk! Add fruits or nuts to boost nutrition. Aim for 300-400 breakfast calories.'}
```

## 🎉 Congratulations!

If you see the test results above, your Health Tracker is working perfectly!

## 🔧 Troubleshooting Common Issues

### Issue 1: "Python is not recognized"

**Problem:** Windows can't find Python
**Solution:**
1. Reinstall Python and check "Add Python to PATH"
2. Or manually add Python to PATH:
   - Search "Environment Variables" in Windows
   - Edit "Path" variable
   - Add Python installation folder

### Issue 2: "No module named 'fastapi'"

**Problem:** Packages not installed
**Solution:**
```bash
pip install -r requirements.txt
```

### Issue 3: "Permission denied"

**Problem:** Don't have permission to install packages
**Solution:**
- **Windows:** Run Command Prompt as Administrator
- **macOS/Linux:** Use `sudo` before commands (be careful!)

### Issue 4: "Port 8000 already in use"

**Problem:** Another program is using port 8000
**Solution:**
1. Find and stop the other program
2. Or change port in `main.py`:
   ```python
   uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
   ```

### Issue 5: "API key not found"

**Problem:** .env file not created correctly
**Solution:**
1. Check `.env` file exists in project folder
2. Verify format: `GEMINI_API_KEY=your_key_here`
3. No spaces around the equals sign
4. No quotes around the key

### Issue 6: "Connection timeout" or AI errors

**Problem:** Network or API issues
**Solution:**
1. Check internet connection
2. Verify API key is valid
3. Check Google AI Studio for quota limits
4. Try again in a few minutes

## 🔄 Daily Usage

### Starting the Health Tracker

1. **Open command line**
2. **Navigate to project folder:** `cd path/to/health-tracker`
3. **Activate virtual environment:**
   - Windows: `health-tracker-env\Scripts\activate`
   - macOS/Linux: `source health-tracker-env/bin/activate`
4. **Start server:** `python main.py`

### Stopping the Health Tracker

- Press `Ctrl + C` in the command line where the server is running

### Quick Start Script (Advanced)

Create a batch file (Windows) or shell script (macOS/Linux) to automate startup:

**Windows (start_health_tracker.bat):**
```batch
@echo off
cd /d "C:\path\to\your\health-tracker"
call health-tracker-env\Scripts\activate
python main.py
pause
```

**macOS/Linux (start_health_tracker.sh):**
```bash
#!/bin/bash
cd /path/to/your/health-tracker
source health-tracker-env/bin/activate
python3 main.py
```

## 📱 IDE/Editor Recommendations

### For Beginners
- **Visual Studio Code** (Free, user-friendly)
  - Download: [https://code.visualstudio.com/](https://code.visualstudio.com/)
  - Install Python extension
- **PyCharm Community** (Free, powerful)
  - Download: [https://www.jetbrains.com/pycharm/](https://www.jetbrains.com/pycharm/)

### For Advanced Users
- **Sublime Text** (Fast, lightweight)
- **Atom** (Customizable)
- **Vim/Neovim** (Terminal-based)

## 🔄 Updating the Health Tracker

### Update Python Packages
```bash
pip install --upgrade -r requirements.txt
```

### Update Python Itself
- Download latest version from python.org
- Install over existing installation

## 🆘 Getting Additional Help

### Documentation Resources
- **Python Official Tutorial:** [https://docs.python.org/3/tutorial/](https://docs.python.org/3/tutorial/)
- **FastAPI Documentation:** [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)
- **Google AI Studio Help:** [https://ai.google.dev/](https://ai.google.dev/)

### Community Support
- **Stack Overflow:** Search for specific error messages
- **Reddit:** r/learnpython, r/Python
- **Discord:** Python community servers

### Before Asking for Help
1. **Copy the exact error message**
2. **Describe what you were trying to do**
3. **Mention your operating system**
4. **Include your Python version** (`python --version`)

## 🎯 Next Steps

Once your Health Tracker is running:

1. **Read the [API_GUIDE.md](API_GUIDE.md)** to understand all endpoints
2. **Check [EXAMPLES.md](EXAMPLES.md)** for practical usage examples
3. **Review [ARCHITECTURE.md](ARCHITECTURE.md)** to understand how it works
4. **Start tracking your health data!**

---

**🎉 Welcome to your personal Health Tracker! You've successfully set up a powerful AI-powered health monitoring system. Happy tracking!**