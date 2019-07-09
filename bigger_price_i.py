def bigger_price(limit, data):

    lista2=sorted(data, key=lambda x:x['price'], reverse=True)
    lista3=lista2[:limit]
    return lista3

# bloque principal

data=[
    {"name": "bread",
     "price": 100
     },
    {"name": "wine",
     "price": 138
     },
    {"name": "meat",
     "price": 15
     },
    {"name": "water",
     "price": 1
     }
]

print(bigger_price(2, data))
