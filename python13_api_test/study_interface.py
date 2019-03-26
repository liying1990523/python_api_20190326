from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route('/login')
def login():
    req_args = request.args
    mobile = req_args.get('mobilephone','')
    pwd = req_args.get('pwd','')
    if not mobile:
        return jsonify({"status":1,"code":"20103","data":None,"msg":"手机号码不能为空"})
    elif mobile == '18566743962' and pwd == '123456':
        return jsonify({"status":1,"code":"10001","data":None,"msg":"登录成功"})
    else:
        return jsonify({"status":1,"code":"20111","data":None,"msg":"用户名或密码错误"})

if __name__ == "__main__":
    app.run(debug=True)