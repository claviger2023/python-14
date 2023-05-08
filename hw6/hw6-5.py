def get_cats_info(path):
    result_list = []
    with open(path, "r") as fh:
        for k in fh:
            line = k.rstrip("\n").split(",")
            cat_info = {
                "id": line[0],
                "name": line[1],
                "age": line[2]
            }
            result_list.append(cat_info)

    return result_list