from flask import Flask, render_template, request, url_for, redirect
import re

app = Flask(__name__)

#@app.route('/')
#def root():
 #   return redirect(url_for('index'))


@app.route("/", methods=['POST', 'GET'])
def index():
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']
        username_error = ''
        password_error = ''

        if request.form['username'] == '':
            username_error = "Required"
            userok = False
        else:
            userok = True

        if request.form['password'] == '':
            password_error = "Required"
            passok = False
        else: 
            passok = True

        if request.form['verify'] != request.form['password']:
            password_error = "Invalid"
            passok = False
        else:
            passok = True

        if len(request.form['username']) <= 3:
            username_error = "Too Short"
            userok = False
        else: 
            userok = True

        if len(request.form['password']) <= 4:
            password_error = 'Too Short'
            passok = False
        else:
            passok = True


        if len(request.form['verify']) <= 4:
            password_error = 'Too Short'
            passok = False
        else: 
            passok = True
        
        if passok and userok:
            return render_template("welcome.html", username=username)
        
        else:


            return render_template("index.html", username=username, password_error=password_error, username_error=username_error)
    else:
        return render_template("index.html")


    return render_template("index.html")
    #return render_template(templ8te, username=username,
    #password=password, verify=verify, password_error=password_error,
    #empty_password=empty_password, verify_empty=verify_empty,
    #username_error=username_error)   
        
        
    
        

if __name__ == "__main__":
    app.run(debug=True)
