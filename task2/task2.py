from pymongo import MongoClient

# Підключення до MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["cats_db"]
collection = db["cats"]

# Create - Додавання нового запису
def create_cat(name, age, features):
    try:
        cat = {"name": name, "age": age, "features": features}
        result = collection.insert_one(cat)
        print(f"Cat added with ID: {result.inserted_id}")
    except Exception as e:
        print(f"Error creating cat: {e}")

# Read - Отримання всіх записів
def read_all_cats():
    try:
        cats = collection.find()
        for cat in cats:
            print(cat)
    except Exception as e:
        print(f"Error reading cats: {e}")

# Read - Отримання кота за ім'ям
def read_cat_by_name(name):
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print("Cat not found")
    except Exception as e:
        print(f"Error reading cat by name: {e}")

# Update - Оновлення віку кота за ім'ям
def update_cat_age(name, new_age):
    try:
        result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.matched_count > 0:
            print(f"Cat's age updated for: {name}")
        else:
            print("Cat not found")
    except Exception as e:
        print(f"Error updating cat age: {e}")

# Update - Додавання нової характеристики коту за ім'ям
def add_feature_to_cat(name, new_feature):
    try:
        result = collection.update_one({"name": name}, {"$addToSet": {"features": new_feature}})
        if result.matched_count > 0:
            print(f"Feature added for cat: {name}")
        else:
            print("Cat not found")
    except Exception as e:
        print(f"Error adding feature to cat: {e}")

# Delete - Видалення кота за ім'ям
def delete_cat_by_name(name):
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count > 0:
            print(f"Cat deleted: {name}")
        else:
            print("Cat not found")
    except Exception as e:
        print(f"Error deleting cat: {e}")

# Delete - Видалення всіх записів
def delete_all_cats():
    try:
        result = collection.delete_many({})
        print(f"Deleted {result.deleted_count} cats from collection")
    except Exception as e:
        print(f"Error deleting all cats: {e}")

if __name__ == "__main__":
    # Створити кота
    create_cat("barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])

    # Отримати всі записи
    read_all_cats()

    # Отримати кота за ім'ям
    read_cat_by_name("barsik")

    # Оновити вік кота
    update_cat_age("barsik", 4)

    # Додати нову характеристику
    add_feature_to_cat("barsik", "грає з м'ячиком")

    # Видалити кота за ім'ям
    delete_cat_by_name("barsik")

    # Видалити всі записи
    delete_all_cats()
