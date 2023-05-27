from selenium import webdriver
from mdutils import Html
from mdutils.mdutils import MdUtils
import sys
import os
from selenium.webdriver.common.by import By

class Main:

    url = sys.argv[1] if len(sys.argv) >= 2 else  "https://lightnovelpub.fan/novel/the-beginning-after-the-end-548/chapter-401-30041322"

    print(url)
    
    url_split = url.split("/")[5].split('-')
    chapter_name = url_split[0].capitalize() + " " +url_split[1]

    folder_name = 'chapters/'

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    file_name = folder_name + chapter_name

    os.path.abspath(folder_name)
    #my_pub = pypub.Epub(chapter_name);
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(options=op)

    driver.get(url)

    chapter = driver.find_element(By.ID, "chapter-container")
    parts = chapter.text.splitlines()
    chapter_title = parts[0]
    parts.pop()

    mdFile = MdUtils(file_name=file_name)

    for part in parts:
        mdFile.new_paragraph(part) 
    mdFile.create_md_file()
    driver.quit()

