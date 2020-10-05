from flask import make_response, jsonify
from app.api import api
from app.models import User
from flask import Flask, abort, request, jsonify, g, url_for
from app.models import db,allowed_file


@app.route('/api/users', methods = ['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    #核对前端传送的数据
    if username is None or password is None:
        abort(400) # missing arguments
    if User.query.filter_by(username = username).first() is not None:
        abort(400) # existing user
    user = User(username = username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({ 'username': user.username }), 201, {'Location': url_for('get_user', id = user.id, _external = True)}




@app.route('/api/users/reg',methods=['POST'])
def user_reg():
    
    username=request.json.get('username')
    password=request.json.get('password')
    if username is None or password is None:
        abort(400)
    if User.query.filter_by(username=username).first() is not None:
        abort(400)

    f=request.files['file']
    if not(f and allowed_file(f.filename)):
        return jsonify({"error":1001,"msg":"check the photo"})
    
    #创建user对象，一边写入数据库
    user=User(username=username)
    user.password(password)
    db.session.add(user)
    db.session.commit()
    



@api.route('/v1.0/homePage/', methods=['GET', 'POST'])
def homepage():
    """
     上面 /v1.0/homePage/ 定义的url最后带上"/"：
     1、如果接收到的请求url没有带"/"，则会自动补上，同时响应视图函数
     2、如果/v1.0/homePage/这条路由的结尾没有带"/"，则接收到的请求里也不能以"/"结尾，否则无法响应
    """
    response = jsonify(code=200,
                       msg="success",
                       data=getHomepageData())

    return response
    # 也可以使用 make_response 生成指定状态码的响应
    # return make_response(response, 200)