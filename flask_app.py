from flask import Flask, render_template, request, url_for
from wtforms import Form, FloatField, validators
import urllib.request                                                         #Importing necessary libraries
from urllib.parse import urlparse             
from bs4 import BeautifulSoup


app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('form.html')

@app.route('/my_form_post', methods=['GET','POST'])
def my_form_post():
    your_list= [1,2,3,4]
    url = request.form['variable']
    page = urllib.request.urlopen(url)
    s = len(page.read())
    #s=str(s)

    links=[]
    domains=[]
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page ,'html.parser') 

    for link in soup.find_all('a'):
        links.append(link.get('href'))                                            #Adding all links to list named "Links"
        parsed_uri = urlparse(link.get('href'))                                   #Parsing the URL for domain name
        domains.append('{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri))     #Appending parse url to list named "Domains"

    link_size=len(links)

    count_dict = {i:domains.count(i) for i in domains}

    
    return render_template('output.html', s=s,links=links,count_dict=count_dict,link_size=link_size)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=False)


