import json

cities = [
    {'rank': 1, 'city': '上海', 'population': 24150000},
    {'rank': 2, 'city': 'カラチ', 'population': 24150000},
    {'rank': 3, 'city': '北京', 'population': 24150000},
]

with open('top_cities.json', 'w') as f:
    json.dump(cities, f)
print(json.dumps(cities, ensure_ascii=False, indent=2))