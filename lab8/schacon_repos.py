#!/usr/bin/env python3

import json

with open('schacon.repos.json', 'r') as file:
    data = json.load(file)

with open('chacon.csv', 'w') as csv_file:
  for repo in data[:5]:
    name = repo["name"]
    html_url = repo["html_url"]
    updated_at = repo["updated_at"]
    visibility = repo["visibility"]
    csv_file.write(f"{name},{html_url},{updated_at},{visibility}\n")

with open('chacon.csv', 'r') as csv_file:
    print(csv_file.read())

