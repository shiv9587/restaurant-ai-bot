# 🍽️ Restaurant AI Assistant Chatbot

A production-ready AI-powered restaurant chatbot built with Python and Streamlit. Features intelligent food recommendations, multi-language support, and a beautiful dark-themed UI.

## 🌟 Features

### 1. **Modern Chat Interface**
- Real-time chat with AI assistant
- Chat history persistence within session
- User-friendly message display
- Typing indicators and loading states

### 2. **AI-Powered Assistant**
- Powered by Groq API (fast and reliable)
- Context-aware responses
- Restaurant-specific knowledge
- Natural conversation flow

### 3. **Smart Food Recommendation Engine**
- Personalized recommendations based on:
  - Budget range (Budget/Medium/Premium)
  - Dietary preference (Veg/Non-Veg/Both)
  - Spice level preference (Mild/Medium/Spicy)
  - Food category
- Similar item suggestions
- Top-rated items
- Budget-friendly options

### 4. **User Memory & Preferences**
- Remember user name
- Store food preferences
- Track favorite items
- Maintain session history
- Export session data

### 5. **Menu Browser**
- Browse complete menu with filters
- Sort by category, price, or rating
- View detailed item information
- Mark favorites and dislikes

### 6. **FAQ Support**
- Common questions answered
- Restaurant information
- Delivery and reservation details
- Contact form integration

### 7. **Analytics Dashboard**
- Track total messages and recommendations
- View user preferences summary
- Monitor favorite items
- See most popular dishes
- Session duration tracking

### 8. **Multi-Language Support**
- English
- Hindi
- Easily extensible to more languages

### 9. **Custom Dark Theme**
- Professional dark UI
- Better eye comfort
- Modern color scheme
- Responsive design

## 📁 Project Structure

```
restaurant-ai-bot/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── README.md             # Project documentation
├── data/
│   └── menu.csv          # Restaurant menu data
├── utils/
│   ├── __init__.py       # Package initialization
│   ├── ai_helper.py      # Groq API integration
│   ├── recommender.py    # Food recommendation engine
│   └── memory.py         # User memory & analytics
├── assets/
│   └── styles.css        # Custom dark theme styling
└── screenshots/          # Application screenshots
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Groq API key (get it free from [console.groq.com](https://console.groq.com/))
- pip (Python package manager)

### 1. Clone/Download the Project

```bash
cd restaurant-ai-bot
```

### 2. Create Virtual Environment (Recommended)

```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the project root:

```bash
# From .env.example
cp .env.example .env
```

Edit `.env` and add your Groq API key:

```
GROQ_API_KEY=your_api_key_here
```

**Get Groq API Key:**
1. Go to [console.groq.com](https://console.groq.com/)
2. Sign up/Login with your account
3. Create an API key
4. Copy and paste it in `.env`

### 5. Run the Application

```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

## 💬 Usage Guide

### Chat Tab
- Ask anything about the menu, recommendations, or restaurant
- AI remembers conversation context
- View chat history in real-time

### Menu Browser Tab
- Browse all menu items
- Filter by category, type, or price
- Mark favorites and dislikes
- View detailed item information

### Recommendations Tab
- Get personalized recommendations
- Find budget-friendly options
- Browse top-rated items
- Find similar items

### Analytics Dashboard
- View session statistics
- Track preferences
- See favorite items
- Monitor most popular dishes

### FAQ Tab
- Read common questions
- Learn about opening hours, delivery, reservations
- Submit contact form

## 🎯 Customization Guide

### Adding Your Restaurant Info

Edit the **sidebar** section in `app.py`:

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

### Updating Menu Items

Edit `data/menu.csv` with your items:

```csv
name,category,type,spicy_level,price,rating
Your Dish Name,Main Course,Veg,Medium,250,4.5
```

Columns:
- `name`: Dish name
- `category`: Starter, Main Course, Bread, Dessert, Beverage
- `type`: Veg, Non-Veg
- `spicy_level`: Mild, Medium, Spicy
- `price`: Price in rupees
- `rating`: Rating 1-5

### Modifying AI System Prompt

Edit the `get_system_prompt()` function in `utils/ai_helper.py`:

```python
@staticmethod
def get_system_prompt(restaurant_name: str = "Our Restaurant") -> str:
    """Customize the AI behavior and personality here"""
```

### Customizing Theme Colors

Edit `assets/styles.css` and modify the color variables:

```css
:root {
    --primary-color: #ff6b35;        /* Orange */
    --secondary-color: #004e89;      /* Blue */
    --accent-color: #f7b801;         /* Yellow */
    --success-color: #00d4aa;        /* Green */
}
```

## 📦 API Models Available

Groq offers several models. Update in `.env`:

- `mixtral-8x7b-32768` - Default, fast and capable
- `llama2-70b-4096` - Powerful, good for complex tasks
- `gemma-7b-it` - Lightweight, quick responses

## 📊 Data & Analytics

The app automatically tracks:
- **Chat History**: All messages in current session
- **Recommendations**: Items recommended to user
- **User Preferences**: Saved dietary preferences
- **Analytics**: Total chats, popular items (stored in `analytics.json`)

## 🔐 Security Notes

- API keys are stored in `.env` file (not committed to Git)
- Environment variables loaded safely with python-dotenv
- No sensitive data stored locally
- Sessions are ephemeral (cleared on app restart)

## 🐛 Troubleshooting

### "GROQ_API_KEY not set"
- Create `.env` file with your API key
- Ensure file is in the project root
- Restart Streamlit: `streamlit run app.py`

### "ModuleNotFoundError"
- Activate virtual environment: `source venv/bin/activate`
- Install dependencies: `pip install -r requirements.txt`

### "FileNotFoundError: data/menu.csv"
- Ensure `menu.csv` exists in `data/` folder
- Check file path is correct

### Slow Responses
- Check internet connection
- Verify Groq API is working: [console.groq.com](https://console.groq.com/)
- Try different model in `.env`

### Streamlit Port Already in Use
```bash
streamlit run app.py --server.port 8502
```

## 🚀 Deployment

### Deploy on Streamlit Community Cloud

1. Push code to GitHub:
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/your-username/restaurant-ai-bot.git
git push -u origin main
```

2. Go to [share.streamlit.io](https://share.streamlit.io/)

3. Click "New app" and select your repository

4. Set the main file as `app.py`

5. Add environment variables in Streamlit settings:
   - Go to app settings
   - Add secret: `GROQ_API_KEY=your_key`

6. Deploy!

### Deploy on Other Platforms

**Heroku:**
```bash
heroku login
heroku create your-app-name
git push heroku main
```

**Railway:**
- Connect GitHub repo
- Add `GROQ_API_KEY` secret
- Deploy

**Docker:**
```dockerfile
FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["streamlit", "run", "app.py"]
```

## 📝 Sample Menu Format

The `menu.csv` file should follow this format:

| name | category | type | spicy_level | price | rating |
|------|----------|------|-------------|-------|--------|
| Paneer Tikka | Starter | Veg | Medium | 250 | 4.6 |
| Butter Chicken | Main Course | Non-Veg | Medium | 350 | 4.8 |
| Naan | Bread | Veg | Mild | 50 | 4.4 |

## 🤝 Contributing

Feel free to customize and extend the project:

1. Add more recommendation algorithms
2. Implement user authentication
3. Add order placement functionality
4. Integrate with payment systems
5. Add more languages
6. Create admin dashboard

## 📜 License

This project is open source and available under the MIT License.

## 💡 Tips & Tricks

1. **Personalization**: The app learns from user interactions and improves recommendations
2. **Favorites**: Users can build a favorite items list for quick ordering
3. **Analytics**: Track what items are popular to optimize your menu
4. **Multi-language**: Responses can be in Hindi by changing the language setting
5. **Context Memory**: AI remembers conversation context for better responses

## 📞 Support & Contact

For issues or questions:
1. Check the troubleshooting section
2. Review the code comments
3. Check Groq API documentation
4. Create an issue on GitHub

## 🎉 Credits

Built with:
- **Streamlit** - Web app framework
- **Groq** - Fast AI inference
- **Pandas** - Data analysis
- **Python** - Programming language

---

**Made with ❤️ for restaurants and food lovers**

Version: 1.0 | Last Updated: May 2026
