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
    print(projectpath)
    s = "https://www.dictionary.com/browse/"+projectpath+"?s=ts"
    source = urllib.request.urlopen(s).read()
    soup = bs.BeautifulSoup(source,'lxml')
    q=[]
    for i in soup.find_all("section",class_="css-pnw38j e1hk9ate0"):
        q.append("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        q.append(i.h3.text)
        for j in i.find_all('div',value=True):
            q.append(j.text)
    return render_template('mean.html',data=q,name=projectpath)

if __name__ == '__main__':
    app.run(debug=True)
