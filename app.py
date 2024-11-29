from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='templates')
post_count = 0  

@app.route('/', methods=['GET', 'POST'])
def index():
    global post_count
    if request.method == 'POST':
        if 'reset' in request.form:
            post_count = 0
        else:
            post_count += 1
    return render_template('index.html', post_count=post_count)

@app.route('/post', methods=['POST']) 
def handle_post(): 
    global post_count 
    post_count += 1 
    return "POST request received", 200

@app.route('/get', methods=['GET']) 
def handle_get():
    return jsonify({"post_count": post_count})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
