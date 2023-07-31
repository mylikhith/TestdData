from bs4 import BeautifulSoup
import requests

websiteUrl = "https://www.wisdomlib.org/hinduism/book/charaka-samhita-english"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
}


page = requests.get(websiteUrl, headers=headers)
soup = BeautifulSoup(page.text, "html.parser")

# To get all chapters links

chapterLinks = []

link_div = soup.find(id="indexList")

links = soup.select("div.py-1.py-md-0.il-cont.cvc")
for a in link_div.find_all('a', href=True):
    chapterLinks.append(a['href'])

# To get all chapters data and store it 

def getChaptersData(chapterLinks):

    url = "https://www.wisdomlib.org" + chapterLinks[0]

    info = soup.find(id="scontent")

    for headerText in info.find_all("h2"):

        data = {
            "Header": headerText.text,
            "Paragraph": []
        }

        while headerText.next_sibling is not None and headerText.next_sibling.name != "h2":
            if headerText.next_sibling.name == "p":
                temp = headerText.next_sibling.get_text().strip()
                data["Paragraph"].append(temp)
            headerText = headerText.next_sibling
        chapterData["data"].append(data)
    return chapterData


def storeChapterData(chapterData):
    with open('CharakaSamhita.txt', 'w', encoding="utf-8") as file:
        for data in chapterData:
            file.write(data["Chapter"] + "\n")
            for d in data["data"]:
                file.write(d["Header"] + "\n")
                for p in d["Paragraph"]:
                    file.write(p + "\n")
                file.write("\n")
            file.write("\n")

if __name__ == "__main__":
    chapterData = getChaptersData(chapterLinks)
    storeChapterData(chapterData)