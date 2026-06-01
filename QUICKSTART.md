# 🍽️ Restaurant AI Bot - Quick Reference

## 📋 Quick Start (Copy & Paste)

```bash
# Navigate to project
cd /Users/shivpratapsingh/Desktop/Restorent/restaurant-ai-bot

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env

# Edit .env and add your Groq API key
# GROQ_API_KEY=gsk_xxxxxxxxxxxxx

# Run application
streamlit run app.py
```

---

## 🔑 Getting Groq API Key (30 seconds)

1. Visit: https://console.groq.com/
2. Sign up (use Google/GitHub for quick signup)
3. Go to API Keys section
4. Click "Create API Key"
5. Copy the key
6. Paste in `.env` file: `GROQ_API_KEY=paste_here`

---

## 📁 Project Files (Quick Reference)

| File | Lines | Purpose |
|------|-------|---------|
| app.py | 800 | Main UI application |
| ai_helper.py | 450 | Groq API integration |
| recommender.py | 350 | Food recommendations |
| memory.py | 400 | User memory & analytics |
| styles.css | 300 | Dark theme |
| menu.csv | 25 | Menu items (24) |
| requirements.txt | 4 | Dependencies |

---

## 🎮 Application Tabs

| Tab | Features |
|-----|----------|
| 💬 **Chat** | Talk to AI assistant |
| 🍽️ **Menu** | Browse & filter items |
| ⭐ **Recommendations** | Smart suggestions |
| 📊 **Dashboard** | Analytics & stats |
| ❓ **FAQ** | Q&A & contact |

---

## 🛠️ Customization (Key Edits)

### Change Restaurant Info
**File:** app.py (line 70)
```python
st.info("""**Opening Hours:** 11 AM - 11 PM""")
```

### Add Menu Items
**File:** data/menu.csv
```csv
name,category,type,spicy_level,price,rating
Biryani,Main Course,Non-Veg,Medium,350,4.7
```

### Change Colors
**File:** assets/styles.css
```css
--primary-color: #ff6b35;  /* Change this */
--secondary-color: #004e89;
```

### Modify AI Behavior
**File:** utils/ai_helper.py
```python
def get_system_prompt():
    # Edit the prompt text here
```

---

## ⚡ Common Commands

```bash
# Activate virtual environment
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Deactivate virtual environment
deactivate

# List installed packages
pip list

# Update a package
pip install --upgrade streamlit

# Run on different port
streamlit run app.py --server.port 8502

# Run in headless mode
streamlit run app.py --headless

# Check if port is in use
lsof -i :8501  # macOS/Linux
netstat -ano | findstr :8501  # Windows
```

---

## 🚀 Deploy to Streamlit Cloud

1. Push to GitHub:
```bash
git init
git add .
git commit -m "Restaurant AI Bot"
git push origin main
```

2. Go to [share.streamlit.io](https://share.streamlit.io/)

3. Deploy:
   - Select repository
   - Set main file: `app.py`
   - Add secret: `GROQ_API_KEY=xxx`
   - Deploy!

---

## 🔧 Environment Variables (.env)

```
# Required
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxx

# Optional (these have defaults)
RESTAURANT_NAME=My Restaurant
GROQ_MODEL=mixtral-8x7b-32768
```

---

## 🐛 Quick Fixes

| Problem | Solution |
|---------|----------|
| API key not working | Check at console.groq.com, create new key |
| ModuleNotFoundError | Run: `pip install -r requirements.txt` |
| Port 8501 in use | Run: `streamlit run app.py --server.port 8502` |
| menu.csv not found | Check file exists: `ls data/menu.csv` |
| .env not recognized | Restart streamlit: `streamlit run app.py` |

---

## 📊 Menu Categories

Add items to `data/menu.csv`:

- **Starter**: Paneer Tikka, Samosa, etc.
- **Main Course**: Butter Chicken, Dal Makhani, etc.
- **Bread**: Naan, Paratha, etc.
- **Dessert**: Gulab Jamun, Kheer, etc.
- **Beverage**: Mango Lassi, Chai, etc.

---

## 🎯 User Preferences

Users can set (sidebar):
- **Food Type**: Veg / Non-Veg / Both
- **Spice Level**: Mild / Medium / Spicy
- **Budget**: Budget / Medium / Premium
- **Language**: English / Hindi

---

## 📈 Analytics Tracked

Dashboard shows:
- Total messages
- Recommendations given
- Favorite items
- Session duration
- Most popular dishes
- Preference breakdown

---

## 🌐 Available AI Models

In `.env`, set `GROQ_MODEL=`:

- `mixtral-8x7b-32768` (recommended, fast & good)
- `llama2-70b-4096` (more powerful)
- `gemma-7b-it` (lightweight)

---

## 📚 Documentation Files

1. **README.md** - Full documentation
2. **SETUP.md** - Installation guide
3. **DEPLOYMENT.md** - Deploy guide
4. **CODE_REFERENCE.md** - This file

---

## ✅ Pre-Launch Checklist

- [ ] Python 3.8+ installed
- [ ] Virtual environment created
- [ ] Dependencies installed
- [ ] .env file created with API key
- [ ] API key tested (works at console.groq.com)
- [ ] menu.csv exists
- [ ] All utility files present
- [ ] App starts: `streamlit run app.py`
- [ ] Can access http://localhost:8501
- [ ] Can type in chat

---

## 🆘 Emergency Contacts

- **Streamlit Issues**: https://discuss.streamlit.io/
- **Groq API Issues**: https://console.groq.com/
- **Python Help**: https://stackoverflow.com/

---

## 💡 Pro Tips

1. **Cache data** - Streamlit auto-caches, use @st.cache_data
2. **Rerun on changes** - Use st.rerun() after updates
3. **Session state** - Use st.session_state for persistence
4. **Secrets** - Never hardcode API keys, use .env
5. **Performance** - Optimize DataFrame operations
6. **UI/UX** - Use columns() for layout, tabs for sections
7. **Error handling** - Always wrap external API calls in try-catch

---

## 📞 File Sizes

- **app.py**: ~35 KB
- **ai_helper.py**: ~15 KB
- **recommender.py**: ~14 KB
- **memory.py**: ~17 KB
- **styles.css**: ~12 KB
- **menu.csv**: ~1 KB
- **Total Python**: ~2,000 lines
- **Total Project**: ~150 MB (with dependencies)

---

## 🎓 Learning Path

1. **Day 1**: Install, run, explore features
2. **Day 2**: Customize restaurant info & menu
3. **Day 3**: Understand code structure
4. **Day 4**: Deploy to Streamlit Cloud
5. **Day 5**: Share with team/customers

---

## 🎉 You're Ready!

```
✅ All files created
✅ All features implemented
✅ Full documentation provided
✅ Ready for production

Next: Run `streamlit run app.py`
```

---

**Version**: 1.0 | **Date**: May 2026 | **Status**: ✅ Production Ready
