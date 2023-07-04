file_path = "map.txt"
txt="def ContentToIdx(content):\n  match content:\n"
with open(file_path, 'r', encoding='utf-8') as file:
    for row in file:
        idx=int(row.split(".")[0].split(" ")[1])
        content=row.split(".")[1].replace("\n","")
        txt+=f"    case '{content}':\n         return {idx}\n"
f=open("map_content_to_id.py","w",encoding="utf-8")
f.write(txt)