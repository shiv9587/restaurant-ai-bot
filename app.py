"""
Restaurant AI Assistant Chatbot - Main Application
A production-ready Streamlit chatbot with AI-powered recommendations and chat interface.
"""

import streamlit as st
import pandas as pd
from datetime import datetime
import os
from pathlib import Path

# Import custom modules
from utils.ai_helper import AIAssistant, ContextManager
from utils.recommender import FoodRecommender
from utils.memory import UserMemory, AnalyticsTracker

# Configure Streamlit page
st.set_page_config(
    page_title="Restaurant AI Assistant",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
def load_css():
    """Load custom CSS styling."""
    css_path = Path("assets/styles.css")
    if css_path.exists():
        with open(css_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Initialize session state
def initialize_session_state():
    """Initialize all session state variables."""
    if "user_memory" not in st.session_state:
        st.session_state.user_memory = UserMemory()

    if "ai_assistant" not in st.session_state:
        try:
            st.session_state.ai_assistant = AIAssistant()
        except ValueError as e:
            st.session_state.ai_assistant = None
            st.error(f"⚠️ {str(e)}")

    if "recommender" not in st.session_state:
        try:
            st.session_state.recommender = FoodRecommender("data/menu.csv")
        except FileNotFoundError:
            st.error("❌ Menu file not found at data/menu.csv")
            st.session_state.recommender = None

    if "context_manager" not in st.session_state:
        st.session_state.context_manager = ContextManager()

    if "analytics" not in st.session_state:
        st.session_state.analytics = AnalyticsTracker()

    if "language" not in st.session_state:
        st.session_state.language = "English"

    if "chat_active" not in st.session_state:
        st.session_state.chat_active = False

initialize_session_state()

# ============= SIDEBAR =============
with st.sidebar:
    st.title("🍽️ Restaurant AI Assistant")
    st.divider()

    # User Profile Section
    st.subheader("👤 Your Profile")
    user_name = st.text_input(
        "Your Name",
        value=st.session_state.user_memory.get_user_name(),
        placeholder="Enter your name"
    )
    if user_name and user_name != "Guest":
        st.session_state.user_memory.set_user_name(user_name)

    # Preferences Section
    st.subheader("🎯 Your Preferences")

    veg_pref = st.selectbox(
        "Food Type Preference",
        ["Both", "Veg", "Non-Veg"],
        index=["Both", "Veg", "Non-Veg"].index(
            st.session_state.user_memory.get_veg_preference()
        )
    )
    st.session_state.user_memory.set_veg_preference(veg_pref)

    spice_pref = st.selectbox(
        "Spice Level Preference",
        ["Mild", "Medium", "Spicy"],
        index=["Mild", "Medium", "Spicy"].index(
            st.session_state.user_memory.get_spicy_preference()
        )
    )
    st.session_state.user_memory.set_spicy_preference(spice_pref)

    budget_pref = st.selectbox(
        "Budget Range",
        ["Budget", "Medium", "Premium"],
        index=["Budget", "Medium", "Premium"].index(
            st.session_state.user_memory.get_budget_range()
        )
    )
    st.session_state.user_memory.set_budget_range(budget_pref)

    # Language Selection
    st.subheader("🌐 Language")
    language = st.selectbox(
        "Choose Language",
        ["English", "Hindi"],
        index=0 if st.session_state.language == "English" else 1
    )
    st.session_state.language = language

    st.divider()

    # Quick Actions
    st.subheader("⚡ Quick Actions")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Clear Chat", use_container_width=True):
            st.session_state.user_memory.clear_chat_history()
            st.success("Chat cleared!")

    with col2:
        if st.button("📊 Analytics", use_container_width=True):
            st.session_state.show_analytics = True

    # Restaurant Info
    st.divider()
    st.subheader("📞 Contact & Hours")
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

    st.divider()
    st.caption("Powered by Groq AI | v1.0")

# ============= MAIN CONTENT =============
def main():
    """Main application logic."""

    # Page title
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.title("🍽️ Restaurant AI Assistant")
        st.markdown("<p style='text-align: center; color: #ff6b35;'>Your Personal Food Recommendation Expert</p>", 
                   unsafe_allow_html=True)

    st.divider()

    # Check if AI Assistant is available
    if st.session_state.ai_assistant is None:
        st.error(
            """
            ❌ **Configuration Error**
            
            The GROQ_API_KEY environment variable is not set.
            Please add your Groq API key to the .env file.
            """
        )
        st.info(
            """
            **To fix this:**
            1. Create a .env file in the project root
            2. Add: GROQ_API_KEY=your_api_key_here
            3. Restart the Streamlit app
            """
        )
        return

    if st.session_state.recommender is None:
        st.error("❌ Menu file not found. Please ensure data/menu.csv exists.")
        return

    # Create tabs for different features
    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["💬 Chat", "🍽️ Menu Browser", "⭐ Recommendations", "📊 Dashboard", "ℹ️ FAQ"]
    )

    # ============= TAB 1: CHAT =============
    with tab1:
        st.subheader("💬 Chat with Assistant")

        # Display chat history
        chat_container = st.container(height=500)
        with chat_container:
            if st.session_state.user_memory.chat_history:
                for message in st.session_state.user_memory.get_chat_history():
                    role = message["role"]
                    content = message["content"]

                    if role == "user":
                        with st.chat_message("user"):
                            st.write(content)
                    else:
                        with st.chat_message("assistant"):
                            st.write(content)
            else:
                st.info("👋 Start chatting! Ask me about our menu, recommendations, or anything about the restaurant.")

        st.divider()

        # Chat input
        user_input = st.chat_input(
            "Ask me anything about our menu, recommendations, or restaurant...",
            key="chat_input"
        )

        if user_input:
            # Add user message to history
            st.session_state.user_memory.add_chat_message("user", user_input)

            # Get AI response
            with st.spinner("🤖 Thinking..."):
                ai_response = st.session_state.ai_assistant.chat(
                    user_input,
                    st.session_state.user_memory.get_chat_history_for_ai()
                )

            # Add AI response to history
            st.session_state.user_memory.add_chat_message("assistant", ai_response)
            st.session_state.analytics.record_chat()

            # Rerun to update chat display
            st.rerun()

    # ============= TAB 2: MENU BROWSER =============
    with tab2:
        st.subheader("🍽️ Menu Browser")

        # Menu filters
        col1, col2, col3 = st.columns(3)

        with col1:
            category = st.selectbox(
                "Select Category",
                ["All"] + st.session_state.recommender.get_categories()
            )

        with col2:
            veg_filter = st.selectbox(
                "Filter by Type",
                ["Both", "Veg", "Non-Veg"]
            )

        with col3:
            sort_by = st.selectbox(
                "Sort By",
                ["Rating (High to Low)", "Price (Low to High)", "Price (High to Low)"]
            )

        # Get filtered menu
        menu_df = st.session_state.recommender.get_menu()

        if category != "All":
            menu_df = menu_df[menu_df["category"] == category]

        if veg_filter != "Both":
            menu_df = menu_df[menu_df["type"] == veg_filter]

        # Sort menu
        if "Rating" in sort_by:
            menu_df = menu_df.sort_values("rating", ascending=False)
        elif "Price (Low" in sort_by:
            menu_df = menu_df.sort_values("price", ascending=True)
        else:
            menu_df = menu_df.sort_values("price", ascending=False)

        # Display menu items
        if not menu_df.empty:
            for idx, (_, item) in enumerate(menu_df.iterrows()):
                col1, col2 = st.columns([3, 1])

                with col1:
                    st.write(f"### {item['name']}")
                    col_a, col_b, col_c = st.columns(3)

                    with col_a:
                        st.caption(f"Category: {item['category']}")
                    with col_b:
                        st.caption(f"Type: {item['type']}")
                    with col_c:
                        st.caption(f"Spice: {item['spicy_level']}")

                with col2:
                    st.write(f"### ₹{item['price']}")
                    st.write(f"⭐ {item['rating']}")

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("❤️ Add to Favorites", key=f"fav_{idx}"):
                        st.session_state.user_memory.add_to_favorites(item['name'])
                        st.success(f"Added {item['name']} to favorites!")

                with col2:
                    if st.button("👎 Dislike", key=f"dislike_{idx}"):
                        st.session_state.user_memory.add_to_disliked(item['name'])
                        st.info(f"Noted: You dislike {item['name']}")

                st.divider()
        else:
            st.warning("No items found matching your filters.")

    # ============= TAB 3: RECOMMENDATIONS =============
    with tab3:
        st.subheader("⭐ Smart Recommendations")

        recommendation_type = st.selectbox(
            "Select Recommendation Type",
            [
                "Based on Your Preferences",
                "Budget-Friendly",
                "Top Rated Items",
                "By Category",
                "Similar to Item"
            ]
        )

        if recommendation_type == "Based on Your Preferences":
            st.info("🎯 Recommendations based on your saved preferences")

            if st.button("Get Personalized Recommendations"):
                with st.spinner("Finding perfect items for you..."):
                    recommendations = st.session_state.recommender.recommend_by_preferences(
                        veg_preference=st.session_state.user_memory.get_veg_preference(),
                        spicy_preference=st.session_state.user_memory.get_spicy_preference(),
                        budget_range=st.session_state.user_memory.get_budget_range(),
                        limit=5
                    )

                    if not recommendations.empty:
                        for _, item in recommendations.iterrows():
                            st.success(f"✨ {item['name']} - ₹{item['price']} ⭐ {item['rating']}")
                            st.caption(f"{item['category']} | {item['type']} | {item['spicy_level']}")
                            st.session_state.user_memory.add_recommendation(
                                item['name'],
                                "Based on your preferences"
                            )
                            st.session_state.analytics.record_recommendation(item['name'])
                            st.divider()

        elif recommendation_type == "Budget-Friendly":
            budget_amount = st.slider("Maximum Budget (₹)", 50, 500, 200)

            if st.button("Find Budget Items"):
                with st.spinner("Searching for affordable options..."):
                    recommendations = st.session_state.recommender.recommend_by_budget(
                        budget_amount,
                        limit=5
                    )

                    if not recommendations.empty:
                        for _, item in recommendations.iterrows():
                            st.success(f"💰 {item['name']} - ₹{item['price']} ⭐ {item['rating']}")
                            st.caption(f"{item['category']} | {item['type']}")

        elif recommendation_type == "Top Rated Items":
            if st.button("Show Top Rated"):
                with st.spinner("Loading top items..."):
                    recommendations = st.session_state.recommender.get_top_rated_items(limit=10)

                    for _, item in recommendations.iterrows():
                        st.success(f"⭐ {item['name']} - {item['rating']} rating (₹{item['price']})")

        elif recommendation_type == "By Category":
            category = st.selectbox("Choose Category", st.session_state.recommender.get_categories())

            if st.button("Get Items"):
                with st.spinner("Loading items..."):
                    recommendations = st.session_state.recommender.get_items_by_category(category)

                    if not recommendations.empty:
                        for _, item in recommendations.iterrows():
                            st.info(f"🍽️ {item['name']} - ₹{item['price']} ⭐ {item['rating']}")

        elif recommendation_type == "Similar to Item":
            item_name = st.selectbox(
                "Choose Item",
                st.session_state.recommender.get_menu()['name'].tolist()
            )

            if st.button("Find Similar Items"):
                with st.spinner("Finding similar items..."):
                    recommendations = st.session_state.recommender.recommend_similar(item_name, limit=5)

                    if not recommendations.empty:
                        for _, item in recommendations.iterrows():
                            st.info(f"🔄 {item['name']} - ₹{item['price']} ⭐ {item['rating']}")
                    else:
                        st.warning("No similar items found.")

    # ============= TAB 4: ANALYTICS DASHBOARD =============
    with tab4:
        st.subheader("📊 Analytics Dashboard")

        # Session Statistics
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Total Messages", len(st.session_state.user_memory.chat_history))

        with col2:
            st.metric("Recommendations Given", st.session_state.user_memory.get_recommendations_count())

        with col3:
            favorites = len(st.session_state.user_memory.get_favorites())
            st.metric("Favorite Items", favorites)

        with col4:
            session_duration = st.session_state.user_memory.get_session_duration()
            st.metric("Session Duration", f"{int(session_duration//60)}m {int(session_duration%60)}s")

        st.divider()

        # Preferences Summary
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Your Preferences")
            prefs = st.session_state.user_memory.get_all_preferences()
            preferences_data = {
                "Veg Preference": prefs.get("veg_preference", "Not set"),
                "Spice Level": prefs.get("spicy_preference", "Not set"),
                "Budget Range": prefs.get("budget_range", "Not set"),
            }
            st.table(pd.DataFrame(preferences_data.items(), columns=["Preference", "Value"]))

        with col2:
            st.subheader("📈 Chat Statistics")
            stats = st.session_state.analytics.get_analytics_summary()
            analytics_data = {
                "Total Chats": stats["total_chats"],
                "Total Recommendations": stats["total_recommendations"],
            }
            st.table(pd.DataFrame(analytics_data.items(), columns=["Metric", "Count"]))

        st.divider()

        # Favorites
        if st.session_state.user_memory.get_favorites():
            st.subheader("❤️ Your Favorite Items")
            favorites_df = pd.DataFrame(
                st.session_state.user_memory.get_favorites(),
                columns=["Item"]
            )
            st.dataframe(favorites_df, use_container_width=True)
        else:
            st.info("No favorite items yet. Add items from the Menu Browser!")

        # Popular Items
        top_items = st.session_state.analytics.get_top_items(5)
        if top_items:
            st.divider()
            st.subheader("🏆 Most Recommended Items (All Sessions)")
            top_items_df = pd.DataFrame(top_items, columns=["Item", "Recommendations"])
            st.bar_chart(top_items_df.set_index("Item"))

    # ============= TAB 5: FAQ =============
    with tab5:
        st.subheader("❓ Frequently Asked Questions")

        faqs = {
            "Opening Hours": "We are open from 11:00 AM to 11:00 PM, 7 days a week.",
            "Delivery": "Yes, we deliver within 5km radius. Delivery time is typically 30-45 minutes.",
            "Reservations": "Yes, you can book a table by calling us or using the online reservation system.",
            "Payment Methods": "We accept Cash, Card, UPI, and all major digital wallets.",
            "Dietary Restrictions": "We have vegetarian and non-vegetarian options. Inform us of allergies while ordering.",
            "Birthday Parties": "We offer special birthday packages. Contact us for more details.",
            "Corporate Events": "Yes, we cater for corporate events and celebrations.",
            "Special Requests": "You can add special requests while ordering or during the chat."
        }

        for question, answer in faqs.items():
            with st.expander(f"❓ {question}"):
                st.write(answer)

        st.divider()

        # Contact Form
        st.subheader("📧 Have More Questions?")
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            message = st.text_area("Your Message")

            if st.form_submit_button("Send Message"):
                if name and email and message:
                    st.success("✅ Message sent! We'll get back to you soon.")
                else:
                    st.error("Please fill in all fields.")

# Run main application
if __name__ == "__main__":
    main()
