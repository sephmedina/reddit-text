from flask import Flask, request, render_template

#routing
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', request=request.method)

#running server/application
if __name__ == '__main__':
    app.run(debug=True)
