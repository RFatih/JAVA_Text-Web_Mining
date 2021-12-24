import requests
from bs4 import BeautifulSoup
import os

file1 = open('site_urls.txt', 'r')
Lines = file1.readlines()
count = 0
word=[]
file1.close()
num_os="/home/fatih/Desktop/Metin-Dosyalar/Numeretic/"
name_os="/home/fatih/Desktop/Metin-Dosyalar/ByName/"
main_os='/home/fatih/Desktop/Metin-Dosyalar/'
for i in range(len(Lines)):
    try:
        os.chdir(main_os)
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ Safari/537.36'}
        flag=False
        doc = Lines[i]
        if("eng.deu" in doc or "feed/" in doc or ".pdf" in doc or "gensek.deu" in doc or ".doc" in doc or ".odt" in doc):
            continue
        print(doc)
        res = requests.get(doc,headers=headers)


        soup = BeautifulSoup(res.content, "html.parser")
        for s in soup.select('script'):
            s.extract()

        tag = soup.body
                
        for string in tag.strings:
                if(string != ' ' and string != '\n' and string != '\t'
                   and string != '\r' and string!='\xa0'):
                    string=string.replace("\t","").replace("\n","").replace("\r","").replace("\xa0","")
                    if(string=="Sayfa Bulunamadı! Hatalı link ya da Aradığınız sayfa silinmiş." or string=="Not Found"
                       or string == "You are not authorized to perform this action." or string=="Internal Server Error"
                       or string == "JavaScript is not available." or string == "You don't have permission to access this resource."
                       or string == "HATA: Geçerli bir besleme şablonu değil." or string == "Please enter an answer in digits:"
                       or string == "Bu sayfa ile ilgili bir problem yaşıyorsanız lütfen "):
                        flag=True
                    word.append(string)
        if(flag or word==[]):
            word=[]
            continue
        os.chdir(num_os)
        f = open(str(count), "a")
        f.write(str(word))
        f.close()

        os.chdir(name_os)
        f = open(str(doc[:-1].replace('/','')), "a")
        f.write(str(word))
        f.close()
        count+=1
        print("iteration=",i)
        word=[]
    except Exception as e:
        print(e)
        
    
    

