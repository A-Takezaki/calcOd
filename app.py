import getPhotoDiode
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    numbers = [1, 2, 3]
    return render_template('index.html', numbers=numbers)

@app.route('/result', methods=['POST'])
def result():
    # selected_number = int(request.form['number'])
    result = getPhotoDiode.outputPhotodiodeSignal()
    print(result)
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port="5000",debug=True)