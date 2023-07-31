from bs4 import BeautifulSoup
import requests
import json

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
for a in link_div.find_all("a", href=True):
    chapterLinks.append(a["href"])

# To get all chapters data and store it

chapterNo = 0

chapterData = {
    "Chapter": "Chapter" + str(chapterNo + 1),
    "data": {"Header": "", "Paragraph": []},
}


# def getChaptersData():
#     for headerText in info.find_all("h2"):
#         chapterData["data"]["Header"] = headerText.text.strip()
#         while (
#             headerText.next_sibling is not None and headerText.next_sibling.name != "h2"
#         ):
#             if headerText.next_sibling.name == "p":
#                 temp = headerText.next_sibling.get_text().strip()
#                 chapterData["data"]["Paragraph"].append(temp)
#             headerText = headerText.next_sibling
#     return chapterData


# def storeChapterData(chapterData):
#     with open("CharakaSamhita.txt", "w", encoding="utf-8") as file:
#         file.write(chapterData["Chapter"] + "\n")
#         file.write(chapterData["data"]["Header"] + "\n")
#         for para in chapterData["data"]["Paragraph"]:
#             file.write(para + "\n")

data = []

def getChaptersDatainJson():
    for headerText in info.find_all("h2"):
        header = headerText.text.strip()
        paragraph = []
        while (
            headerText.next_sibling is not None and headerText.next_sibling.name != "h2"
        ):
            if headerText.next_sibling.name == "p":
                paragraph.append(headerText.next_sibling.get_text().strip())
            headerText = headerText.next_sibling
        data.append({"ChapterNo":  "ChapterNo" + str(chapterNo+1), "Header": header, "Paragraph": paragraph})
    return data

def storeInJson(chapterData):
    with open("test.json", "w", encoding="utf-8") as file:
        json.dump(chapterData, file, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    for chapter in chapterLinks:
        chapterNo += 1
        url = "https://www.wisdomlib.org" + chapter
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.text, "html.parser")
        info = soup.find(id="scontent")
        abcd = getChaptersDatainJson()
        storeInJson(abcd)



# To get all chapters data and store it in josn file   ##### correctly working