import argparse

from bs4 import BeautifulSoup


parser = argparse.ArgumentParser()
parser.add_argument('file', nargs='?', help='location of the html file to process')
args = parser.parse_args()

with open(args.file, encoding="utf8") as page:
    soup = BeautifulSoup(page, "html.parser")

html_text = soup.get_text()

f = open("html_text.txt", "w")

for line in html_text:
    f.write(line)

f.close()

print("Succesfully written output to html_text.txt")
