from flask import make_response, jsonify
from app.api import api
from app.models import getHomepageData

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