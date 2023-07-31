from bs4 import BeautifulSoup
import requests
import pandas as pd


# url = "https://www.wisdomlib.org/hinduism/book/charaka-samhita-english/d/doc627511.html"
# url = "https://www.wisdomlib.org/hinduism/book/charaka-samhita-english/d/doc627511.html"
url = "https://www.wisdomlib.org/hinduism/book/charaka-samhita-english"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
}

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, "html.parser")
# print(soup.prettify())

info = soup.find(id="scontent")
# print(info.prettify())

heading = soup.find_all("h2")
# print(heading)

headers_table = [h.text for h in heading]
# print(headers_table)

df = pd.DataFrame(columns=headers_table)
# print(df)

# for h in heading:
#     print(h.find_all('p'))


# para = soup.find_all("p")
# print(para)

###################################################################################################################

link_div = soup.find(id="indexList")
chapterLinks = []

links = soup.select("div.py-1.py-md-0.il-cont.cvc")
for a in link_div.find_all('a', href=True):
    chapterLinks.append(a['href'])

print(chapterLinks)
################################################################################################################### imp

data = []

def get_data():
    for headerText in info.find_all("h2"):
        print(headerText.text)
        data.append(headerText.text.strip())
        while headerText.next_sibling is not None and headerText.next_sibling.name != "h2":
            if headerText.next_sibling.name == "p":
                print(headerText.next_sibling.get_text().strip())
                data.append(headerText.next_sibling.get_text().strip())
            headerText = headerText.next_sibling
    return data

def store_data(data):
    with open("output.txt", "w", encoding="utf-8") as f:
        for d in data:
            f.write(d + "\n")

if __name__ == "__main__":

    for chapter in chapterLinks:
        url = "https://www.wisdomlib.org" + chapter
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.text, "html.parser")
        info = soup.find(id="scontent")
        Data = get_data()
        store_data(Data)
###################################################################################################################

# for i in info.find_all("h2", "p"):
#     print({"i.text": i.text})

###################################################################################################################

# headers = soup.find_all('h2')
# header_paragraph_pairs = []

# for header in headers:
#         # Extract the text of the header
#         header_text = header.get_text().strip()

#         # Find the next sibling elements until the next h2 header is encountered
#         next_element = header.next_sibling
#         paragraph_texts = []
#         while next_element is not None and next_element.name != 'h2':
#             if next_element.name == 'p':
#                 paragraph_texts.append(next_element.get_text().strip())
#             next_element = next_element.next_sibling

#         # Store the header-paragraph pair as a tuple
#         header_paragraph_pairs.append((header_text, paragraph_texts))

# print(header_paragraph_pairs)

###################################################################################################################


# first_h2_header = info.find('h2')

#     # Find all preceding p elements
# preceding_paragraphs = first_h2_header.find_all_previous('p')

# for paragraph in preceding_paragraphs:
#     paragraph_text = paragraph.get_text().strip()
#     print(paragraph_text)

###################################################################################################################

# link_div = soup.find(id="indexList")
# chapterLinks = []

# links = soup.select("div.py-1.py-md-0.il-cont.cvc")
# for a in link_div.find_all('a', href=True):
#     chapterLinks.append(a['href'])

# print(chapterLinks)


# To get all the links and store them in a text file #### corredctly working