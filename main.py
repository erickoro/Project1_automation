from modules.book import Book
from modules.magazine import Magazine
from modules.dvd import Dvd
from modules.cd import Cd
from modules.catalog import Catalog
import json

book1 = Book(
    'ini title',
    'ini subject',
    None,
    '3289-0394',
    'Ericko',
    '081182937925'
)

book2 = Book(
    'ini title',
    'ini subject',
    None,
    '3289-0394',
    'Ericko',
    '081182937925'
)

book3 = Book(
    'ini title',
    'ini subject',
    None,
    '3289-0394',
    'Ericko',
    '081182937925'
)


magazine1 = Magazine(
    'media cnn indonesia',
    'edisi 14 Juli 2023',
    None,
    'volume 1',
    '-'
)

magazine2 = Magazine(
    'cnbc',
    'edisi 15 Juli 2023',
    None,
    'volume 1',
    '-'
)

dvd1 = Dvd(
    'Test dvd 1',
    'subject test dvd 1',
    None,
    None,
    None,
    'Comedy'
)

cd1 = Cd(
    'Test cd 1',
    'Subject test cd 1',
    None,
    None
)

# collect data per jenis
book = [book1,book2,book3]
magazine = [magazine1,magazine2]
dvd = [dvd1]
cd = [cd1]

# get data from json
f = open('files/catalog.json')
data_json = json.load(f)

# create object from json data
for item in data_json:
    if item['source'] == 'magazine':
        magazine.append(Magazine(
            title=item['title'],
            subject=item['title'],
            upc=item['title'],
            volume=item['title'],
            issue=item['title']
        ))
    elif item['source'] == 'book':
        book.append(Book(
            title=item['title'],
            subject=item['subject'],
            upc=item['upc'],
            issbn=item['issbn'],
            authors=item['authors'],
            dds_number=item['dds_number']
        ))
    elif item['source'] == 'dvd':
        dvd.append(Dvd(
            title=item['title'],
            subject=item['subject'],
            upc=item['upc'],
            actors=item['actors'],
            director=item['director'],
            genre=item['genre']
        ))
    elif item['source'] == 'cd':
        cd.append(Cd(
            title=item['title'],
            subject=item['subject'],
            upc=item['upc'],
            artist=item['artist']
        ))

# collect all data
catalog_all = [book,magazine,dvd,cd]

# run search & result

input_search = input('input_search: ')
results = Catalog(catalog_all).search(input_search)
if results:
    for index, result in enumerate(results):
        print(f"result ke-{index+1} | {result}")
else:
    print('No result :(')