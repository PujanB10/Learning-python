def read_files(file_name):
    result=[]
    names=[]
    index=0
    contents=[]
    with open(file_name) as new_files:
        for lines in new_files:
            lines=lines.strip()
            if lines=="":
                names.append(contents)
                contents=[]
                continue
            contents.append(lines)
    names.append(contents)
    return names

def search_by_name(filename: str, word: str):
    names=[]
    with open(filename) as new_file:
        for lines in new_file:
            if word.lower() in lines.lower() and lines!=lines.lower():
                names.append(lines.strip())
    return names

def search_by_time(filename: str, prep_time: int):
    result=[]
    names=read_files(filename)
    for items in names:
        if int(items[1])<=prep_time:
            result.append(f"{items[0]}, preparation time {items[1]} min")
    return result

def search_by_ingredient(filename: str, ingredient: str):
    result=[]
    names=read_files(filename)
    for items in names:
        if ingredient in items:
            result.append(f"{items[0]}, preparation time {items[1]} min")
    return result


if __name__ == "__main__":
    found_recipes=search_by_name("recipes2.txt", "oat")
    for recipe in found_recipes:
        print(recipe)

    found_recipes_by_time = search_by_time("recipes1.txt", 20)
    for items in found_recipes_by_time:
        print(items)

    found_recipes = search_by_ingredient("recipes1.txt", "eggs")
    for recipe in found_recipes:
        print(recipe)
