file_path = "map.txt"

with open(file_path, 'r', encoding='utf-8') as file:
    for row in file:
        print(row.strip())
