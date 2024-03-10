from flask import Flask,render_template,request
import re
app=Flask(__name__)

###################################################
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/results')
def results():
    u_text=request.args.get('user_text')
    u_regex=request.args.get('user_regex')
    text1=re.findall(u_regex,u_text)
    return render_template('home.html' ,text1=text1,u_text=u_text,u_regex=u_regex)

@app.route('/email_validation',methods=['POST'])
def email_valid():
    u_email=request.form.get('user_email')
    pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$'
    is_valid_email = re.match(pattern, u_email) is not None

    return render_template('home.html',u_email=u_email,is_valid_email=is_valid_email)
###################################################


if __name__=='__main__':
    app.run(debug=True)