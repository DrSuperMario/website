from flask import Flask, render_template
#impordi flaski classi objekti flaski raamatust ja html renderdaja

app=Flask(__name__)
#kirjutan välja flaski objekti nime

@app.route('/')
#millisele aadressile soovid runnida nt. /about/ 
#kui soovid veel lehti siis lisa veel route objekte
# kuid tuleb määrata ka funktsioon
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

if __name__ =="__main__":
    app.run(debug=True)
#kontrollin kas nimi on võrdne mainiga ja käivitan skripti
