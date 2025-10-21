from flask import *
import math

app = Flask(__name__)

@app.route('/divisible')
def divisible():
    return render_template('index.html')
        
@app.route('/output', methods=['POST', 'GET'])
def output():
    if request.method == 'POST':
        num = int(request.form['number'])
        if num % 6 == 0 and num % 5 == 0:
            return render_template('result.html',number = num, result = ' Divisible by both 5 and 6')
        elif num % 6 == 0:
            return render_template('result.html',number = num, result =' Divisible by 6')
        elif num % 5 == 0:
            return render_template('result.html',number = num, result = ' Divisible by 5')
        
        else:
            return render_template('result.html',number = num, result = ' not divisible by 5 and 6')


@app.route('/prime')
def prime():
    return render_template('index1.html')

@app.route('/output1', methods=['POST', 'GET'])
def output1():
    if request.method == 'POST':
        num = int(request.form['number'])
        if num <= 1:
            return render_template('prime.html', res = 'Neither prime nor composite')
        elif num == 2:
            return render_template('prime.html', res ='prime')
        elif num % 2 == 0:  
            return render_template('prime.html', res ='composite')
        else:
            is_prime = True
            for i in range(3, int(math.sqrt(num)) + 1, 2):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                res = 'Prime'
            else:
                res = 'Composite'

    return render_template('prime.html', res=res)
        


    
        
if __name__ == '__main__':
    app.run(debug=True)