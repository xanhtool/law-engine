import requests
lawUrl= 'http://thuvienphapluat.vn/van-ban/Quyen-dan-su/Bo-luat-dan-su-2015-296215.aspx'
web_content = requests.get(lawUrl).content
file_name = "law-demo.html"

#Save:
file_html = open(file_name,"wb")
file_html.write(web_content)
file_html.close()

# open and decode:
file = open (file_name, "rb")
decoded_content = file.read().decode('utf-8')
file.close()

# law content
from bs4 import BeautifulSoup
soup=BeautifulSoup(decoded_content,"html.parser")
content = soup.find("div", class_='content1')
text_list = content.find_all("p")
demo_list = text_list[10:20]
#checkpoint: phan biet the can gan ID va khong
for text in demo_list:
    if( text.a):
        print("the a:",text.a)
    else:
        print("the ko phai a:",text)
