from bs4 import BeautifulSoup
from csv import writer

# set up directories 
data_dir = '/data/new-yorker/'
html_dir = data_dir + 'raw-html/'
caption_dir = data_dir + 'captions/'

# grabbing valid htmls
valid_htmls = []
with open(data_dir + 'valid_htmls.txt','r') as valid:
    for line in valid:
        valid_htmls.append(line.strip())

# looping through htmls and scraping captions
for html in valid_htmls:
    with open(html_dir + html) as fp:
        soup = BeautifulSoup(fp, 'html.parser')

        caption = soup.find('div', attrs={'class': 'mega-caption read-more'})
        caption = caption.text.strip()
    
    # writing caption to txt file
    with open(caption_dir + html[:-5] + '.txt', 'w') as f:
        caption = caption.replace('“', '')
        caption = caption.replace('”', '')
        f.write(caption)