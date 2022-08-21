from flask import Flask, render_template
app = Flask(__name__)    

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<int:num>')
def size(num):
    return render_template('four.html', num=num)
# this should render a checkerboard with num being the number of row added.
# for loop that shit create custom rows using modulo for 2 first or 1 first?

@app.route('/<int:num>/<int:cup>')
def custom(num,cup):
    return render_template('xandy.html', num=num, cup=cup)

@app.route('/<int:num>/<int:cup>/<string:color1>/<string:color2>')
def coluhzzz(num,cup,color1,color2):
    return render_template('colorzz.html', num=num, cup=cup,color1=color1,color2=color2)

if __name__=="__main__":   
    app.run(debug=True)      



