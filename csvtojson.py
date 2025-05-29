import csv
import json
#Converts csv file to json file
def csv_to_json(csv_filepath, json_filepath):
    data = []
    with open(csv_filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)

    
    with open(json_filepath, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    csv_to_json('profiles1.csv', 'data.json')
    print("Csv file converted to json successfully")
        