ComeLetsCook 🍴

ComeLetsCook is a web application that helps users find recipes based on the ingredients they have at hand. Built using Streamlit and powered by the Spoonacular API, this application provides a user-friendly interface for meal planning and cooking.

Project Overview

ComeLetsCook leverages the Spoonacular API to fetch recipe data based on user-provided ingredients. It analyzes the input and displays relevant recipes along with their used and missing ingredients. For each recipe, users can view detailed cooking instructions to prepare meals easily.

Features ✨

Ingredient-Based Recipe Search: Find recipes by entering available ingredients.
Filters for Meal Type and Cuisine: Refine search results based on meal types (e.g., breakfast, lunch) and cuisines (e.g., Italian, Indian).
Dietary Preferences: Supports dietary options like vegetarian, vegan, and gluten-free.
Step-by-Step Cooking Instructions: Provides detailed steps to prepare meals.
Interactive and Intuitive UI: Clean, custom-designed interface for easy navigation.

Setup Instructions ⚙️

Prerequisites
Python 3.7 or higher.
A valid Spoonacular API key.
Basic familiarity with running Python scripts.

Spoonacular API Setup:

Sign Up: Create an account at Spoonacular and generate an API key.
Replace API Key: Open comeletscook.py and replace the API_KEY variable with your Spoonacular API key:

API_KEY = "your_spoonacular_api_key"


Application Setup:
Clone the Repository:

git clone https://github.com/yourusername/comeletscook.git
cd comeletscook


*Install Required Libraries:
Install Streamlit and other dependencies:

pip install streamlit requests


*Run the Application:
Start the Streamlit server:

streamlit run comeletscook.py


Access the Application:
Open your browser and go to the provided URL (e.g., http://localhost:8501).

Usage 📋
Enter Ingredients: Input a comma-separated list of ingredients in the sidebar.
Set Filters (Optional): Choose meal types, dietary preferences, or cuisines.
Find Recipes: Click "Find Recipes" to view matching results.
Clear Filters: Use the "Clear All Filters" button to reset inputs.
Explore Results: View recipes, used/missing ingredients, and cooking instructions.
