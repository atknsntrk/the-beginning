#import pypub

from selenium import webdriver
from mdutils import Html
from mdutils.mdutils import MdUtils

from selenium.webdriver.common.by import By

class Main:
    def array_to_html(arr):
        title = arr[0]
        text = '\n'.join(arr[1:])
        a = ""
        for part in arr[1:]:
            a += f"<p>{part}</p>"
        html = f'''
        <html>
        <head>
        <title>{title}</title>
        <style>
        body {{
            background-color: darkgrey;
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 0;
            padding: 0;
        }}

        .container {{
            text-align: center;
            background-color: #f1f1f1;
            padding: 20px;
            border-radius: 10px;
        }}
        </style>
        </head>
        <body>
        <h1>{title}</h1>
        {a}
        </body>
        </html>
        '''

        return html

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
    #parts.pop(0)
    #print(array_to_html(parts))
    #soup = BeautifulSoup(response.content, "lxml")

    #links = soup.find_all('a')

    #print(soup)
    print(type(parts[0]))

    #with open("C:\\Users\\ataka\\Documents\\fun\\the-beginning\\" + file_name, "w", encoding="utf8") as my_file:
    #    my_file.write(array_to_html(parts))

    mdFile = MdUtils(file_name=chapter_title, title=chapter_title)

    mdFile.new_header(level=1, title=chapter_title)

    for part in parts:
        mdFile.new_paragraph(part) 
    mdFile.create_md_file()
    driver.quit()

