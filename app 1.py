from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('index.html')

@app.route("/math", methods=['POST'])
def math_ops():
    if (request.method=='POST'):
        ops= request.form['operation']
        num1= int(request.form['num1'])
        num2= int(request.form['num2'])
        if ops== 'add':
            r= num1+num2
            res= "The sum of" +str(num1) +"and" +str(num2) +"is" +str(r)
        if ops== 'subtract':
            r= num1-num2
            res= "The subtraction of" +str(num1) +"and" +str(num2) +"is" +str(r)
        if ops== 'multiply':
            r= num1*num2
            res= "The multiplication of" +str(num1) +"and" +str(num2) +"is" +str(r)
        if ops== 'divide':
            r= num1/num2
            res= "The division of" +str(num1) +"and" +str(num2) +"is" +str(r)
        return render_template('results.html', result= res)

@app.route("/postman_action", methods=['POST'])
def math_ops1():
    if (request.method=='POST'):
        ops= request.json['operation']
        num1= int(request.json['num1'])
        num2= int(request.json['num2'])
        if ops== 'add':
            r= num1+num2
            res= "The sum of" +str(num1) +"and" +str(num2) +"is" +str(r)
        if ops== 'subtract':
            r= num1-num2
            res= "The subtraction of" +str(num1) +"and" +str(num2) +"is" +str(r)
        if ops== 'multiply':
            r= num1*num2
            res= "The multiplication of" +str(num1) +"and" +str(num2) +"is" +str(r)
        if ops== 'divide':
            r= num1/num2
            res= "The division of" +str(num1) +"and" +str(num2) +"is" +str(r)
        return jsonify(res)


if __name__=="__main__":
    app.run(host="0.0.0.0")
