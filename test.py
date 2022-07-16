import json

raw_file_name = 'Dhaka-Bangladesh.json'
fixed = 'Dhaka-Bangladesh_fixed.json'

def read_strange_json(in_file: str) -> dict[str, str]:
    with open(in_file) as in_f:
        return json.loads(json.loads(in_f.read()))
    
def write_new_json(dict: dict[str, str], out_file: str) -> None:
    with open(out_file, "w") as out_f:
        json.dump(dict, out_f, indent = 4)

d = read_strange_json(raw_file_name)
write_new_json(d, fixed)