import internetarchive
import time
import os

error_log = open('IA_download_errors.log', 'a')

identifiers = [] #creating a list to hold all the identifers

# Specify destination directories
text_destination_directory = './data/text'
pdf_destination_directory = './data/pdf'

# Create the directories if they don't exist
os.makedirs(text_destination_directory, exist_ok=True)
os.makedirs(pdf_destination_directory, exist_ok=True)


#conducting a search to isolate the identifiers of all of the Hatchets published in 1964
search = internetarchive.search_items('collection:gwulibraries AND title:Hatchet AND date:1964')
for result in search:
   identifier = (result['identifier'])
   identifiers.append(identifier)

# provide an identifier and recieve the item to download the text and PDF files
def download_items(identifier):
    item = internetarchive.get_item(identifier)
    text = item.get_file(identifier + '_djvu.txt')
    pdf = item.get_file(identifier + '.pdf')
    try:
        text.download(destdir=text_destination_directory)
        pdf.download(destdir=pdf_destination_directory)
    except:
        error_log.write(identifier)
    else:
        print("downloading: " + identifier)
        time.sleep(1)


#downloading pdf and txt files for each file associated with our list of identifiers
for identifier in identifiers:
    download_items(identifier)
