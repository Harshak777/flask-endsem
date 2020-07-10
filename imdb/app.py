from flask import *
import urllib.request
import bs4 as bs

app = Flask(__name__, static_url_path='/static')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/', methods=['POST','GET'])
def mai():
    i = 1
    if i == 1:
        return render_template('index.html')

@app.route('/meaning', methods=['POST','GET'])
def mean():
    projectpath = request.form['projectFilepath']
    s = "https://www.imdb.com/find?q="+projectpath+"&s=tt&ref_=fn_al_tt_mr"
    source = urllib.request.urlopen(s).read()
    soup = bs.BeautifulSoup(source,'lxml')
    ar = soup.table
    l = []
    for i in ar.find_all('tr'):
        print(i.find_all('td')[1].text)
        l.append(i.find_all('td')[1].text)
    return render_template('mean.html',data=l)

if __name__ == '__main__':
    app.run(debug=True)
