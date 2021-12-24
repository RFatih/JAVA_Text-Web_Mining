import requests
from bs4 import BeautifulSoup
import urllib
from urllib.parse import urlparse, urljoin
import pprint
import urllib.request
import networkx as nx
import matplotlib.pyplot as plt




user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ Safari/537.36'
url = 'https://www.deu.edu.tr/'

G = nx.Graph()
links= set()
visit= set()
visited=set()
visit.add(url)
pp = pprint.PrettyPrinter(width=41, compact=True)
domain='deu.edu'

total_urls_visited = 0

session = requests.Session()
session.max_redirects = 3
session.get(url)
def req(url,agent):
    return session.get(url,headers={'User-Agent': agent})
def crawler(url,maxpages):
    try:
        
        global total_urls_visited
        
        domain_name=urlparse(str(url)).netloc
        print("a")
        r = req(url,user_agent)
        print("b")
        soup = BeautifulSoup(r.content, 'html.parser',from_encoding="iso-8859-1")
        if(G.has_node(url) != True):
            G.add_node(url)
        for link in soup.find_all(['a', 'link'], href=True):
            if(domain not in str(link) or '.jpg' in str(link) or 'css' in str(link) or 'json' in str(link) or '.jpeg' in str(link) or '.png' in str(link)
               or 'facebook.' in str(link) or 'google.' in str(link) or 'twitter.' in str(link)):
                continue
            if(str(link.get('href')) not in links):
                if('http' not in link.get('href')):
                    continue
                if(link['href'].find(domain) != -1):
                    if(G.has_node(str(link['href']))!= True):
                        G.add_node(str(link['href']))
                    G.add_edge(url,str(link['href']))
                    links.add(str(link['href']))
                    total_urls_visited += 1
                    if(total_urls_visited>=maxpages):
                        return
                else:
                    continue
                
            else:
                 G.add_edge(url,str(link['href']))
    except Exception as e: print(e)

      
while(total_urls_visited <12000):
    for link in visit:
        print("*",total_urls_visited,"*", end ="")
        if(total_urls_visited <12000):
            crawler(link,1000000)
        else:
            break
    visited.update(visit)
    visit.update(links)
    visit.difference_update(visited)




degree_C=nx.degree_centrality(G)
between_C=nx.betweenness_centrality(G, k=None, normalized=True, weight=None, endpoints=False, seed=None)
close_C=nx.closeness_centrality(G, u=None, distance=None, wf_improved=True)

degree_CS=sorted(degree_C.items(), key=lambda x: x[1],reverse=True)
between_CS=sorted(between_C.items(), key=lambda x: x[1],reverse=True)
close_CS=sorted(close_C.items(), key=lambda x: x[1],reverse=True)
degree_txt=""
between_txt=""
close_txt=""
for word in degree_CS:
    value=str(word[1])
    if(value[0]=='\''):
        n=float(value[1:])
    n=float(value)
    fvalue=("%.40f" % n).rstrip('0').rstrip('.')
    degree_txt+=word[0]+","+str(fvalue)+"\n"
for word in between_CS:
    value=str(word[1])
    if(value[0]=='\''):
        n=float(value[1:])
    n=float(value)
    fvalue=("%.40f" % n).rstrip('0').rstrip('.')
    between_txt+=word[0]+","+str(fvalue)+"\n"
for word in close_CS:
    value=str(word[1])
    if(value[0]=='\''):
        n=float(value[1:])
    n=float(value)
    fvalue=("%.40f" % n).rstrip('0').rstrip('.')
    close_txt+=word[0]+","+str(fvalue)+"\n"

f = open("degree_C.csv", "w")
f.write(str(degree_txt))
f.close()

f = open("between_C.csv", "w")
f.write(str(between_txt))
f.close()

f = open("close_C.csv", "w")
f.write(str(close_txt))
f.close()
