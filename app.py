from flask import Flask, render_template, url_for, request, redirect
import dotenv
import time

app = Flask(__name__)

result = []

@app.post('/delete')
def delete():
    if request.form.get("penis"):
        result.clear()
    return homepage()


@app.route('/')
def homepage():
    result.clear()
    return render_template('homepage.html', title="General Quiz | Homepage")


@app.route('/contact')
def contact():
    return render_template('contact.html', title="General Quiz | Contact")


@app.route('/about')
def about():
    return render_template('about.html', title="General Quiz | About")


@app.route('/questions', methods=["POST", "GET"])
def questions():
    return render_template('question1.html', title='General Quiz | Question 1')


# QUESTÃO 1
@app.route('/answer1', methods=["POST"])
def answer1():
    question1=[]
    question1d = request.form.get("question1d")
    if request.form.get("question1d"):
        question1.append(request.form.get(question1d))
        result.append(question1d)
    else:
        print('incorreto')
    return render_template('question2.html', title="General Quiz | Question 2")


#QUESTÃO 2
@app.route('/answer2', methods=["POST"])
def answer2():
    question2=[]
    question2c = request.form.get("question2c")
    if  request.form.get("question2c"):
        question2.append(question2c)
        result.append(question2c)
        print(result)
    else:
        if len(question2) > 1:
            pass
    return render_template('question3.html', title="Question 3")


# QUESTÃO 3
@app.route('/answer3', methods=["POST"])
def answer3():
    # QUESTÃO 3
    question3 = []
    question3a = request.form.get("question3a")
    if request.form.get("question3a"):
        question3.append(question3a)
        result.append(question3a)
        print(result)
    else:
        if len(question3) > 1:
            pass
    return render_template('question4.html', title='General Quiz | Question 4')


# QUESTÃO 4
@app.route('/answer4', methods=["POST"])
def answer4():
    question4=[]
    question4b = request.form.get("question4b")
    if  request.form.get("question4b"):
        question4.append(question4b)
        result.append(question4b)
        print(result)
    else:
        if len(question4) > 1:
            pass
    return render_template('question5.html', title='General Quiz | Question 5')


# QUESTÃO 5
@app.route('/answer5', methods=["POST"])
def answer5():
    question5=[]
    question5b = request.form.get("question5b")
    if  request.form.get("question5b"):
        question5.append(question5b)
        result.append(question5b)
        print(result)
    else:
        if len(question5) > 1:
            pass
    return render_template('question6.html', title='General Quiz | Question 6')


# QUESTÃO 6
@app.route('/answer6', methods=["POST"])
def answer6():
    question6=[]
    question6a = request.form.get("question6a")
    if  request.form.get("question6a"):
        question6.append(question6a)
        result.append(question6a)
        print(result)
    else:
        if len(question6) > 1:
            pass
    return render_template('question7.html', title='General Quiz | Question 7')


# QUESTÃO 7
@app.route('/answer7', methods=["POST"])
def answer7():
    question7=[]
    question7a = request.form.get("question7a")
    if  request.form.get("question7a"):
        question7.append(question7a)
        result.append(question7a)
        print(result)
    else:
        if len(question7) > 1:
            pass
    return render_template('question8.html', title='General Quiz | Question 8')


# QUESTÃO 8
@app.route('/answer8', methods=["POST"])
def answer8():
    question8=[]
    question8c = request.form.get("question8c")
    if  request.form.get("question8c"):
        question8.append(question8c)
        result.append(question8c)
        print(result)
    else:
        print('resposta incorreta, indo para questão 5')
        if len(question8) > 1:
            pass
    return render_template('question9.html', title='General Quiz | Question 9')


# QUESTÃO 9
@app.route('/answer9', methods=["POST"])
def answer9():
    question9=[]
    question9d = request.form.get("question9d")
    if  request.form.get("question9d"):
        question9.append(question9d)
        result.append(question9d)
        print(result)
    else:
        if len(question9) > 1:
            pass
    return render_template('question10.html', title='General Quiz | Question 10')


# QUESTÃO 10
@app.route('/answer10', methods=["POST"])
def answer10():
    question10=[]
    question10c = request.form.get("question10c")
    if  request.form.get("question10c"):
        question10.append(question10c)
        result.append(question10c)
        print(result)
    else:
        if len(question10) > 1:
            pass
    if len(result) < 10:
        print('deu ruim amigo')
    elif len(result) == 10:
        print('filé')
    penis = len(result)
    return render_template('results.html', title='Results', penis=penis)

if __name__ == "__main__":
    app.run(debug=True)
