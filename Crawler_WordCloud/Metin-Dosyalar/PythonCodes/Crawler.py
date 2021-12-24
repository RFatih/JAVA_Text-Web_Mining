import requests
from bs4 import BeautifulSoup
import urllib
from urllib.parse import urlparse, urljoin
import pprint
import urllib.request


user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ Safari/537.36'
url = 'https://www.deu.edu.tr/'
domain_name=urlparse(url).netloc
links= set()
visit= set()
visited=set()
visit.add(url)
pp = pprint.PrettyPrinter(width=41, compact=True)
domain='deu.edu'
print("\n\n"+domain_name+"\n\n")

total_urls_visited = 0
def crawler(url,maxpages):
    try:
        
        global total_urls_visited
        
        domain_name=urlparse(str(url)).netloc
        r = requests.get(url, headers={'User-Agent': user_agent})
        soup = BeautifulSoup(r.content, 'html.parser',from_encoding="iso-8859-1")
        for link in soup.find_all(['a', 'link'], href=True):
            if(domain not in str(link) or '.jpg' in str(link) or 'css' in str(link) or 'json' in str(link) or '.jpeg' in str(link) or '.png' in str(link)
               or 'facebook.' in str(link) or 'google.' in str(link) or 'twitter.' in str(link)):
                continue
            if(str(link.get('href')) not in links):
                #pp.pprint(links)
                if('http' not in link.get('href')):
                    continue
                if(link['href'].find(domain) != -1):
                    links.add(str(link['href']))
                    total_urls_visited += 1
                    if(total_urls_visited>=maxpages):
                        return
                else:
                    continue
                
    except:
        print('hata')
        print(total_urls_visited)
      
while(total_urls_visited <1000000):
    for link in visit:
        print("*", end ="")        
        crawler(link,1000000)
    print(total_urls_visited)  
    visited.update(visit)
    visit.update(links)
    visit.difference_update(visited)
    f = open("site_urls.txt", "w")
    for link in links:    
        f.write(str(link))
        f.write("\n")
    f.close()
pp.pprint(links)
