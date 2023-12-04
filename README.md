![Alt text](/ReadMe/readme_coverpage.jpg)
## Project Summary
The objective of this project is to develop a user-friendly application that recommends a recipe to users (from a database of over 8000 recipes from the Food Network) based on current grocery store promotion items (Super C and Metro grocery stores).

![Alt text](/ReadMe/readme_flask.jpg)

## How Does It Work ?
The user will randomly generate 5 products that are currently on promotion at a grocery store (Super C or Metro). Then, based on the products generated, 5 different recipes from the Food Network will be recommended to the user.
## How Was This Created ?
![Alt text](/ReadMe/readme_img2.jpg)
## Repository Files
_Description of Notebooks_
- [Notebook 1](/Notebook1_FoodNetwork_Recipes.ipynb) covers the following: 
  -  Web Scraping the Food Network's website for recipes
  -  Cleaning the dataframe after web scrapping
- [Notebook 2](/Notebook2_GroceryStorePromotions.ipynb) covers the following:
  -  Web scraping grocery store websites (Super C and Metro) for promotions (effective as of 11.29.2023)
  -  Cleaning the dataframe after web scraping
- [Notebook 3](/Notebook3_RecipeRecommendations.ipynb) covers the following:
  -  Recipe Recommendations based on 5 randomly generated grocery store items.
  -  The functions created for this project are saved as pickle files (for deployment on Flask).
- [Notebook 4](/Notebook4_FlaskDeployment.py) covers the following:
  -  Deployment of the project on Flask
  -  The following files are required to deploy the project on Flask: [Notebook 3 (.py)](/Notebook3_RecipeRecommendations.py) , [grocery_items.pkl](/grocery_items.pkl) , [recipe_recommendation.pkl](/recipe_recommendation.pkl),the folder [templates](/templates) and the folder [static](/static) 

_Description of CSV files_
- [recipes.csv](/recipes.csv)  : recipes scraped & not cleaned (generated from Notebook 1)
- [recipes_clean_v2.csv](/recipes_clean_v2.csv)  : recipes scraped & cleaned (generated from Notebook 1)
- [metro_11292023.csv](/metro_11292023.csv)  : Metro products scraped & not cleaned (generated from Notebook 2)
- [superc_11292023.csv](/superc_11292023.csv)  : Super C products scraped & not cleaned (generated from Notebook 2)
- [grocerypromo_11292023.csv](/grocerypromo_11292023.csv) : Metro & Super C promotions & not cleaned (generated from Notebook 2)
- [grocerydeals_v3.csv](/grocerydeals_v3.csv) : Metro & Super C promotions & cleaned (generated from Notebook 2)
