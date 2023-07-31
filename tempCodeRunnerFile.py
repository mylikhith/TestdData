all("h2"):
    print(headerText.text)
    while headerText.next_sibling is not None and headerText.next_sibling.name != "h2":
        if headerText.next_sibling.name == "p":
            print(headerText.next_sibling.get_text().strip())
        headerText = headerText.next_sibling