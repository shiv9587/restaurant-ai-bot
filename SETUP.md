# 🚀 Complete Installation & Setup Guide

## Project Overview

The **Restaurant AI Assistant** is a production-ready chatbot application with:
- AI-powered food recommendations
- Modern Streamlit web interface
- Dark theme UI
- Multi-language support
- Analytics dashboard
- Groq API integration

---

## 📋 Prerequisites

Before starting, ensure you have:
- **Python 3.8+** installed ([Download](https://www.python.org/downloads/))
- **pip** (comes with Python)
- **Groq API key** (free from [console.groq.com](https://console.groq.com/))
- A terminal/command prompt
- ~500MB free disk space

### Check Python Installation

```bash
python3 --version
pip --version
```

---

## 📁 Complete Project Structure

```
restaurant-ai-bot/
├── 📄 app.py                         # Main Streamlit application (500+ lines)
├── 📄 requirements.txt               # Dependencies list
├── 📄 .env.example                   # Environment variables template
├── 📄 README.md                      # Project documentation
├── 📄 SETUP.md                       # This setup guide
│
├── 📁 data/
│   └── 📊 menu.csv                   # Restaurant menu (24 items)
│
├── 📁 utils/
│   ├── 📄 __init__.py               # Python package marker
│   ├── 🤖 ai_helper.py              # Groq AI integration (450+ lines)
│   ├── 🍽️ recommender.py             # Food recommendation engine (350+ lines)
│   └── 💾 memory.py                  # User memory & analytics (400+ lines)
│
├── 📁 assets/
│   └── 🎨 styles.css                # Dark theme styling (300+ lines)
│
└── 📁 screenshots/                   # App screenshots (empty, for your use)
```

---

## ⚡ Quick Start (5 Minutes)

### Step 1: Navigate to Project
```bash
cd /Users/shivpratapsingh/Desktop/Restorent/restaurant-ai-bot
```

### Step 2: Create Virtual Environment
```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Setup Environment Variables
```bash
# Copy template
cp .env.example .env

# Edit .env and add your Groq API key
# GROQ_API_KEY=your_api_key_here
```

### Step 5: Run Application
```bash
streamlit run app.py
```

✅ **App opens at:** http://localhost:8501

---

## 🔐 Getting Groq API Key (Detailed Steps)

### Method 1: Direct Sign-up

1. **Visit** [console.groq.com](https://console.groq.com/)
2. **Click** "Sign Up" (top right)
3. **Enter** your email and create password
4. **Verify** your email
5. **Go to** API Keys section (left sidebar)
6. **Click** "Create API Key"
7. **Copy** your key (you won't see it again!)
8. **Paste** in `.env` file

### Method 2: GitHub Sign-up

1. **Visit** [console.groq.com](https://console.groq.com/)
2. **Click** "Sign Up with GitHub"
3. **Authorize** Groq to access your GitHub
4. **Go to** API Keys section
5. **Create** and **Copy** your key

---

## 📝 Creating .env File

### Option A: Command Line (Recommended)

**macOS/Linux:**
```bash
cat > .env << 'EOF'
GROQ_API_KEY=your_actual_api_key_here
RESTAURANT_NAME=My Restaurant
GROQ_MODEL=mixtral-8x7b-32768
EOF
```

**Windows:**
```cmd
echo GROQ_API_KEY=your_actual_api_key_here > .env
echo RESTAURANT_NAME=My Restaurant >> .env
echo GROQ_MODEL=mixtral-8x7b-32768 >> .env
```

### Option B: Text Editor

1. **Open** your text editor (VS Code, Notepad, etc.)
2. **Create** new file: `.env`
3. **Add** these lines:
```
GROQ_API_KEY=your_actual_api_key_here
RESTAURANT_NAME=My Restaurant
GROQ_MODEL=mixtral-8x7b-32768
```
4. **Save** in project root folder

### Option C: Rename Example File

```bash
cp .env.example .env
```
Then edit `.env` with your API key

---

## 🎯 Detailed Installation Steps

### Step 1: Verify Python

**macOS/Linux:**
```bash
which python3
python3 --version   # Should be 3.8 or higher
```

**Windows:**
```cmd
python --version    # Should be 3.8 or higher
```

### Step 2: Create Virtual Environment

**What is it?** A isolated Python workspace for this project (best practice)

**macOS/Linux:**
```bash
cd /Users/shivpratapsingh/Desktop/Restorent/restaurant-ai-bot

# Create virtual environment named 'venv'
python3 -m venv venv

# Activate it (you'll see (venv) in terminal)
source venv/bin/activate
```

**Windows:**
```cmd
cd C:\Users\YourUsername\Desktop\Restorent\restaurant-ai-bot

# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate
```

**Verify activation:**
```bash
which python    # Should show path with 'venv' in it
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**What gets installed:**
- `streamlit==1.35.0` - Web app framework
- `pandas==2.1.4` - Data handling
- `groq==0.4.2` - Groq API client
- `python-dotenv==1.0.0` - Environment variables

### Step 4: Configure .env

**Edit `.env` file:**
```
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxx   # Your actual key
RESTAURANT_NAME=The Food Palace          # Your restaurant name
GROQ_MODEL=mixtral-8x7b-32768           # AI model to use
```

**Important:**
- Never share your API key
- Never commit `.env` to Git
- Replace with actual key from Groq console

### Step 5: Verify Menu Data

Check that `data/menu.csv` exists:
```bash
ls data/menu.csv    # macOS/Linux
dir data\menu.csv   # Windows
```

Should show 24 items (Paneer Tikka to Masala Chai)

### Step 6: Run Application

```bash
streamlit run app.py
```

**Output should show:**
```
You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

---

## 🎮 First Time Using the App

### On First Run:

1. **Enter your name** in sidebar
2. **Select your preferences:**
   - Food type (Veg/Non-Veg/Both)
   - Spice level (Mild/Medium/Spicy)
   - Budget (Budget/Medium/Premium)

3. **Try these actions:**
   - 💬 Chat: "What do you recommend?"
   - 🍽️ Menu: Browse all items
   - ⭐ Recommendations: Get smart suggestions
   - 📊 Dashboard: View analytics
   - ❓ FAQ: Read common questions

---

## 🛠️ Customization Guide

### Customize Restaurant Info

**Edit `app.py` (around line 70):**

```python
st.info(
    """
    **Opening Hours:**
    🕐 11:00 AM - 11:00 PM

    **Delivery:**
    🚚 Within 5km radius
    ⏱️ 30-45 minutes

    **Contact:**
    📞 +91-XXXX-XXXX-XX
    📧 info@restaurant.com
    """
)
```

### Update Menu Items

**Edit `data/menu.csv`:**

```csv
name,category,type,spicy_level,price,rating
Margherita Pizza,Main Course,Veg,Mild,299,4.5
Tandoori Paneer,Starter,Veg,Medium,180,4.6
```

**Categories:** Starter, Main Course, Bread, Dessert, Beverage
**Types:** Veg, Non-Veg
**Spice:** Mild, Medium, Spicy
**Price:** Any number
**Rating:** 1.0 - 5.0

### Change Theme Colors

**Edit `assets/styles.css` (top section):**

```css
:root {
    --primary-color: #ff6b35;      /* Change orange */
    --secondary-color: #004e89;    /* Change blue */
    --accent-color: #f7b801;       /* Change yellow */
}
```

[Color picker tool](https://htmlcolorcodes.com/)

---

## 🚀 Deployment Options

### Option 1: Streamlit Community Cloud (Easiest)

**Steps:**
1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io/)
3. Click "New app"
4. Select your repository
5. Set main file to `app.py`
6. Add secret: `GROQ_API_KEY=your_key`
7. Deploy!

**Benefits:**
- ✅ Free hosting
- ✅ Auto-updates from GitHub
- ✅ Public URL

### Option 2: Heroku

**Install Heroku CLI:**
```bash
brew install heroku    # macOS
```

**Deploy:**
```bash
heroku login
heroku create your-app-name
git init
git add .
git commit -m "Initial commit"
git push heroku main
```

**Set environment variable:**
```bash
heroku config:set GROQ_API_KEY=your_key
```

### Option 3: Docker

**Create `Dockerfile`:**
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501"]
```

**Build and run:**
```bash
docker build -t restaurant-bot .
docker run -p 8501:8501 -e GROQ_API_KEY=your_key restaurant-bot
```

### Option 4: PythonAnywhere

1. Sign up at [pythonanywhere.com](https://www.pythonanywhere.com/)
2. Upload your code
3. Create web app
4. Set Python version to 3.10
5. Configure WSGI file

---

## 🐛 Troubleshooting

### Problem: "GROQ_API_KEY not set"

**Solution:**
```bash
# Check .env exists
ls .env                    # macOS/Linux
type .env                  # Windows

# Check format
cat .env                   # macOS/Linux
type .env                  # Windows

# Verify file content (should see: GROQ_API_KEY=gsk_...)
```

**If .env missing:**
```bash
cp .env.example .env
# Edit and add your key
```

### Problem: "ModuleNotFoundError: No module named 'streamlit'"

**Solution:**
```bash
# Verify venv is activated (should see (venv) in terminal)
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

### Problem: "FileNotFoundError: data/menu.csv"

**Solution:**
```bash
# Verify file exists
ls data/menu.csv           # macOS/Linux
dir data\menu.csv          # Windows

# If missing, recreate from data/menu.csv in this folder
```

### Problem: "Port 8501 already in use"

**Solution:**
```bash
# Run on different port
streamlit run app.py --server.port 8502
```

### Problem: Slow responses

**Solution:**
1. Check internet connection
2. Verify Groq API status
3. Try different model in `.env`:
   ```
   GROQ_MODEL=gemma-7b-it
   ```

### Problem: API key not working

**Solution:**
1. Check key in `.env` (no spaces)
2. Verify key at [console.groq.com](https://console.groq.com/)
3. Create new API key if needed
4. Restart Streamlit

---

## 📊 File Descriptions

### app.py (~800 lines)
Main application with:
- Streamlit UI components
- 5 main tabs (Chat, Menu, Recommendations, Dashboard, FAQ)
- Session state management
- User interaction handling

### utils/ai_helper.py (~450 lines)
AI integration:
- Groq API client initialization
- System prompts for restaurant assistant
- Context management
- Token estimation

### utils/recommender.py (~350 lines)
Food recommendation engine:
- Menu data loading (pandas)
- Filtering by preferences
- Similarity calculations
- Statistics generation

### utils/memory.py (~400 lines)
User memory & analytics:
- User preference storage
- Chat history tracking
- Analytics data collection
- Session export functionality

### assets/styles.css (~300 lines)
Dark theme styling:
- Color variables
- Component styling
- Animations
- Responsive design

### data/menu.csv
Sample menu with 24 items:
- 6 Starters
- 8 Main Courses
- 3 Breads
- 3 Desserts
- 4 Beverages

---

## 🎓 Learning Resources

### Streamlit Documentation
- [streamlit.io/docs](https://docs.streamlit.io/)
- Building apps
- Components reference

### Groq API Documentation
- [console.groq.com/docs](https://console.groq.com/docs/api-overview)
- Rate limits
- Model availability

### Pandas Documentation
- [pandas.pydata.org](https://pandas.pydata.org/docs/)
- DataFrame operations
- Data filtering

---

## 📝 Example Workflows

### Adding a New Menu Item

1. **Open** `data/menu.csv`
2. **Add** new line:
   ```
   Biryani,Main Course,Non-Veg,Medium,350,4.7
   ```
3. **Save** file
4. **Reload** app (Streamlit auto-reloads)

### Changing AI Personality

1. **Open** `utils/ai_helper.py`
2. **Find** `get_system_prompt()` method
3. **Edit** the prompt text
4. **Save** and reload

### Adding FAQ Entry

1. **Open** `app.py`
2. **Find** FAQ tab section (around line 650)
3. **Edit** `faqs` dictionary
4. **Save** and reload

---

## ✅ Verification Checklist

Before considering setup complete:

- [ ] Python 3.8+ installed
- [ ] Virtual environment created and activated
- [ ] All dependencies installed (`pip list` shows streamlit, pandas, groq)
- [ ] `.env` file created with GROQ_API_KEY
- [ ] Groq API key is valid and working
- [ ] `data/menu.csv` exists with items
- [ ] App starts without errors: `streamlit run app.py`
- [ ] Can access UI at http://localhost:8501
- [ ] Sidebar shows successfully
- [ ] Can type in chat input
- [ ] Recommendations tab works

---

## 🎉 You're Ready!

**Next steps:**
1. ✅ Customize restaurant info
2. ✅ Add your menu items
3. ✅ Deploy to Streamlit Cloud
4. ✅ Share with team/customers

---

## 📧 Support

If you encounter issues:
1. Check this guide's troubleshooting section
2. Review error messages carefully
3. Check Groq API console status
4. Verify all files exist with `ls` or `dir`
5. Test with fresh `.env` file

---

**Version: 1.0 | Created: May 2026**

Happy deploying! 🚀🍽️
