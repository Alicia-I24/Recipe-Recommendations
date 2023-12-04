from flask import Flask,render_template
import pickle
from Notebook3_RecipeRecommendations import random_groceries_5 #need to import the functions from .py file
from Notebook3_RecipeRecommendations import recipe_recommendations #need to import the functions from .py file

app=Flask(__name__)

#### STEP 1
# IMPORTING THE GROCERY RANDOMIZER
with open('grocery_items.pkl', 'rb') as file:
    saved_data=pickle.load(file)
loaded_function=saved_data['function']

# IMPORTING THE RECIPE RECOMMENDATION
with open('recipe_recommendation.pkl', 'rb') as file2:
    saved_data2=pickle.load(file2)
loaded_function2=saved_data2['function']
loaded_function2()

#### STEP 2
@app.route("/")
def index():
    
    # Recipe Recommendation
    tables=loaded_function2() #function returns 2 dataframes
    groceries=tables[0] #first table is the random groceries
    recipes=tables[1] #second table is the recipes 

    groceries_table=groceries.to_html(classes='table table-striped', index=False) #transforming the df to html table
    recipes_table=recipes.to_html(classes='table table-striped', index=False) #transforming the df to html table

    return render_template("index.html",groceries_table=groceries_table,recipes_table=recipes_table)

if __name__=="__main__":
     app.run(debug=True)