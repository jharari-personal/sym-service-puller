import json

languages = ["ara","chs","cht","deu","esp","fra","gre","heb","ita"]

def process_json(json_data):
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            if key == "Color_Light":
                json_data[key] = "#" + value
            elif key == 'Color_Dark':
                json_data[key] = "#" + value
            elif isinstance(value, str):
                try:
                    value = json.loads('"' + value + '"')
                    json_data[key] = value
                except:
                    pass
            elif isinstance(value, (dict, list)):
                process_json(value)
    elif isinstance(json_data, list):
        for item in json_data:
            process_json(item)

def main():
    for i in languages:
        input_file_path = f"{i} cat.json"
        output_file_path = f"{i} cat.json"

        with open(input_file_path, "r", encoding="utf=8") as input_file:
            data = json.load(input_file)

        process_json(data)

        with open(output_file_path, "w", encoding="utf=8") as output_file:
            json.dump(data, output_file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    main()

