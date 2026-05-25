from flask import Flask, render_template, request

app =Flask(__name__)

# GET Method

@app.route('/squarenum',methods=['GET'])
def squarenumber():
    num = request.args.get('num')

    if num is None:
        return render_template('squarenum.html')
    elif num.strip() == ' ':
        return "<h1>Invalid Number. Enter correct number</h1>"
    try:
        square = int(num)**2
        return render_template('answer.html',squareofnum = square , num=num)
    except ValueError:
        return "<h1>Invalid Number</h1>"
    
if __name__ == '__main__':
    app.run(debug=True)