import json

input = """
[ 
    { "id": "001",
      "x": "2",
      "name": "Ifeanyi"
    },
    { "id": "002",
      "x": "7",
      "name" : "Chidinma"
    }
]
"""

data = json.loads(input)
print("User count ", len(data))
for item in data:
    print("Name", item['name'])
    print('ID', item['id'])