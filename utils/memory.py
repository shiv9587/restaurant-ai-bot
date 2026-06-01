"""
Memory module for storing user preferences and chat history.
Manages session-based data including user name, food preferences, and conversation history.
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Any


class UserMemory:
    """
    Manages user information, preferences, and conversation history.
    Stores data in session state for easy access and persistence within a session.
    """

    def __init__(self):
        """Initialize user memory with empty preferences and history."""
        self.preferences = {
            "name": None,
            "veg_preference": None,  # 'Veg', 'Non-Veg', 'Both'
            "spicy_preference": None,  # 'Mild', 'Medium', 'Spicy'
            "budget_range": None,  # 'Budget', 'Medium', 'Premium'
            "favorite_items": [],
            "disliked_items": []
        }
        self.chat_history = []
        self.recommendations_given = []
        self.session_start_time = datetime.now()

    def set_user_name(self, name: str) -> None:
        """
        Store the user's name.
        
        Args:
            name: User's name
        """
        self.preferences["name"] = name

    def get_user_name(self) -> str:
        """
        Retrieve the user's name.
        
        Returns:
            User's name or 'Guest' if not set
        """
        return self.preferences["name"] or "Guest"

    def set_veg_preference(self, preference: str) -> None:
        """
        Store user's vegetarian preference.
        
        Args:
            preference: 'Veg', 'Non-Veg', or 'Both'
        """
        if preference in ['Veg', 'Non-Veg', 'Both']:
            self.preferences["veg_preference"] = preference

    def get_veg_preference(self) -> str:
        """Get user's vegetarian preference."""
        return self.preferences["veg_preference"] or "Both"

    def set_spicy_preference(self, preference: str) -> None:
        """
        Store user's spice level preference.
        
        Args:
            preference: 'Mild', 'Medium', or 'Spicy'
        """
        if preference in ['Mild', 'Medium', 'Spicy']:
            self.preferences["spicy_preference"] = preference

    def get_spicy_preference(self) -> str:
        """Get user's spice level preference."""
        return self.preferences["spicy_preference"] or "Medium"

    def set_budget_range(self, budget: str) -> None:
        """
        Store user's budget preference.
        
        Args:
            budget: 'Budget', 'Medium', or 'Premium'
        """
        if budget in ['Budget', 'Medium', 'Premium']:
            self.preferences["budget_range"] = budget

    def get_budget_range(self) -> str:
        """Get user's budget preference."""
        return self.preferences["budget_range"] or "Medium"

    def add_to_favorites(self, item: str) -> None:
        """
        Add an item to user's favorites.
        
        Args:
            item: Food item name
        """
        if item not in self.preferences["favorite_items"]:
            self.preferences["favorite_items"].append(item)

    def remove_from_favorites(self, item: str) -> None:
        """
        Remove an item from user's favorites.
        
        Args:
            item: Food item name
        """
        if item in self.preferences["favorite_items"]:
            self.preferences["favorite_items"].remove(item)

    def get_favorites(self) -> List[str]:
        """Get list of user's favorite items."""
        return self.preferences["favorite_items"]

    def add_to_disliked(self, item: str) -> None:
        """
        Add an item to user's disliked list.
        
        Args:
            item: Food item name
        """
        if item not in self.preferences["disliked_items"]:
            self.preferences["disliked_items"].append(item)

    def get_disliked(self) -> List[str]:
        """Get list of user's disliked items."""
        return self.preferences["disliked_items"]

    def add_chat_message(self, role: str, content: str, metadata: Dict[str, Any] = None) -> None:
        """
        Add a message to chat history.
        
        Args:
            role: 'user' or 'assistant'
            content: Message content
            metadata: Additional information (optional)
        """
        message = {
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat(),
            "metadata": metadata or {}
        }
        self.chat_history.append(message)

    def get_chat_history(self) -> List[Dict[str, Any]]:
        """Get complete chat history."""
        return self.chat_history

    def get_chat_history_for_ai(self) -> List[Dict[str, str]]:
        """
        Get chat history in format suitable for AI API.
        
        Returns:
            List of messages with 'role' and 'content' only
        """
        return [{"role": msg["role"], "content": msg["content"]} for msg in self.chat_history]

    def clear_chat_history(self) -> None:
        """Clear chat history."""
        self.chat_history = []

    def add_recommendation(self, item: str, reason: str) -> None:
        """
        Track recommendations given to user.
        
        Args:
            item: Recommended food item
            reason: Reason for recommendation
        """
        recommendation = {
            "item": item,
            "reason": reason,
            "timestamp": datetime.now().isoformat()
        }
        self.recommendations_given.append(recommendation)

    def get_recommendations_count(self) -> int:
        """Get count of recommendations given."""
        return len(self.recommendations_given)

    def get_all_preferences(self) -> Dict[str, Any]:
        """Get all stored preferences as dictionary."""
        return self.preferences.copy()

    def get_session_duration(self) -> float:
        """
        Get session duration in seconds.
        
        Returns:
            Duration in seconds
        """
        duration = datetime.now() - self.session_start_time
        return duration.total_seconds()

    def export_session_data(self) -> Dict[str, Any]:
        """
        Export complete session data.
        
        Returns:
            Dictionary containing all session information
        """
        return {
            "preferences": self.preferences,
            "chat_history": self.chat_history,
            "recommendations": self.recommendations_given,
            "session_duration_seconds": self.get_session_duration(),
            "message_count": len(self.chat_history)
        }

    def reset_session(self) -> None:
        """Reset all session data while keeping preferences."""
        self.chat_history = []
        self.recommendations_given = []
        self.session_start_time = datetime.now()


class AnalyticsTracker:
    """
    Tracks analytics data for the restaurant bot.
    Records total chats, popular items, and user preferences.
    """

    def __init__(self, analytics_file: str = "analytics.json"):
        """
        Initialize analytics tracker.
        
        Args:
            analytics_file: File path to store analytics data
        """
        self.analytics_file = analytics_file
        self.data = self._load_analytics()

    def _load_analytics(self) -> Dict[str, Any]:
        """Load analytics data from file if it exists."""
        if os.path.exists(self.analytics_file):
            try:
                with open(self.analytics_file, 'r') as f:
                    return json.load(f)
            except:
                return self._initialize_analytics()
        return self._initialize_analytics()

    @staticmethod
    def _initialize_analytics() -> Dict[str, Any]:
        """Initialize default analytics structure."""
        return {
            "total_chats": 0,
            "total_recommendations": 0,
            "popular_items": {},
            "user_preferences": {
                "veg": 0,
                "non_veg": 0,
                "spicy_levels": {"Mild": 0, "Medium": 0, "Spicy": 0}
            },
            "daily_stats": {}
        }

    def record_chat(self) -> None:
        """Record a new chat session."""
        self.data["total_chats"] += 1
        self._save_analytics()

    def record_recommendation(self, item: str) -> None:
        """
        Record a recommended item.
        
        Args:
            item: Item name
        """
        self.data["total_recommendations"] += 1
        if item not in self.data["popular_items"]:
            self.data["popular_items"][item] = 0
        self.data["popular_items"][item] += 1
        self._save_analytics()

    def record_preference(self, veg_type: str, spicy_level: str) -> None:
        """
        Record user preference.
        
        Args:
            veg_type: 'Veg' or 'Non-Veg'
            spicy_level: 'Mild', 'Medium', or 'Spicy'
        """
        if veg_type == "Veg":
            self.data["user_preferences"]["veg"] += 1
        else:
            self.data["user_preferences"]["non_veg"] += 1

        if spicy_level in self.data["user_preferences"]["spicy_levels"]:
            self.data["user_preferences"]["spicy_levels"][spicy_level] += 1

        self._save_analytics()

    def get_top_items(self, limit: int = 5) -> List[tuple]:
        """
        Get most recommended items.
        
        Args:
            limit: Number of items to return
            
        Returns:
            List of (item, count) tuples
        """
        sorted_items = sorted(
            self.data["popular_items"].items(),
            key=lambda x: x[1],
            reverse=True
        )
        return sorted_items[:limit]

    def get_analytics_summary(self) -> Dict[str, Any]:
        """Get complete analytics summary."""
        return self.data.copy()

    def _save_analytics(self) -> None:
        """Save analytics data to file."""
        try:
            with open(self.analytics_file, 'w') as f:
                json.dump(self.data, f, indent=2)
        except Exception as e:
            print(f"Error saving analytics: {e}")
