from bs4 import BeautifulSoup


req = Request("https://en.wikipedia.org/wiki/Python_(programming_language)")
html_page = urlopen(req)

soup = BeautifulSoup(html_page, "html.parser")

html_text = soup.get_text()

f = open("html_text.txt", "w")

for line in html_text:
	f.write(line)

f.close()