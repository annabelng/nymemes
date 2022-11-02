import csv

# set up directories 
data_dir = '/data/new-yorker/'
html_dir = data_dir + 'raw-html/'
caption_dir = data_dir + 'captions/'
image_dir = data_dir + 'images-raw/'

# grabbing valid htmls
valid_htmls = []
with open(data_dir + 'valid_htmls.txt','r') as valid:
    for line in valid:
        valid_htmls.append(line.strip())

# header = ['image','text']
# with open(data_dir + 'image_dataset.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(header)
#     for html in valid_htmls:
#         # writing image file path
#         row = []
#         row.append(html[:-5] + '.jpg')

#         # writing caption
#         with open(caption_dir + html[:-5] + '.txt', 'r') as g:
#             caption = g.read()
#             caption = caption.replace('"', '')
#             caption = caption.replace('"', '')
#             row.append(caption)
#             # f.write(caption)
#         writer.writerow(row)

with open(image_dir + 'metadata.jsonl', 'w') as f:
    for html in valid_htmls:
        line = '{\"file_name\": \"' + html[:-5] + '.jpg\", \"text\": \"'
        with open (caption_dir + html[:-5] + '.txt', 'r') as g:
            caption = g.read()
            caption = caption.replace('"','')
            line += caption
            line += '\"}\n'
            line = str(line)
            f.write(line)
