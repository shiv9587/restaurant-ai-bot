"""
AI helper module using Groq API for restaurant assistant chatbot.
Handles AI responses with context awareness and conversation management.
"""
from dotenv import load_dotenv
load_dotenv()
import os
from groq import Groq
from typing import List, Dict, Any, Optional



class AIAssistant:
    """
    Restaurant AI Assistant powered by Groq API.
    Provides intelligent responses about menu, recommendations, and general inquiries.
    """

    def __init__(self, api_key: Optional[str] = None, model: str = "llama-3.3-70b-versatile"):
        """
        Initialize AI Assistant.
        
        Args:
            api_key: Groq API key (defaults to GROQ_API_KEY environment variable)
            model: Model name to use (defaults to mixtral-8x7b-32768)
        """
        self.api_key = api_key or os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("GROQ_API_KEY environment variable not set")

        self.client = Groq(api_key=self.api_key)
        self.model = self.model = os.getenv("GROQ_MODEL", "llama3-8b-8192")
        self.conversation_history = []

    @staticmethod
    def get_system_prompt(restaurant_name: str = "Our Restaurant") -> str:
        """
        Get the system prompt for restaurant assistant.
        
        Args:
            restaurant_name: Name of the restaurant
            
        Returns:
            System prompt string
        """
        return f"""You are a helpful and friendly restaurant assistant for {restaurant_name}. 
Your primary responsibilities are:

1. Help customers with menu inquiries and food recommendations
2. Provide information about restaurant hours, delivery, and reservations
3. Answer questions about ingredients, spice levels, and dietary preferences
4. Suggest food combinations and meal options based on customer preferences
5. Handle complaints and special requests professionally

Guidelines:
- Be warm, welcoming, and professional in tone
- Provide accurate information about menu items
- Respect dietary restrictions and preferences
- Offer helpful suggestions without being pushy
- Keep responses concise and friendly
- If you don't know something, suggest contacting the restaurant directly

When recommending food:
- Ask about budget, dietary preferences, and spice level if not mentioned
- Suggest popular and highly-rated items
- Offer vegetarian options if customer is interested
- Provide pricing information when relevant

Available information about menu:
- Categories: Starters, Main Course, Bread, Desserts, Beverages
- Types: Veg, Non-Veg
- Spice levels: Mild, Medium, Spicy

Remember: Your goal is to enhance customer experience and help them make informed food choices."""

    def chat(self, user_message: str, conversation_history: List[Dict[str, str]]) -> str:
        """
        Send a message and get AI response.
        
        Args:
            user_message: User's input message
            conversation_history: List of previous messages for context
            
        Returns:
            AI assistant's response
        """
        # Build messages list with system prompt
        messages = [
            {"role": "system", "content": self.get_system_prompt()}
        ]

        # Add conversation history
        messages.extend(conversation_history)

        # Add current user message
        messages.append({"role": "user", "content": user_message})

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=1024,
                temperature=0.7,
                top_p=0.9
            )

            return response.choices[0].message.content

        except Exception as e:
            error_message = f"Error communicating with AI: {str(e)}"
            print(error_message)
            return "I apologize, but I'm having trouble connecting. Please try again shortly."

    def get_recommendations_ai(
        self,
        preferences: Dict[str, Any],
        conversation_history: List[Dict[str, str]]
    ) -> str:
        """
        Get AI-powered food recommendations based on preferences.
        
        Args:
            preferences: User preferences dictionary
            conversation_history: Conversation history for context
            
        Returns:
            AI recommendation message
        """
        veg_pref = preferences.get("veg_preference", "Both")
        spice_pref = preferences.get("spicy_preference", "Medium")
        budget = preferences.get("budget_range", "Medium")

        prompt = f"""Based on the following user preferences, provide 3-4 food recommendations:
        
- Vegetarian Preference: {veg_pref}
- Spice Level Preference: {spice_pref}
- Budget Range: {budget}

Please provide friendly recommendations with brief explanations of why each item would be good for them.
Include approximate prices if possible. Keep the tone conversational and helpful."""

        return self.chat(prompt, conversation_history)

    def answer_faq(self, question: str, conversation_history: List[Dict[str, str]]) -> str:
        """
        Answer frequently asked questions about restaurant.
        
        Args:
            question: FAQ question
            conversation_history: Conversation history
            
        Returns:
            AI-generated answer
        """
        faq_context = """
Common FAQs:
1. Opening Hours: 11:00 AM - 11:00 PM (Monday to Sunday)
2. Delivery Available: Yes, within 5km radius, 30-45 minutes
3. Reservations: Yes, call or book online
4. Payment Methods: Cash, Card, UPI, Digital wallets
5. Special Occasions: Birthday parties, corporate events available

Please answer the customer's question based on this information if applicable."""

        prompt = f"{faq_context}\n\nCustomer Question: {question}"
        return self.chat(prompt, conversation_history)

    def suggest_meal_combo(
        self,
        main_item: str,
        veg_preference: str,
        conversation_history: List[Dict[str, str]]
    ) -> str:
        """
        Suggest a complete meal combo around a main item.
        
        Args:
            main_item: Main course item
            veg_preference: User's vegetarian preference
            conversation_history: Conversation history
            
        Returns:
            Meal combo suggestion
        """
        prompt = f"""Suggest a complete meal combo for someone who has chosen '{main_item}' as their main course.
The person prefers {veg_preference} options.

Include recommendations for:
1. A starter to go with it
2. A bread/side dish
3. A dessert to finish
4. A beverage pairing

Make the suggestions friendly and explain why these items complement each other well."""

        return self.chat(prompt, conversation_history)

    def handle_complaint(
        self,
        complaint: str,
        conversation_history: List[Dict[str, str]]
    ) -> str:
        """
        Handle customer complaints professionally.
        
        Args:
            complaint: Customer complaint
            conversation_history: Conversation history
            
        Returns:
            Professional response to complaint
        """
        prompt = f"""A customer has lodged a complaint: '{complaint}'

Please respond with empathy and professionalism. 
- Acknowledge their concern
- Apologize for the inconvenience
- Suggest solutions if possible
- Offer to escalate to management if needed

Keep the tone sincere and helpful."""

        return self.chat(prompt, conversation_history)

    def create_language_response(
        self,
        message: str,
        target_language: str,
        conversation_history: List[Dict[str, str]]
    ) -> str:
        """
        Generate response in specific language.
        
        Args:
            message: User message
            target_language: Language for response ('English' or 'Hindi')
            conversation_history: Conversation history
            
        Returns:
            Response in specified language
        """
        language_instruction = f"Please respond in {target_language}."

        prompt = f"{language_instruction}\n\nUser message: {message}"
        return self.chat(prompt, conversation_history)

    def validate_api_key(self) -> bool:
        """
        Validate that API key is working.
        
        Returns:
            True if API key is valid, False otherwise
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": "test"}],
                max_tokens=5
            )
            return True
        except:
            return False

    def estimate_tokens(self, text: str) -> int:
        """
        Rough estimate of token count (4 characters ≈ 1 token).
        
        Args:
            text: Text to estimate
            
        Returns:
            Estimated token count
        """
        return len(text) // 4

    def truncate_history(
        self,
        history: List[Dict[str, str]],
        max_messages: int = 10
    ) -> List[Dict[str, str]]:
        """
        Keep only recent messages to manage context window.
        
        Args:
            history: Full conversation history
            max_messages: Maximum number of messages to keep
            
        Returns:
            Truncated history
        """
        if len(history) > max_messages:
            return history[-max_messages:]
        return history


class ContextManager:
    """
    Manages conversation context and memory for multi-turn conversations.
    """

    def __init__(self, max_history: int = 10):
        """
        Initialize context manager.
        
        Args:
            max_history: Maximum conversation messages to keep
        """
        self.max_history = max_history
        self.context = {
            "user_name": None,
            "preferences": {},
            "last_recommendation": None,
            "conversation_count": 0
        }

    def update_context(self, key: str, value: Any) -> None:
        """
        Update context information.
        
        Args:
            key: Context key
            value: Context value
        """
        self.context[key] = value

    def get_context(self, key: str) -> Any:
        """
        Get context information.
        
        Args:
            key: Context key
            
        Returns:
            Context value or None
        """
        return self.context.get(key)

    def format_context_for_prompt(self) -> str:
        """
        Format context information for use in prompts.
        
        Returns:
            Formatted context string
        """
        context_str = ""

        if self.context.get("user_name"):
            context_str += f"User Name: {self.context['user_name']}\n"

        if self.context.get("preferences"):
            context_str += f"User Preferences: {self.context['preferences']}\n"

        return context_str

    def reset_context(self) -> None:
        """Reset all context information."""
        self.context = {
            "user_name": None,
            "preferences": {},
            "last_recommendation": None,
            "conversation_count": 0
        }
