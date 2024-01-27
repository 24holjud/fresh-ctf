from flask import request, Response, render_template, Blueprint,jsonify

CTFapp = Blueprint('ctfapp', __name__,
                   static_folder='static',
                   static_url_path='/',
                   template_folder='templates')

@CTFapp.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@CTFapp.route('/form', methods=['GET','POST'])
def add_form():
    
    return render_template('add_form.html')

@CTFapp.route('/add', methods=['GET','POST'])
def add():
    num1 = request.args.get('num1', type=float)
    num2 = request.args.get('num2', type=float)

    result = int(num1 + num2)

    return jsonify('try changing the variables in the url',
                    result, 
                   'next route at /function_form')

        
@CTFapp.route('/function_form', methods=['GET', 'POST'])
def function_form():
    return render_template('function.html')

def fib(n: int):
    if n <= 0:
        return "Invalid input. Please provide a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b

@CTFapp.route('/function', methods=['GET', 'POST'])
def function():
    num = request.args.get('num', type=int)
    f_of_20 = request.args.get('f_of_20', type=int)

    result = fib(num)

    if f_of_20 == 4181:
        return jsonify('next route at /gloating_form')

    if num <= 10:
        return jsonify('choose number less than or equal to 10',
                        result, 
                        'find f(20) for the next route')

    else:
        return jsonify('not in range, pick number less than or equal to 10')
 
@CTFapp.route('/gloating_form', methods=['GET', 'POST'])
def trivia():
    return render_template('jude_form.html')

@CTFapp.route('/gloating', methods=['GET', 'POST'])
def gloating():
    if request.method == 'GET':
        user_answer = request.args.get('response', type=str)
        correct_answer = 'Jude'

        if user_answer.lower() == correct_answer.lower():
            return jsonify('Correct! Next route at /uhhhh')
        else:
            return jsonify('Incorrect. Try again.')