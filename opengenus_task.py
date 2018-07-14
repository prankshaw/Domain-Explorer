import urllib.request                                                         #Importing necessary libraries
from urllib.parse import urlparse             
from bs4 import BeautifulSoup

url= input( "Enter the Url : ")                                               #Input the URL
page = urllib.request.urlopen(url)
print("Total Size of web page is: " , len(page.read()), "bytes")              #Outputting size of web page in bytes

links=[]
domains=[]
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page ,'html.parser') 
for link in soup.find_all('a'):
    links.append(link.get('href'))                                            #Adding all links to list named "Links"
    parsed_uri = urlparse(link.get('href'))                                   #Parsing the URL for domain name
    domains.append('{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri))     #Appending parse url to list named "Domains"

print("The links present are:")
print(links)                                                                  # Printing all links
print ("Total number of links in web page are : ", len(links) , "Links")      #Printing the total number of links
count_dict = {i:domains.count(i) for i in domains}
for c in count_dict:
    print("count of domain name ", c ,"=", domains.count(c))                  #Printing Count of links pointing to same domain





















