from flask import *
import urllib.request
import bs4 as bs

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def mai():
    return render_template('index.html')

@app.route('/thesaurus', methods=['POST','GET'])
def thesaurus():
    projectpath = request.form['projectFilepath']
    s = "https://www.thesaurus.com/browse/"+projectpath+"?s=t"
    source = urllib.request.urlopen(s).read()
    soup = bs.BeautifulSoup(source,'lxml')
    q = soup.find('section',class_="MainContentContainer css-1y12pw e1h3b0ep0")
    a = (q.h1.text)
    h = []
    for i in q.find_all('h2'):
        h.append(i.text)
    #print(h[0])
    div = []
    for i in q.find_all('div', class_='css-kv266z e1qo4u830'):
        div.append(i)
    q=[]
    for i in div[0].find_all('li'):
        q.append(i.text)
    #print(h[1])
    w = []
    for i in div[1].find_all('li'):
        w.append(i.text)
    return render_template('thesaurus.html',z=a,x=h,c=q,v=w)

if __name__ == '__main__':
    app.run(debug=True)
