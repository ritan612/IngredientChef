import json
recipes = [
    {
        "title": "Spaghetti Carbonara",
        "ingredients": ["spaghetti", "eggs", "parmesan cheese", "bacon", "black pepper"],
        "instructions": "Cook spaghetti. Mix eggs and cheese. Cook bacon. Combine all with pasta and pepper.",
        "meal_type": "Dinner",
        "rating": 4.7,
        "image": r"c:\Users\Lenovo\Desktop\mispce\2nd year\sem4 2year\I2207\project\picture\pngwing.com.png"
    },
   {
        "title": "Chicken Curry",
        "ingredients": ["chicken", "curry powder", "coconut milk", "onion", "garlic", "ginger", "tomatoes"],
        "instructions": "Cook onions, garlic, and ginger. Add chicken and curry powder. Stir in tomatoes and coconut milk. Simmer until chicken is done.",
        "meal_type": "Dinner",
        "rating": 4.8,
        "image": r"c:\Users\Lenovo\Desktop\mispce\2nd year\sem4 2year\I2207\project\picture\vecteezy_chicken-makhani-png-with-ai-generated_25268632.png"
    },
    {
        "title": "Minestrone Soup",
        "ingredients": ["onion", "carrots", "celery", "zucchini", "tomatoes", "beans", "pasta", "vegetable broth", "basil"],
        "instructions": "Sauté onions, carrots, and celery. Add zucchini, tomatoes, beans, broth, and pasta. Simmer until vegetables and pasta are tender. Stir in basil.",
        "meal_type": "Lunch",
        "rating": 4.5,
        "image": r"c:\Users\Lenovo\Desktop\mispce\2nd year\sem4 2year\I2207\project\picture\minestrone-soup.png"
    },
    {
        "title": "Greek Salad",
        "ingredients": ["cucumber", "tomatoes", "red onion", "olives", "feta cheese", "olive oil", "lemon juice", "oregano"],
        "instructions": "Chop vegetables. Toss with olives, feta, olive oil, lemon juice, and oregano.",
        "meal_type": "Salad",
        "rating": 4.6,
        "image": r"c:\Users\Lenovo\Desktop\mispce\2nd year\sem4 2year\I2207\project\picture\greek salad.png"
    },
    {
        "title": "Pad Thai",
        "ingredients": ["rice noodles", "chicken", "shrimp", "eggs", "bean sprouts", "peanuts", "lime", "fish sauce", "tamarind paste", "sugar"],
        "instructions": "Cook noodles. Stir-fry chicken, shrimp, and eggs. Add noodles, bean sprouts, and sauce made from fish sauce, tamarind, and sugar. Top with peanuts and lime.",
        "meal_type": "Main Course",
        "rating": 4.8,
        "image": r"c:\Users\Lenovo\Desktop\mispce\2nd year\sem4 2year\I2207\project\picture\pad-thai-nasi-goreng-thai-cuisine-thai-tea-chinese-cuisine-pad-thai.png"
    },
    {
        "title": "Pancakes",
        "ingredients": ["flour", "milk", "eggs", "baking powder", "sugar", "butter"],
        "instructions": "Mix flour, milk, eggs, baking powder, and sugar. Cook on griddle. Serve with butter and syrup.",
        "meal_type": "Breakfast",
        "rating": 4.7,
        "image": r"c:\Users\Lenovo\Desktop\mispce\2nd year\sem4 2year\I2207\project\picture\pancake.png"
    },
    {
        "title": "Tacos",
        "ingredients": ["ground beef", "taco seasoning", "tortillas", "lettuce", "tomatoes", "cheese", "sour cream"],
        "instructions": "Cook beef with seasoning. Serve in tortillas with lettuce, tomatoes, cheese, and sour cream.",
        "meal_type": "Dinner",
        "rating": 4.6,
        "image": r"c:\Users\Lenovo\Desktop\mispce\2nd year\sem4 2year\I2207\project\picture\tacos.png"
    },
    {
        "title": "Chocolate Cake",
        "ingredients": ["flour", "sugar", "cocoa powder", "baking powder", "eggs", "milk", "butter"],
        "instructions": "Mix dry ingredients. Add eggs, milk, and melted butter. Bake until done. Frost with chocolate icing.",
        "meal_type": "Dessert",
        "rating": 4.8,
        "image": r"c:\Users\Lenovo\Desktop\mispce\2nd year\sem4 2year\I2207\project\picture\chocolate cake.png"
    },
    {
        "title": "Caprese Salad",
        "ingredients": ["tomatoes", "mozzarella", "basil", "olive oil", "balsamic vinegar"],
        "instructions": "Slice tomatoes and mozzarella. Layer with basil leaves. Drizzle with olive oil and balsamic vinegar.",
        "meal_type": "Salad",
        "rating": 4.5,
        "image": r"c:\Users\Lenovo\Desktop\mispce\2nd year\sem4 2year\I2207\project\picture\caprese salad.png"
    },
    {
        "title": "Fish Tacos",
        "ingredients": ["white fish", "tortillas", "cabbage", "lime", "cilantro", "sour cream", "cumin", "cayenne pepper"],
        "instructions": "Season and cook fish. Serve in tortillas with cabbage, lime, cilantro, and seasoned sour cream.",
        "meal_type": "Dinner",
        "rating": 4.6,
        "image": r"c:\Users\Lenovo\Desktop\mispce\2nd year\sem4 2year\I2207\project\picture\fish tacos.png"
    },
    {
        "title": "French Toast",
        "ingredients": ["bread", "eggs", "milk", "cinnamon", "vanilla", "butter"],
        "instructions": "Dip bread in egg mixture. Cook on griddle until golden. Serve with butter and syrup.",
        "meal_type": "Breakfast",
        "rating": 4.7,
        "image": r"c:\Users\Lenovo\Desktop\mispce\2nd year\sem4 2year\I2207\project\picture\french toast.png"
    },
    {
        "title": "Gazpacho",
        "ingredients": ["tomatoes", "cucumber", "bell pepper", "onion", "garlic", "olive oil", "vinegar", "bread"],
        "instructions": "Blend vegetables with soaked bread, olive oil, and vinegar. Chill before serving.",
        "meal_type": "Lunch",
        "rating": 4.5,
        "image": r"c:\Users\Lenovo\Desktop\mispce\2nd year\sem4 2year\I2207\project\picture\gazpacho.png"
    },
    {
        "title": "Butter Chicken",
        "ingredients": ["chicken", "yogurt", "garlic", "ginger", "tomatoes", "cream", "butter", "garam masala", "cumin"],
        "instructions": "Marinate chicken in yogurt, garlic, and ginger. Cook with tomatoes, cream, butter, and spices until chicken is done.",
        "meal_type": "Main Course",
        "rating": 4.8,
        "image": r"c:\Users\Lenovo\Desktop\mispce\2nd year\sem4 2year\I2207\project\picture\butter chicken.png"
    },
    {
        "title": "Ratatouille",
        "ingredients": ["eggplant", "zucchini", "bell peppers", "tomatoes", "onion", "garlic", "herbs"],
        "instructions": "Sauté vegetables with garlic and herbs. Simmer until tender.",
        "meal_type": "Main Course",
        "rating": 4.5,
        "image": r"c:\Users\Lenovo\Desktop\mispce\2nd year\sem4 2year\I2207\project\picture\ratatouille.png"
    },
    {
        "title": "Chili Con Carne",
        "ingredients": ["ground beef", "kidney beans", "onions", "tomatoes", "chili powder", "cumin", "garlic"],
        "instructions": "Cook beef with onions, garlic, and spices. Add beans and tomatoes. Simmer until thickened.",
        "meal_type": "Main Course",
        "rating": 4.7,
        "image": r"c:\Users\Lenovo\Desktop\mispce\2nd year\sem4 2year\I2207\project\picture\chili con carne.png"
    },
    {
        "title": "Paella",
        "ingredients": ["rice", "chicken", "shrimp", "chorizo", "peas", "tomatoes", "saffron", "broth"],
        "instructions": "Cook chicken and chorizo. Add rice, saffron, and broth. Simmer. Add shrimp and peas near the end.",
        "meal_type": "Main Course",
        "rating": 4.8,
        "image": r"c:\Users\Lenovo\Desktop\mispce\2nd year\sem4 2year\I2207\project\picture\paella.png"
    },
    {
        "title": "Moussaka",
        "ingredients": ["eggplant", "ground beef", "onions", "tomatoes", "béchamel sauce", "cheese"],
        "instructions": "Layer fried eggplant with beef mixture. Top with béchamel and cheese. Bake until golden.",
        "meal_type": "Main Course",
        "rating": 4.6,
        "image": r"c:\Users\Lenovo\Desktop\mispce\2nd year\sem4 2year\I2207\project\picture\moussaka.png"
    },
    {
        "title": "Falafel",
        "ingredients": ["chickpeas", "onions", "garlic", "parsley", "cumin", "coriander", "flour"],
        "instructions": "Blend ingredients. Form into balls. Fry until golden.",
        "meal_type": "Appetizer",
        "rating": 4.7,
        "image": r"c:\Users\Lenovo\Desktop\mispce\2nd year\sem4 2year\I2207\project\picture\falafel.png"
    },
    {
        "title": "Tiramisu",
        "ingredients": ["mascarpone cheese", "espresso", "ladyfingers", "eggs", "sugar", "cocoa powder"],
        "instructions": "Layer mascarpone mixture with espresso-dipped ladyfingers. Chill and dust with cocoa powder.",
        "meal_type": "Dessert",
        "rating": 4.8,
        "image": r"c:\Users\Lenovo\Desktop\mispce\2nd year\sem4 2year\I2207\project\picture\tiramisu.png"
    },
    {
        "title": "Stuffed Peppers",
        "ingredients": ["bell peppers", "ground beef", "rice", "tomatoes", "onion", "garlic", "cheese"],
        "instructions": "Stuff peppers with beef, rice, tomatoes, onions, and garlic. Bake until peppers are tender. Top with cheese.",
        "meal_type": "Main Course",
        "rating": 4.5,
        "image": r"c:\Users\Lenovo\Desktop\mispce\2nd year\sem4 2year\I2207\project\picture\stuffed peppers.png"
    },
    {
        "title": "Lamb Kebabs",
        "ingredients": ["lamb", "yogurt", "garlic", "mint", "cumin", "paprika"],
        "instructions": "Marinate lamb in yogurt and spices. Skewer and grill until done.",
        "meal_type": "Main Course",
        "rating": 4.7,
        "image": r"c:\Users\Lenovo\Desktop\mispce\2nd year\sem4 2year\I2207\project\picture\lamb kebabs.png"
    },
    {
        "title": "Lentil Soup",
        "ingredients": ["lentils", "carrots", "celery", "onions", "garlic", "tomatoes", "cumin", "broth"],
        "instructions": "Sauté vegetables and garlic. Add lentils, tomatoes, broth, and cumin. Simmer until lentils are tender.",
        "meal_type": "Lunch",
        "rating": 4.5,
        "image": r"c:\Users\Lenovo\Desktop\mispce\2nd year\sem4 2year\I2207\project\picture\lentil_soup-removebg-preview.png"
    },
    {
        "title": "Banana Bread",
        "ingredients": ["bananas", "flour", "sugar", "eggs", "butter", "baking soda"],
        "instructions": "Mix ingredients. Bake until a toothpick comes out clean.",
        "meal_type": "Dessert",
        "rating": 4.8,
        "image": r"c:\Users\Lenovo\Desktop\mispce\2nd year\sem4 2year\I2207\project\picture\banana-bread-isolated-transparent-background-png-psd_888962-825-removebg-preview.png"
    },
    {
        "title": "Crème Brûlée",
        "ingredients": ["cream", "sugar", "egg yolks", "vanilla", "brown sugar"],
        "instructions": "Bake custard mixture. Chill. Caramelize sugar on top before serving.",
        "meal_type": "Dessert",
        "rating": 4.8,
        "image": r"c:\Users\Lenovo\Desktop\mispce\2nd year\sem4 2year\I2207\project\picture\creme_brule-removebg-preview.png"
    },
    {
        "title": "Shepherd's Pie",
        "ingredients": ["ground lamb", "potatoes", "carrots", "peas", "onion", "gravy"],
        "instructions": "Layer cooked lamb and vegetables with mashed potatoes. Bake until golden.",
        "meal_type": "Main Course",
        "rating": 4.7,
        "image": r"c:\Users\Lenovo\Desktop\mispce\2nd year\sem4 2year\I2207\project\picture\shepherd_s_pie-removebg-preview.png"
    },
    {
        "title": "Caesar Salad",
        "ingredients": ["romaine lettuce", "croutons", "parmesan cheese", "Caesar dressing"],
        "instructions": "Toss lettuce with croutons, cheese, and dressing.",
        "meal_type": "Salad",
        "rating": 4.5,
        "image": r"c:\Users\Lenovo\Desktop\mispce\2nd year\sem4 2year\I2207\project\picture\chicken-caesar-salad-chicken-caesar-salad-11563612667adbn0huszd-removebg-preview.png"
    },
    {
        "title": "Shakshuka",
        "ingredients": ["eggs", "tomatoes", "bell peppers", "onion", "garlic", "spices"],
        "instructions": "Cook vegetables with spices. Poach eggs in sauce.",
        "meal_type": "Breakfast",
        "rating": 4.6,
        "image": r"c:\Users\Lenovo\Desktop\mispce\2nd year\sem4 2year\I2207\project\picture\shakshuka.png"
    },
    {
        "title": "Beef Wellington",
        "ingredients": ["beef tenderloin", "mushrooms", "prosciutto", "puff pastry", "egg wash"],
        "instructions": "Wrap seared beef in mushrooms, prosciutto, and puff pastry. Bake until golden.",
        "meal_type": "Main Course",
        "rating": 4.8,
        "image": r"c:\Users\Lenovo\Desktop\mispce\2nd year\sem4 2year\I2207\project\picture\beef_wellington-removebg-preview.png"
    }
]

with open('recipes.json', 'w') as file:
    json.dump(recipes, file)
