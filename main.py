#import pypub

from selenium import webdriver

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


    #element = driver.find_element(By.ID, "chapter-container")
    chapter = driver.find_element(By.ID, "chapter-container")
    parts = chapter.text.splitlines()
    chapter_title = parts[0]
    parts.pop(0)
    print(parts)
    #soup = BeautifulSoup(response.content, "lxml")
    
    #links = soup.find_all('a')

    #print(soup)


    with open("C:\\Users\\ataka\\Documents\\fun\\the-beginning\\" + file_name, "w", encoding="utf8") as my_file:
        my_file.write(chapter.text)

    driver.quit()
        