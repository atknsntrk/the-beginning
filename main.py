from selenium import webdriver
from mdutils import Html
from mdutils.mdutils import MdUtils

from selenium.webdriver.common.by import By

class Main:

    url = "https://lightnovelpub.fan/novel/the-beginning-after-the-end-548/chapter-401-30041322"



    url_split = url.split("/")[5].split('-')
    chapter_name = url_split[0].capitalize() + " " +url_split[1]
    file_name = chapter_name + ".txt"

    #my_pub = pypub.Epub(chapter_name);
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome("C:\\Users\\ataka\\Documents\\fun\\the-beginning\\chromedriver_win32\\chromedriver.exe", options=op)

    driver.get(url)

    chapter = driver.find_element(By.ID, "chapter-container")
    parts = chapter.text.splitlines()
    chapter_title = parts[0]

    print(type(parts[0]))

    mdFile = MdUtils(file_name=chapter_title, title=chapter_title)

    mdFile.new_header(level=1, title=chapter_title)

    for part in parts:
        mdFile.new_paragraph(part) 
    mdFile.create_md_file()
    driver.quit()

