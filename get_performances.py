from bs4 import BeautifulSoup

# Load the HTML file
with open('page.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Find all span tags and extract their text
a_tags = soup.find_all('a', class_='link font-body-md')
a_texts = [a.get_text() for a in a_tags]
fcis=[element for element in a_texts if element != '']

# Find all a tags and extract their text (plus sanitize list)
spans = soup.find_all('span')
span_texts = [span.get_text() for span in spans]
clean_spans=[element for element in span_texts if element != '']
cleanest_spans=[element for element in clean_spans if element != ' ']
performances=[element for element in cleanest_spans if element != '  ']

#Zip lists, for every three performance indicators, save the fci name
fci_performances = []
len_performances = len(performances)
indexB = 0

for a in fcis:
    fci_performances.append(a)
    
    for _ in range(3):
        if indexB < len_performances:
            fci_performances.append(performances[indexB])
            indexB += 1
        else:
            break

#Print list 
for text in fci_performances:
    print(text)
