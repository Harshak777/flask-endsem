from flask import *
import urllib.request
import random 
import bs4 as bs

app = Flask(__name__, static_url_path='/static')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/', methods=['POST','GET'])
def mai():
    s = "https://www.goodreads.com"
    try:
        source = urllib.request.urlopen(s).read()
    except urllib.error.HTTPError as e:
        reason=format(e.code)
        res = make_response("<h1>" + reason + "</h1>")
        return res
    except urllib.error.URLError as e:
        reason =format(e.reason)
        res = make_response("<h1>" + reason + "</h1>")
        return res
    #source = urllib.request.urlopen(s).read()
    a = []
    body = bs.BeautifulSoup(source,'html.parser').body
    for i in body.find_all('div',class_='quoteText'):
        a.append(i.text)
    a=a[:11]
    sq = random.randrange(0, 10)
    name = request.cookies.get('books')
    return render_template('index.html',data = a[sq].strip(),name=name)

@app.route('/search', methods=['POST','GET'])
def search():
    project = request.form['projectFilepath']
    projectpath = project.replace(" ","+")
    s = "https://www.goodreads.com/search?utf8=%E2%9C%93&query="+projectpath
    try:
        source = urllib.request.urlopen(s).read()
    except urllib.error.HTTPError as e:
        reason=format(e.code)
        res = make_response("<h1>" + reason + "</h1>")
        return res
    except urllib.error.URLError as e:
        reason =format(e.reason)
        res = make_response("<h1>" + reason + "</h1>")
        return res
    #source = urllib.request.urlopen(s).read()
    soup = bs.BeautifulSoup(source,'lxml')
    ar = soup.table
    q=[]
    w=[]
    e=[]
    r=[]
    for z,i,j,m in zip(ar.find_all('span',role="heading"),ar.find_all('span',itemprop="author"),ar.find_all('span',class_='minirating'),ar.find_all('a',class_="bookTitle",href=True)):
        q.append(z.text.replace(" ",""))
        w.append(i.text.strip().replace(" ",""))
        e.append(j.text.strip())
        r.append(m['href'][11:])
    resp = make_response(render_template('search.html',data=zip(q,w,e,r)))
    resp.set_cookie('books', projectpath)
    return resp

@app.route('/bookreview/<url>', methods=['POST','GET'])
def review(url):
    s = "https://www.goodreads.com/book/show/"+url
    session['book'] = s
    try:
        source = urllib.request.urlopen(s).read()
    except urllib.error.HTTPError as e:
        reason=format(e.code)
        res = make_response("<h1>" + reason + "</h1>")
        return res
    except urllib.error.URLError as e:
        reason =format(e.reason)
        res = make_response("<h1>" + reason + "</h1>")
        return res
    #source = urllib.request.urlopen(s).read()
    body = bs.BeautifulSoup(source,'html.parser').body
    q = body.find('div',id="description").text
    w = body.find('h1',id="bookTitle").text.strip()
    src = body.find('img',id="coverImage")
    return render_template('review.html',q=q,w=w,src=src['src'])

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
