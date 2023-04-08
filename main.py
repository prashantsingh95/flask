from flask import Flask,render_template,request

app =Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/service')
def service():
    return render_template('ourwork.html')
@app.route('/client')
def client():
    return render_template('clients.html')

@app.route('/Api_Devlopmennt')
def Api_Devlopmennt():
    return render_template('api_dev.html')
@app.route('/Mobile')
def Mobile():
    return render_template('Mob_App.html')
@app.route('/server')
def server():
    return render_template('Server_M.html')
@app.route('/Website')
def Website():
    return render_template('Website_devlop.html')
@app.route('/Testing')
def Testing():
    return render_template('Testing.html')
@app.route('/IoT')
def IoT():
    return render_template('IoT.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
