import streamlit as st
import requests

# Your Spoonacular API key
API_KEY = "a010192bae9d4b83a9013e53cca69a2c"

# Custom CSS for UI improvements
st.markdown(
    """
    <style>
        .title {
            font-size: 50px;
            color: #FF6F61;
            font-family: 'Arial', sans-serif;
            text-align: center;
        }
        .subheader {
            font-size: 24px;
            color: #4B8B3B;
        }
        .button {
            background-color: #FF6F61;
            color: white;
            border-radius: 5px;
            padding: 10px 20px;
            font-size: 16px;
        }
        .container {
            padding: 20px;
        }
        .recipe-image {
            width: 100%;
            max-width: 400px;
            margin-bottom: 20px;
        }
        .stButton button {
            background-color: #FF6F61;
            color: white;
        }
        .stTextInput input {
            background-color: #F3F4F6;
            color: #333;
            border-radius: 5px;
        }
        .stSelectbox select, .stMultiselect select {
            background-color: #F3F4F6;
            color: #333;
            border-radius: 5px;
        }
        .stTextArea textarea {
            background-color: #F3F4F6;
            color: #333;
            border-radius: 5px;
        }
    </style>
    """, unsafe_allow_html=True
)

# Function to get recipes from the Spoonacular API
def get_recipes(ingredients, meal_type="Any", diet=None, cuisine=None):
    url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&apiKey={API_KEY}&number=5"
    if meal_type != "Any":
        url += f"&type={meal_type}"
    if diet:
        url += f"&diet={diet}"
    if cuisine:
        url += f"&cuisine={cuisine}"

    response = requests.get(url)
    
    if response.status_code == 200:
        recipes = response.json()
        return recipes
    else:
        return None

# Function to get cooking instructions for a recipe
def get_cooking_instructions(recipe_id):
    url = f"https://api.spoonacular.com/recipes/{recipe_id}/analyzedInstructions?apiKey={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        instructions = response.json()
        return instructions
    else:
        return None

# Main function
def main():
    st.markdown("<h1 class='title'>Recipe Finder</h1>", unsafe_allow_html=True)
    st.write("Enter the ingredients you have, and we'll find recipes for you!")

    # Sidebar for ingredients input, meal type, dietary preference, and cuisine
    st.sidebar.title("Search Recipes")
    ingredients = st.sidebar.text_input("Enter ingredients (comma-separated)", help="Enter a list of ingredients you have, separated by commas.")
    meal_type = st.sidebar.selectbox("Select Meal Type", ["Any", "Breakfast", "Lunch", "Dinner", "Snack"])
    diet = st.sidebar.selectbox("Select Dietary Preference", ["Any", "Vegetarian", "Vegan", "Gluten-Free", "Ketogenic"])
    cuisine = st.sidebar.selectbox("Select Cuisine", ["Any", "Italian", "Mexican", "Chinese", "Indian", "French"])
    
    # Add a button to clear all filters
    if st.sidebar.button("Clear All Filters"):
        ingredients = ""
        meal_type = "Any"
        diet = "Any"
        cuisine = "Any"
        st.experimental_rerun()

    # Button to fetch recipes
    if st.sidebar.button("Find Recipes"):
        if ingredients:
            # Fetch recipes based on input ingredients, meal type, and dietary preference
            recipes = get_recipes(ingredients, meal_type, diet, cuisine)
            
            if recipes:
                # Display recipe results
                for i, recipe in enumerate(recipes):
                    st.subheader(f"{i + 1}. {recipe['title']}")
                    st.image(f"https://spoonacular.com/recipeImages/{recipe['id']}-312x231.jpg", width=500)  # Recipe Image
                    st.write(f"Used ingredients: {', '.join([ingredient['name'] for ingredient in recipe['usedIngredients']])}")
                    st.write(f"Missing ingredients: {', '.join([ingredient['name'] for ingredient in recipe['missedIngredients']])}")

                    # Get and display cooking instructions
                    instructions = get_cooking_instructions(recipe['id'])
                    if instructions:
                        for step in instructions[0]['steps']:
                            st.write(f"{step['number']}. {step['step']}")

            else:
                st.write("Sorry, no recipes found. Try again!")
        else:
            st.write("Please enter some ingredients.")

# Run the app
if __name__ == "__main__":
    main()