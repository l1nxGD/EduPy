from csv import reader
import xml.dom.minidom as minidom
from os import write

#'''
with open('books.csv', 'r', encoding='windows-1251') as csvfile:
    table = list(reader(csvfile, delimiter=';'))

def searchAuthor(author, table):
    listAuthor = []
    for row in table:
        if '2015' in row[6] or '2018' in row[6]:
            lower_case = row[3].lower()
            index = lower_case.find(author.lower())
            if index != -1:
                listAuthor.append(row)
    if len(listAuthor) > 0:
        return listAuthor
    else:
        return ("Книга с данным авторм не найдена")

def lengthName(table):
    k = 0
    for i in range(1, len(table)):
        if len(table[i][1]) >= 30:
            k += 1
    return k

def ratingBook(table):
    count = 0
    listBooks = []
    maxRating = 0
    for i in range(1, len(table)):
        if int(table[i][8]) > maxRating:
            maxRating = int(table[i][8])
    for i in range(1, len(table)):
        if int(table[i][8]) >= maxRating and count < 20:
            listBooks.append(table[i])
    return listBooks

def catalogBooks(table):
    counter = 0
    output = open('result.txt', 'w')
    for i in range(10, 30):
        counter += 1
        output.write(f'{counter}. {table[i][3]} "{table[i][1]}" {table[i][6]}\n')
    output.close()

def listOfTags(table):
    tags = []
    for i in range(1, len(table)):
        tags.append(int(table[i][0]))
    return set(tags)

search = input('Enter author: ')
print(searchAuthor(search, table))
print(f"Название > 30 символов: {lengthName(table)}")
catalogBooks(table)
for book in ratingBook(table):
    print(book)
print(listOfTags(table))
#'''

#xml_file = open('currency.xml', 'r', encoding="windows-1251")
#xml_data = xml_file.read()

#dom = minidom.parseString(xml_data)
dom = minidom.parse("currency.xml")
dom.normalize()

elemets = dom.getElementsByTagName('Valute')

charCode = {}
code = ''
nominal = ''

for node in elemets:
    for child in node.childNodes:
        if child.nodeType == 1:
            if child.tagName == 'CharCode':
                if child.firstChild.nodeType == 3:
                    code = (child.firstChild.data)
            if child.tagName == 'Nominal':
                if child.firstChild.nodeType == 3:
                    nominal = int(child.firstChild.data)
    charCode[code] = nominal

print(charCode)
#xml_file.close()
#'''
