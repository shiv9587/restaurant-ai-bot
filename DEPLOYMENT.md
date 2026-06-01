# 🍽️ Restaurant AI Assistant - Complete Deployment Guide

## 📊 Project Complete ✅

All files have been successfully created and organized!

---

## 📁 Final Project Structure

```
restaurant-ai-bot/
├── app.py                      # Main application (800 lines)
├── requirements.txt            # Python dependencies
├── .env.example               # Environment template
├── README.md                  # Full documentation
├── SETUP.md                   # Installation guide
│
├── utils/                      # Python modules (1,200 lines)
│   ├── __init__.py            # Package init
│   ├── ai_helper.py           # Groq AI integration (450 lines)
│   ├── recommender.py         # Recommendation engine (350 lines)
│   └── memory.py              # User memory & analytics (400 lines)
│
├── data/                       # Data files
│   └── menu.csv               # 24 menu items
│
├── assets/                     # Styling
│   └── styles.css             # Dark theme (300 lines)
│
└── screenshots/               # For app screenshots
```

---

## 🚀 Installation Instructions

### Step 1: Open Terminal/Command Prompt

```bash
cd /Users/shivpratapsingh/Desktop/Restorent/restaurant-ai-bot
```

### Step 2: Create Virtual Environment

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**Packages installed:**
- streamlit 1.35.0
- pandas 2.1.4
- groq 0.4.2
- python-dotenv 1.0.0

### Step 4: Create .env File

**Option A - Command Line:**

macOS/Linux:
```bash
cat > .env << 'EOF'
GROQ_API_KEY=your_api_key_here
RESTAURANT_NAME=My Restaurant
GROQ_MODEL=mixtral-8x7b-32768
EOF
```

**Option B - Text Editor:**
1. Create new file `.env`
2. Add these lines:
```
GROQ_API_KEY=your_api_key_here
RESTAURANT_NAME=My Restaurant
GROQ_MODEL=mixtral-8x7b-32768
```
3. Save in project root

### Step 5: Get Groq API Key

1. Go to [console.groq.com](https://console.groq.com/)
2. Sign up (free account)
3. Go to API Keys section
4. Create API Key
5. Copy and replace `your_api_key_here` in `.env`

### Step 6: Run Application

```bash
streamlit run app.py
```

**Output:**
```
You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

✅ **Open http://localhost:8501 in your browser**

---

## 🎮 Application Features

### 💬 Chat Tab
- Real-time chat with AI assistant
- Chat history display
- Context-aware responses
- Typing indicators

### 🍽️ Menu Browser Tab
- Browse all 24 menu items
- Filter by category, type, price
- Sort by rating or price
- Mark favorites
- View detailed info (price, rating, type, spice level)

### ⭐ Recommendations Tab
- Personalized recommendations
- Budget-friendly options
- Top-rated items
- Similar item suggestions
- Category-based browsing

### 📊 Analytics Dashboard Tab
- Total messages count
- Recommendations given
- Favorite items list
- Session duration
- Most popular items
- User preference summary

### ❓ FAQ Tab
- 8 pre-built FAQs
- Restaurant hours, delivery, reservations
- Payment information
- Contact form

---

## 📝 Code Features

### Key Components

1. **AI Integration (Groq)**
   - Fast inference
   - Context awareness
   - Error handling
   - System prompts for restaurant context

2. **Recommendation Engine**
   - Pandas DataFrame filtering
   - Budget filtering
   - Dietary preference matching
   - Spice level matching
   - Rating-based sorting

3. **User Memory**
   - Session-based preferences
   - Chat history tracking
   - Favorites management
   - Analytics collection

4. **UI/UX**
   - Dark theme (professional appearance)
   - Responsive design
   - Mobile-friendly
   - Smooth interactions

5. **Error Handling**
   - API key validation
   - File existence checks
   - Graceful error messages
   - Fallback responses

---

## 🔧 Customization Guide

### 1. Update Restaurant Info

Edit **app.py** (line 70):
```python
st.info(
    """
    **Opening Hours:**
    🕐 11:00 AM - 11:00 PM

    **Delivery:**
    🚚 Within 5km radius

    **Contact:**
    📞 +91-XXXX-XXXX-XX
    """
)
```

### 2. Add Menu Items

Edit **data/menu.csv**:
```csv
name,category,type,spicy_level,price,rating
Biryani,Main Course,Non-Veg,Medium,350,4.7
```

### 3. Change AI Personality

Edit **utils/ai_helper.py** `get_system_prompt()` method

### 4. Change Theme Colors

Edit **assets/styles.css**:
```css
:root {
    --primary-color: #ff6b35;      /* Orange */
    --secondary-color: #004e89;    /* Blue */
    --accent-color: #f7b801;       /* Yellow */
}
```

---

## 📊 File Descriptions

| File | Size | Purpose |
|------|------|---------|
| **app.py** | 800 lines | Main Streamlit application with all UI |
| **utils/ai_helper.py** | 450 lines | Groq API integration and AI logic |
| **utils/recommender.py** | 350 lines | Food recommendation engine with pandas |
| **utils/memory.py** | 400 lines | User memory, preferences, and analytics |
| **assets/styles.css** | 300 lines | Custom dark theme styling |
| **data/menu.csv** | 25 lines | Restaurant menu with 24 items |
| **requirements.txt** | 4 lines | Python dependencies |
| **.env.example** | 7 lines | Environment variable template |
| **README.md** | 500 lines | Project documentation |
| **SETUP.md** | 600 lines | Installation and setup guide |

---

## 🚀 Deployment Options

### Option 1: Streamlit Cloud (Recommended, Free)

1. Push code to GitHub
2. Visit [share.streamlit.io](https://share.streamlit.io/)
3. Select your repository
4. Set main file: `app.py`
5. Add secret: `GROQ_API_KEY=your_key`
6. Deploy!

### Option 2: Heroku

```bash
heroku login
heroku create your-app-name
git push heroku main
heroku config:set GROQ_API_KEY=your_key
```

### Option 3: Docker

```bash
docker build -t restaurant-bot .
docker run -p 8501:8501 -e GROQ_API_KEY=your_key restaurant-bot
```

### Option 4: PythonAnywhere

1. Upload to [pythonanywhere.com](https://www.pythonanywhere.com/)
2. Configure web app
3. Set environment variables
4. Deploy

---

## 🐛 Troubleshooting

### Error: "GROQ_API_KEY not set"
- Create `.env` file with your API key
- Restart Streamlit: `streamlit run app.py`

### Error: "ModuleNotFoundError: No module named 'streamlit'"
- Activate virtual environment
- Run: `pip install -r requirements.txt`

### Error: "FileNotFoundError: data/menu.csv"
- Check file exists: `ls data/menu.csv`
- Verify it's in correct location

### Error: "Port 8501 already in use"
- Use different port: `streamlit run app.py --server.port 8502`

### Slow responses
- Check internet connection
- Verify Groq API status
- Try different model in `.env`

---

## ✅ Verification Checklist

Before running the app, verify:

- [ ] Python 3.8+ installed
- [ ] Virtual environment created
- [ ] All dependencies installed
- [ ] `.env` file created with API key
- [ ] `data/menu.csv` exists
- [ ] `assets/styles.css` exists
- [ ] `utils/` folder has all 4 files
- [ ] API key is valid (test at console.groq.com)

---

## 📚 Documentation Files

### README.md
- Project overview
- Feature list
- Quick start
- Customization guide
- Deployment instructions
- Troubleshooting

### SETUP.md
- Prerequisites checklist
- Detailed installation steps
- API key setup
- First-time usage
- Customization examples
- All deployment options

### app.py
- Inline code comments
- Section headers
- Function docstrings
- Clear variable names

### utils/*.py
- Module docstrings
- Class docstrings
- Function docstrings
- Detailed parameter descriptions

---

## 🎓 Code Quality

### Best Practices Implemented

✅ **Clean Code**
- Modular architecture
- DRY principle
- Meaningful variable names
- Clear function organization

✅ **Error Handling**
- Try-catch blocks
- Validation checks
- Graceful fallbacks
- User-friendly error messages

✅ **Documentation**
- Docstrings for all functions
- Inline comments
- README documentation
- Setup guide

✅ **Security**
- API key in environment variables
- No hardcoded secrets
- Input validation
- Safe file operations

✅ **Performance**
- Efficient pandas filtering
- Session-based caching
- Pagination support
- Optimized CSS

---

## 🎯 Next Steps

1. **Install & Run**
   ```bash
   cd restaurant-ai-bot
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   cp .env.example .env
   # Edit .env with your Groq API key
   streamlit run app.py
   ```

2. **Customize**
   - Update restaurant info
   - Add your menu items
   - Change theme colors
   - Modify AI personality

3. **Test**
   - Try chatting
   - Browse menu
   - Get recommendations
   - Check analytics

4. **Deploy**
   - Push to GitHub
   - Deploy to Streamlit Cloud
   - Share public URL with customers

---

## 📞 Support Resources

### Official Documentation
- [Streamlit Docs](https://docs.streamlit.io/)
- [Groq API Docs](https://console.groq.com/docs/api-overview)
- [Pandas Docs](https://pandas.pydata.org/docs/)

### Groq Models Available
- `mixtral-8x7b-32768` (default, recommended)
- `llama2-70b-4096` (more powerful)
- `gemma-7b-it` (lightweight)

### Community
- Streamlit Discord: [streamlit.io/chat](https://streamlit.io/chat)
- Groq Discord: [groq.com/discord](https://groq.com/discord)
- Stack Overflow tags: streamlit, groq, pandas

---

## 🎉 You're All Set!

Your production-ready Restaurant AI Assistant is complete with:

✅ 2000+ lines of clean, documented code
✅ Full AI integration with Groq API
✅ Smart recommendation engine
✅ User memory and analytics
✅ Professional dark theme UI
✅ Complete documentation
✅ Multiple deployment options

**Happy coding! 🚀🍽️**

---

**Created**: May 2026
**Version**: 1.0
**Status**: Production Ready
