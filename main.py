from selenium import webdriver
#from mdutils.mdutils import MdUtils
import sys
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pypub

class Main:

    url = sys.argv[1] if len(sys.argv) >= 2 else "https://lightnovelpub.fan/novel/the-beginning-after-the-end-web-novel-25052147/chapters?page=5"

    folder_name = 'chapters'

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


    my_pub = pypub.Epub("TBATE");
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    print(os.path.exists("chromedriver_mac64/chromedriver"))
    driver = webdriver.Chrome("chromedriver_mac64/chromedriver",options=op)

    driver.get(url)

    #chapter = driver.find_element(By.ID, "chapter-container")
    #parts = chapter.text.splitlines()
    #chapter_title = parts[0]
    #parts.pop()

    chapter_list = driver.find_element(By.CLASS_NAME, "chapter-list ")
    chapters = chapter_list.find_elements(By.TAG_NAME, "a")
    links = [a.get_attribute('href') for a in chapters ]
    for current_link in links:
        
        driver.get(current_link)
        chapter = driver.find_element(By.ID, "chapter-container")
        parts = chapter.text.splitlines()
        link_split = current_link.split("/")[5].split('-')

        chapter_name = link_split[0].capitalize() + " " +link_split[1]
        file_name = folder_name+ "/" + chapter_name

        '''mdFile = MdUtils(file_name=file_name)
        

        for part in parts:
            mdFile.new_paragraph(part)'''
        
        a = '/n'.join(parts)
        ch = pypub.Chapter(a, file_name)
        my_pub.add_chapter(ch)
        #mdFile.create_md_file()
        my_pub.create_epub("/Users/goldroger/Fuuun/tools/the-beginning/")
    driver.quit()
