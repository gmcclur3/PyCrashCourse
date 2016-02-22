rivers = {
    'nile': 'egypt',
    'delaware': 'usa',
    'amazon': 'brazil',
}

for river, country in sorted(rivers.items()):
    print("The " + river +
          " runs through " + country + ".")

for river in sorted(rivers.keys()):
    print(river)

for country in sorted(rivers.values()):
    print(country)

