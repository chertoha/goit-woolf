from pprint import pprint

def get_cats_info(path):

    try: 
        with open(path, "r", encoding="utf-8") as fh:
            cats = []
            for line in fh:
                id, name, age = line.strip().split(",")
                cats.append({"id":id, "name":name, "age":int(age)})
                
        return cats
    except FileNotFoundError:
        return "No file"
    except Exception as err:
        return err





if __name__ == "__main__":
    pprint(get_cats_info("./data/cats.txt"), indent=4)





    
