"""
Food recommendation engine using pandas for menu analysis.
Recommends dishes based on budget, vegetarian preference, spicy level, and category.
"""

import pandas as pd
from typing import List, Dict, Any, Optional
import os


class FoodRecommender:
    """
    Recommends food items from menu based on user preferences and criteria.
    Uses pandas DataFrame for efficient data filtering and analysis.
    """

    def __init__(self, menu_file: str = "data/menu.csv"):
        """
        Initialize the recommendation engine by loading menu data.
        
        Args:
            menu_file: Path to CSV file containing menu items
        """
        self.menu_df = pd.read_csv(menu_file)
        self._prepare_data()

    def _prepare_data(self) -> None:
        """Prepare and validate menu data."""
        # Ensure all required columns exist
        required_columns = ['name', 'category', 'type', 'spicy_level', 'price', 'rating']
        for col in required_columns:
            if col not in self.menu_df.columns:
                raise ValueError(f"Missing required column: {col}")

        # Convert price to numeric
        self.menu_df['price'] = pd.to_numeric(self.menu_df['price'], errors='coerce')
        self.menu_df['rating'] = pd.to_numeric(self.menu_df['rating'], errors='coerce')

    def get_menu(self) -> pd.DataFrame:
        """
        Get complete menu as DataFrame.
        
        Returns:
            DataFrame with all menu items
        """
        return self.menu_df.copy()

    def recommend_by_preferences(
        self,
        veg_preference: str = "Both",
        spicy_preference: str = "Medium",
        budget_range: str = "Medium",
        limit: int = 5
    ) -> pd.DataFrame:
        """
        Recommend items based on user preferences.
        
        Args:
            veg_preference: 'Veg', 'Non-Veg', or 'Both'
            spicy_preference: 'Mild', 'Medium', or 'Spicy'
            budget_range: 'Budget' (0-150), 'Medium' (150-350), 'Premium' (350+)
            limit: Number of recommendations
            
        Returns:
            DataFrame with recommended items
        """
        df = self.menu_df.copy()

        # Filter by vegetarian preference
        if veg_preference != "Both":
            df = df[df['type'] == veg_preference]

        # Filter by spice level
        if spicy_preference != "Any":
            df = df[df['spicy_level'] == spicy_preference]

        # Filter by budget range
        if budget_range == "Budget":
            df = df[df['price'] <= 150]
        elif budget_range == "Medium":
            df = df[(df['price'] > 150) & (df['price'] <= 350)]
        elif budget_range == "Premium":
            df = df[df['price'] > 350]

        # Sort by rating (highest first)
        df = df.sort_values('rating', ascending=False)

        return df.head(limit)

    def recommend_by_category(
        self,
        category: str,
        limit: int = 5,
        veg_preference: str = "Both"
    ) -> pd.DataFrame:
        """
        Recommend items from specific category.
        
        Args:
            category: Food category (e.g., 'Main Course', 'Starter')
            limit: Number of recommendations
            veg_preference: 'Veg', 'Non-Veg', or 'Both'
            
        Returns:
            DataFrame with recommended items from category
        """
        df = self.menu_df[self.menu_df['category'] == category].copy()

        if veg_preference != "Both":
            df = df[df['type'] == veg_preference]

        df = df.sort_values('rating', ascending=False)

        return df.head(limit)

    def recommend_by_budget(self, budget: float, limit: int = 5) -> pd.DataFrame:
        """
        Recommend best-rated items within budget.
        
        Args:
            budget: Maximum budget amount
            limit: Number of recommendations
            
        Returns:
            DataFrame with affordable items sorted by rating
        """
        df = self.menu_df[self.menu_df['price'] <= budget].copy()
        df = df.sort_values('rating', ascending=False)

        return df.head(limit)

    def recommend_similar(self, item_name: str, limit: int = 5) -> pd.DataFrame:
        """
        Recommend items similar to a given item.
        
        Args:
            item_name: Name of reference item
            limit: Number of recommendations
            
        Returns:
            DataFrame with similar items
        """
        # Find the reference item
        ref_item = self.menu_df[self.menu_df['name'].str.lower() == item_name.lower()]

        if ref_item.empty:
            return pd.DataFrame()

        ref_category = ref_item['category'].values[0]
        ref_type = ref_item['type'].values[0]
        ref_spice = ref_item['spicy_level'].values[0]

        # Find similar items (same category and type)
        similar = self.menu_df[
            (self.menu_df['category'] == ref_category) &
            (self.menu_df['type'] == ref_type) &
            (self.menu_df['name'] != item_name)
        ].copy()

        similar = similar.sort_values('rating', ascending=False)

        return similar.head(limit)

    def get_items_by_spice_level(self, spice_level: str) -> pd.DataFrame:
        """
        Get all items with specific spice level.
        
        Args:
            spice_level: 'Mild', 'Medium', or 'Spicy'
            
        Returns:
            DataFrame with items of specified spice level
        """
        return self.menu_df[self.menu_df['spicy_level'] == spice_level].copy()

    def get_categories(self) -> List[str]:
        """Get list of all available categories."""
        return self.menu_df['category'].unique().tolist()

    def get_items_by_category(self, category: str) -> pd.DataFrame:
        """
        Get all items in a category.
        
        Args:
            category: Food category
            
        Returns:
            DataFrame with items from category
        """
        return self.menu_df[self.menu_df['category'] == category].copy()

    def get_veg_options(self) -> pd.DataFrame:
        """Get all vegetarian items."""
        return self.menu_df[self.menu_df['type'] == 'Veg'].copy()

    def get_nonveg_options(self) -> pd.DataFrame:
        """Get all non-vegetarian items."""
        return self.menu_df[self.menu_df['type'] == 'Non-Veg'].copy()

    def get_items_within_budget(self, max_price: float) -> pd.DataFrame:
        """
        Get items within budget.
        
        Args:
            max_price: Maximum price
            
        Returns:
            DataFrame with affordable items
        """
        return self.menu_df[self.menu_df['price'] <= max_price].copy()

    def get_top_rated_items(self, limit: int = 5) -> pd.DataFrame:
        """
        Get top-rated items.
        
        Args:
            limit: Number of items
            
        Returns:
            DataFrame with highest-rated items
        """
        return self.menu_df.nlargest(limit, 'rating')

    def search_items(self, search_query: str) -> pd.DataFrame:
        """
        Search for items by name.
        
        Args:
            search_query: Search term
            
        Returns:
            DataFrame with matching items
        """
        mask = self.menu_df['name'].str.contains(search_query, case=False, na=False)
        return self.menu_df[mask].copy()

    def get_item_details(self, item_name: str) -> Optional[Dict[str, Any]]:
        """
        Get detailed information about a specific item.
        
        Args:
            item_name: Name of the item
            
        Returns:
            Dictionary with item details or None if not found
        """
        item = self.menu_df[self.menu_df['name'].str.lower() == item_name.lower()]

        if item.empty:
            return None

        return item.iloc[0].to_dict()

    def get_combo_recommendations(
        self,
        base_item: str,
        veg_preference: str = "Both",
        limit: int = 3
    ) -> Dict[str, pd.DataFrame]:
        """
        Suggest complementary items for a meal combo.
        
        Args:
            base_item: Main item selected
            veg_preference: User's vegetarian preference
            limit: Number of suggestions per category
            
        Returns:
            Dictionary with recommendations by category
        """
        combos = {}

        # Get starter recommendations
        starters = self.recommend_by_category("Starter", limit, veg_preference)
        if not starters.empty:
            combos["Starter"] = starters

        # Get bread recommendations
        breads = self.recommend_by_category("Bread", limit, veg_preference)
        if not breads.empty:
            combos["Bread"] = breads

        # Get dessert recommendations
        desserts = self.recommend_by_category("Dessert", limit, veg_preference)
        if not desserts.empty:
            combos["Dessert"] = desserts

        # Get beverage recommendations
        beverages = self.recommend_by_category("Beverage", limit, veg_preference)
        if not beverages.empty:
            combos["Beverage"] = beverages

        return combos

    def get_price_range_statistics(self) -> Dict[str, Any]:
        """
        Get price statistics from menu.
        
        Returns:
            Dictionary with price stats
        """
        return {
            "min_price": float(self.menu_df['price'].min()),
            "max_price": float(self.menu_df['price'].max()),
            "average_price": float(self.menu_df['price'].mean()),
            "median_price": float(self.menu_df['price'].median())
        }

    def get_menu_statistics(self) -> Dict[str, Any]:
        """
        Get overall menu statistics.
        
        Returns:
            Dictionary with menu statistics
        """
        return {
            "total_items": len(self.menu_df),
            "categories": self.menu_df['category'].nunique(),
            "veg_items": len(self.menu_df[self.menu_df['type'] == 'Veg']),
            "non_veg_items": len(self.menu_df[self.menu_df['type'] == 'Non-Veg']),
            "average_rating": float(self.menu_df['rating'].mean()),
            "price_stats": self.get_price_range_statistics()
        }
