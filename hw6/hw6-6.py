def get_recipe(path, search_id):
    with open(path, "r") as fh:
        recipe_info = None
        for k in fh:
            line = k.rstrip("\n").split(",")
            if line[0] != search_id:
                continue
            
            ingredients = []

            for i in range(len(line)):
                if i > 1:
                    ingredients.append(line[i])

            recipe_info = {
                "id": line[0],
                "name": line[1],
                "ingredients": ingredients
                }
        
        return recipe_info