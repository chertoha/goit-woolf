from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, DuplicateKeyError


def get_db():
    try:
        client = MongoClient("mongodb://localhost:27017", serverSelectionTimeoutMS=2000)
        client.admin.command('ping')
        db = client["cats_db"]
        return db
    except ConnectionFailure:
        print("Не вдалося підключитися до MongoDB")
        return None

# ==================== CREATE ====================
def create_cat(name, age, features):
    db = get_db()
    if db is not None:
        try:
            cat = {"name": name, "age": age, "features": features}
            result = db.cats.insert_one(cat)
            print(f"Кота додано з id: {result.inserted_id}")
        except Exception as e:
            print(f"Помилка при створенні: {e}")

# ==================== READ ====================
def get_all_cats():
    db = get_db()
    if db is not None:
        cats = db.cats.find()
        for cat in cats:
            print(cat)

def get_cat_by_name(name):
    db = get_db()
    if db is not None:
        cat = db.cats.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print("Кота не знайдено")

# ==================== UPDATE ====================
def update_cat_age(name, new_age):
    db = get_db()
    if db is not None:
        result = db.cats.update_one({"name": name}, {"$set": {"age": new_age}})
        print(f"Оновлено: {result.modified_count} документ(ів)")

def add_feature_to_cat(name, new_feature):
    db = get_db()
    if db is not None:
        result = db.cats.update_one({"name": name}, {"$addToSet": {"features": new_feature}})
        print(f"Додано характеристику: {result.modified_count} документ(ів)")

# ==================== DELETE ====================
def delete_cat_by_name(name):
    db = get_db()
    if db is not None:
        result = db.cats.delete_one({"name": name})
        print(f"Видалено: {result.deleted_count} документ(ів)")

def delete_all_cats():
    db = get_db()
    if db is not None:
        result = db.cats.delete_many({})
        print(f"Усі коти видалені: {result.deleted_count} документ(ів)")

# ==================== MAIN ====================
if __name__ == "__main__":
    create_cat("Barsik", 3, ["рудий", "грає з мишкою"])
    get_all_cats()
    get_cat_by_name("Barsik")
    update_cat_age("Barsik", 4)
    add_feature_to_cat("Barsik", "любить лазити по шторам")
    delete_cat_by_name("Barsik")
    delete_all_cats()
