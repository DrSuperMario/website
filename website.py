from flask import Flask, render_template
#import requests as req
#impordi flaski classi objekti flaski raamatust ja html renderdaja

app=Flask(__name__)
#kirjutan välja flaski objekti nime

@app.route('/')
def home():
    return render_template("home.html")
#funktsioon mis väljastab info lehele

@app.route('/about/')
def about():
    return render_template("about.html")
#teine leht

@app.route('/portfolio/')
def portfolio():
    return render_template("portfolio.html")

@app.route('/social/')
def social():
    return render_template("social.html")

'''
@app.route('/fcssignals', methods = ['GET'])
def fcssignals():
    data = req.get("http://127.0.0.1:5000/markets")
    return data.content
'''

if __name__ =="__main__":
    app.run(debug=True, host='0.0.0.0', port=5050)
#kontrollin kas nimi on võrdne mainiga ja käivitan skripti
			
