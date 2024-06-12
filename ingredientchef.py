import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from PIL import Image, ImageTk
import json

def load_recipes():
    with open('recipes.json') as file:
        return json.load(file)

recipes = load_recipes()

def get_recipes_by_ingredient(ingredient):
    return [recipe for recipe in recipes if ingredient in recipe['ingredients']]

def show_selected_ingredient(event):
    selected_indices = ingredients_listbox.curselection()
    if selected_indices:
        selected_ingredient = ingredients_listbox.get(selected_indices[0])
        matching_recipes = get_recipes_by_ingredient(selected_ingredient)
        recipe_listbox.delete(0, tk.END)
        for recipe in matching_recipes:
            recipe_listbox.insert(tk.END, recipe['title'])
        global current_recipes
        current_recipes = matching_recipes

def show_selected_recipe(event):
    selected_indices = recipe_listbox.curselection()
    if selected_indices:
        selected_index = int(selected_indices[0])
        selected_recipe = current_recipes[selected_index]
        recipe_title.config(text=selected_recipe['title'])
        recipe_ingredients.config(text=f"Ingredients: {', '.join(selected_recipe['ingredients'])}")
        recipe_instructions.config(text=f"Instructions: {selected_recipe['instructions']}")
        recipe_meal_type.config(text=f"Meal Type: {selected_recipe['meal_type']}")
        recipe_rating.config(text=f"Rating: {selected_recipe['rating']}")
        recipe_image_path = selected_recipe.get("image")
        if recipe_image_path:
            try:
                recipe_image = Image.open(recipe_image_path)
                recipe_image = recipe_image.resize((80, 80), Image.Resampling.LANCZOS)
                recipe_image = ImageTk.PhotoImage(recipe_image)
                recipe_image_label.config(image=recipe_image)
                recipe_image_label.image = recipe_image
            except Exception as e:
                messagebox.showerror("Error", f"Error loading image: {e}")
                recipe_image_label.config(image='')
        else:
            recipe_image_label.config(image='')

def show_all_recipes():
    recipe_listbox.delete(0, tk.END)
    for recipe in recipes:
        recipe_listbox.insert(tk.END, recipe['title'])
    global current_recipes
    current_recipes = recipes

def add_new_recipe():
    def save_recipe():
        new_recipe = {
            "title": title_entry.get(),
            "ingredients": ingredients_entry.get().split(","),
            "instructions": instructions_entry.get(),
            "meal_type": meal_type_entry.get(),
            "rating": float(rating_entry.get()),
            "image": image_entry.get()
        }

        recipes.insert(0,new_recipe)

        with open('recipes.json', 'w') as file:
            json.dump(recipes, file, indent=4)

        recipe_listbox.insert(0, new_recipe['title'])
        recipe_listbox.selection_set(0)
        show_selected_recipe(None)
        update_ingredients_listbox()
        messagebox.showinfo("Success", "Recipe added successfully!")
        add_recipe_window.destroy()

    add_recipe_window = tk.Toplevel(app)
    add_recipe_window.title("Add Recipe")

    title_label = tk.Label(add_recipe_window, text="Title:")
    title_label.pack()
    title_entry = tk.Entry(add_recipe_window)
    title_entry.pack()

    ingredients_label = tk.Label(add_recipe_window, text="Ingredients (comma-separated):")
    ingredients_label.pack()
    ingredients_entry = tk.Entry(add_recipe_window)
    ingredients_entry.pack()

    instructions_label = tk.Label(add_recipe_window, text="Instructions:")
    instructions_label.pack()
    instructions_entry = tk.Entry(add_recipe_window)
    instructions_entry.pack()

    meal_type_label = tk.Label(add_recipe_window, text="Meal Type:")
    meal_type_label.pack()
    meal_type_entry = tk.Entry(add_recipe_window)
    meal_type_entry.pack()

    rating_label = tk.Label(add_recipe_window, text="Rating:")
    rating_label.pack()
    rating_entry = tk.Entry(add_recipe_window)
    rating_entry.pack()

    image_label = tk.Label(add_recipe_window, text="Image Path:")
    image_label.pack()
    image_entry = tk.Entry(add_recipe_window)
    image_entry.pack()

    save_button = tk.Button(add_recipe_window, text="Save Recipe", command=save_recipe)
    save_button.pack()

def delete_selected_recipe():
    selected_indices = recipe_listbox.curselection()
    if selected_indices:
        selected_index = int(selected_indices[0])
        selected_recipe = current_recipes[selected_index]
        result = messagebox.askyesno("Delete", f"Are you sure you want to delete the recipe '{selected_recipe['title']}'?")
        if result:
            recipes.remove(selected_recipe)
            with open('recipes.json', 'w') as file:
                json.dump(recipes, file, indent=4)
            update_recipe_listbox()
            update_ingredients_listbox()
            clear_recipe_details()
            messagebox.showinfo("Success", "Recipe deleted successfully!")
    else:
        messagebox.showwarning("Delete", "Please select a recipe to delete.")

def clear_recipe_details():
    recipe_title.config(text="Recipe Title")
    recipe_ingredients.config(text="Ingredients:")
    recipe_instructions.config(text="Instructions:")
    recipe_meal_type.config(text="")
    recipe_rating.config(text="")
    recipe_image_label.config(image='')

def update_recipe_listbox():
    recipe_listbox.delete(0, tk.END)
    for recipe in current_recipes:
        recipe_listbox.insert(tk.END, recipe['title'])


def update_ingredients_listbox():
    all_ingredients = sorted(set([ingredient for recipe in recipes for ingredient in recipe['ingredients']]))
    ingredients_listbox.delete(0, tk.END)
    for ingredient in all_ingredients:
        ingredients_listbox.insert(tk.END, ingredient)

app = tk.Tk()
app.title("Ingredient Chef")
app.geometry("1800x900")

background_image_path = r"c:\Users\Lenovo\Desktop\mispce\2nd year\sem4 2year\I2207\project\picture\vegetables-set-left-black-slate.jpg"
background_image = Image.open(background_image_path)
background_image = background_image.resize((1800, 1000), Image.Resampling.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)

background_label = tk.Label(app, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

title_font = ("Helvetica", 24, "bold")
subtitle_font = ("Helvetica", 16, "bold")
normal_font = ("Helvetica", 12)
button_font = ("Helvetica", 14, "bold")
background_color = "#4c4e4d"
accent_color = "#c30010"
entry_width = 40

title_label = tk.Label(app, text="Ingredient Chef", font=title_font, bg=background_color, fg="white")
title_label.pack(pady=20)

ingredient_frame = tk.Frame(app, bg=background_color)
ingredient_frame.pack(pady=20)

ingredients_label = tk.Label(ingredient_frame, text="Select Ingredient:", font=subtitle_font, bg=background_color, fg="white")
ingredients_label.grid(row=0, column=0, padx=10)

ingredients_scrollbar = tk.Scrollbar(ingredient_frame, orient=tk.VERTICAL)
ingredients_scrollbar.grid(row=0, column=2, sticky='ns')

all_ingredients = sorted(set([ingredient for recipe in recipes for ingredient in recipe['ingredients']]))
ingredients_listbox = tk.Listbox(ingredient_frame, selectmode=tk.SINGLE, height=10, font=normal_font, width=25, yscrollcommand=ingredients_scrollbar.set)
for ingredient in all_ingredients:
    ingredients_listbox.insert(tk.END, ingredient)
ingredients_listbox.grid(row=0, column=1, padx=10)
ingredients_listbox.bind("<<ListboxSelect>>", show_selected_ingredient)

ingredients_scrollbar.config(command=ingredients_listbox.yview)

add_recipe_button = tk.Button(ingredient_frame, text="Add Recipe", font=button_font, bg=accent_color, fg="white", command=add_new_recipe)
add_recipe_button.grid(row=1, column=0, pady=10)

show_all_button = tk.Button(ingredient_frame, text="Show All Recipes", font=button_font, bg=accent_color, fg="white", command=show_all_recipes)
show_all_button.grid(row=1, column=1, pady=10)

recipe_frame = tk.Frame(app, bg=background_color, height=100)
recipe_frame.pack(pady=20)

recipe_scrollbar = tk.Scrollbar(recipe_frame, orient=tk.VERTICAL)
recipe_scrollbar.pack(side=tk.LEFT, fill=tk.Y)


recipe_listbox = tk.Listbox(recipe_frame, height=100, font=normal_font, width=30)
recipe_listbox.pack(side=tk.LEFT, padx=20)
recipe_listbox.bind("<<ListboxSelect>>", show_selected_recipe)

recipe_scrollbar.config(command=recipe_listbox.yview)

delete_recipe_button = tk.Button(recipe_frame, text="Delete Recipe", font=button_font, bg=accent_color, fg="white", command=delete_selected_recipe)
delete_recipe_button.pack(side=tk.BOTTOM, pady=10)

recipe_details_frame = tk.Frame(recipe_frame, bg=background_color)
recipe_details_frame.pack(side=tk.LEFT, padx=20)

recipe_title = tk.Label(recipe_details_frame, text="Recipe Title", font=subtitle_font, bg=background_color, fg="white")
recipe_title.pack(pady=10)

recipe_ingredients = tk.Label(recipe_details_frame, text="Ingredients:", font=subtitle_font, wraplength=500, justify=tk.LEFT, bg=background_color, fg="white")
recipe_ingredients.pack(pady=5)

recipe_instructions = tk.Label(recipe_details_frame, text="Instructions:", font=normal_font, wraplength=500, justify=tk.LEFT, bg=background_color, fg="white")
recipe_instructions.pack(pady=5)

recipe_meal_type = tk.Label(recipe_details_frame, text="", font=normal_font, bg=background_color, fg="white")
recipe_meal_type.pack(pady=5)

recipe_rating = tk.Label(recipe_details_frame, text="", font=normal_font, bg=background_color, fg="white")
recipe_rating.pack(pady=5)

recipe_image_label = tk.Label(recipe_details_frame, bg=background_color)
recipe_image_label.pack(pady=10, side=tk.RIGHT, padx=30)

current_recipes = recipes
for recipe in current_recipes:
    recipe_listbox.insert(tk.END, recipe['title'])

app.mainloop()
