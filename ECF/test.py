import json
import pandas as pd
# Large data
large_data = [{'name': 'John', 'age': i} for i in range(1000000)]
data = [{'name': 'John', 'age': 30}, {'name': 'John', 'age': 30}]
dict = {'name': 'John', 'age': 30}
# Write large data to a file in chunks

#
# with open("resultat.json", mode='a', encoding='utf-8') as fichier_json:
#     # Écrire le dictionnaire dans le fichier JSON
#     json.dump(data, fichier_json, ensure_ascii=False, indent=4)
with open('resultat.json', 'r') as f:
  dd = json.load(f)
f.close()


print(dd)
print(len(dd))
dd.append(dict)

with open('resultat.json', 'w',) as fz:
  json.dump(dd, fz,ensure_ascii=False, indent=4)


print('new')
print(dd)
print(len(dd))