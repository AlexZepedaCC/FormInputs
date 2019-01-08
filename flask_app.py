from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    # found in ../templates/
    return render_template("main_page.html")

@app.route('/process_inputs', methods=['POST'])
def process_inputs():
    customer_message = ""
    name = request.form.get('input_name', '')
    dropdown = request.form.get('input_dropdown', '')
    if dropdown == "engine":
        customer_message = "Have 3 in stock"



    select = request.form.get('input_select', '')
    freeform = request.form.get('input_freeform', '')
    return render_template("main_page.html", output=customer_message)
