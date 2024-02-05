from flask import Flask, render_template, request, redirect, url_for
from linkedlistmodule import merge_sorted_lists, print_linked_list, create_linked_list

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('index'))

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/touppercase', methods=['GET', 'POST'])
def touppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/areaOfcircle', methods=['GET', 'POST'])
def area_of_circle():
    area = None
    if request.method == 'POST':
        radius = float(request.form.get('radius', 0))
        area = 3.14159265359 * (radius ** 2)
    return render_template('areaOfcircle.html', area=area)
    

@app.route('/areaOftriangle', methods=['GET', 'POST'])
def area_of_triangle():
    area = None
    if request.method == 'POST':
        base = float(request.form.get('base', 0))
        height = float(request.form.get('height', 0))
        area = 0.5 * base * height
    return render_template('areaOftriangle.html', area=area)

@app.route('/mergedList', methods=['GET', 'POST'])
def merge():
    result_values = None
    error = None
    list1 = None
    list2 = None

    if request.method == 'POST':
        try:
            size1 = int(request.form.get('size1', 0))
            values1 = [val.strip() for val in request.form.get('values1', '').split(',')]
            if size1 != len(values1):
                raise ValueError("Size should be equal to the number of values for Linked List 1.")
            list1 = create_linked_list(size1, values1)

            size2 = int(request.form.get('size2', 0))
            values2 = [val.strip() for val in request.form.get('values2', '').split(',')]
            if size2 != len(values2):
                raise ValueError("Size should be equal to the number of values for Linked List 2.")
            list2 = create_linked_list(size2, values2)

            result_values = merge_sorted_lists(list1, list2)

        except ValueError as e:
            error = str(e)

    return render_template('mergedList.html', result_values=result_values, error=error, print_linked_list=print_linked_list, list1=list1, list2=list2)

if __name__ == "__main__":
    app.run(debug=True)