from flask import Flask,render_template
app=Flask(__name__)

@app.route('/hello/<name>')
def hello(name=None):
	user={'name':name}
	return render_template('hello.html',user=user)

@app.route('/')
def Default():
	return "Hello pk!"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
	user={'name':name}
	return render_template('conditional.html',name=name)


if __name__=='__main__':
	app.run(debug=True)