from flask import Flask, render_template, request


app= Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    weight = request.form['Weight']
    height = request.form['Height']
    
    weight = float(weight)
    height = float(height)
    
    height = height/100     # Converting height to meters
    BMI = weight / (height ** 2)
    
    BMI = round(BMI, 2)
    
    if BMI > 0:
        if BMI <= 16:
            return render_template('s_under.html', result= f'BMI score is {BMI}. You are "Severely Underweight"')
        elif BMI <= 18.5:
            return render_template('under.html', result= f'BMI score is {BMI}. You are "Underweight"')
        elif BMI <= 25:
            return render_template('normal.html', result= f'BMI score is {BMI}. You are "Normal"')
        elif BMI <= 30:
            return render_template('over.html', result= f'BMI score is {BMI}. You are "Overweight"')
        elif BMI <= 35:
            return render_template('obese.html', result= f'BMI score is {BMI}. You are "Obese"')
        elif BMI <= 40:
            return render_template('obese1.html', result= f'BMI score is {BMI}. You are "Severely Obese"')
        else:
            return render_template('obese2.html', result= f'BMI score is {BMI}. You are "Extremely Obese"')
        
    else:
        return render_template('correct.html')
    
        


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)