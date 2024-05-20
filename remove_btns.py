
from bs4 import BeautifulSoup

# Load the HTML file
with open('page.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Find all button tags and remove them
buttons = soup.find_all('button')
for button in buttons:
    button.decompose()

# Save the modified HTML back to the file
with open('page.html', 'w', encoding='utf-8') as file:
    file.write(str(soup))
