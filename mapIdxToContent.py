file_path = "map.txt"
txt="def idxtoContent(idx):\n  match idx:\n"
with open(file_path, 'r', encoding='utf-8') as file:
    for row in file:
        idx=int(row.split(".")[0].split(" ")[1])
        content=row.split(".")[1].replace("\n","")
        txt+=f"    case {idx}:\n         return '{content}'\n"
f=open("map_idx_to_content.py","w",encoding="utf-8")
f.write(txt)