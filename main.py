import requests
import bs4
import json

URL = 'https://umod.org/documentation/games/rust/definitions'
OUTPUT = 'output.json'

response = requests.get(URL)

if response.status_code != 200:
    print("Failed to fetch.")
    exit(1)

soup = bs4.BeautifulSoup(response.content, 'html.parser')
skins_section = soup.find(attrs={'data-name': "Rust Skins"})

if skins_section is None:
    print("Failed to find skin section.")
    exit(1)

elements = list(skins_section.next_siblings)
items = [
    {
        'Item Shortname': t.h2.contents[0].split('(')[0].strip(),
        'Skins': [int(x.contents[0]) for x in ids.tbody.find_all(class_='col-1')],
    }
    for (t, ids) in zip(elements[::2], elements[1::2])
]

try:
    with open(OUTPUT, 'w') as f:
        f.write(json.dumps(items, indent=4))
        print("Items were written to %s" % OUTPUT)
except Exception as err:
    print("An error occurred when writing to %s" % OUTPUT)
    print(err)
