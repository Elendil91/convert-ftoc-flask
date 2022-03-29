from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
def ftoc(ftemp):
   return (ftemp-32.0)*(5.0/9.0)

@app.route('/ftoc/<ftempString>')
def convertFtoC(ftempString):
    ftemp = 0.0
    try:
        ftemp = float(ftempString)
        ctemp = ftoc(ftemp)
        return "Farenheit: " + ftempString + " Celsius " + str(ctemp) 
    except ValueError:
        return "Sorry.  Could not convert " + ftempString + " to a number"

if __name__ == "__main__":
    app.run(port=5000)

    