import flask, json
from flask import request
from gevent import pywsgi
from csv import reader


'''
flask： web框架，通过flask提供的装饰器@server.route()将普通函数转换为服务
登录接口，需要传url、username、passwd
'''

# 创建一个服务，把当前这个python文件当做一个服务
server = flask.Flask(__name__)


# server.config['JSON_AS_ASCII'] = False
# @server.route()可以将普通函数转变为服务 登录接口的路径、请求方式
@server.route('/login', methods=['get', 'post'])
def login():
    # 获取通过url请求传参的数据
    username = request.values.get('name')
    # 获取url请求传的密码，明文
    pwd = request.values.get('pwd')
    information = request.values.get('information')
    # 判断用户名、密码都不为空，如果不传用户名、密码则username和pwd为None
    if username and pwd:
        if username == 'wangyunlong' and pwd == 'wangyunlong':
            if information == 'LotteryTicket_information':
                with open('./ssq.txt', 'r', encoding='utf8') as f:
                    return str(list(reader(f)))
        else:
            return '账号密码错误！'
    else:
        return '参数不能为空！'


def main():
    a = pywsgi.WSGIServer(('0.0.0.0', 8888), server)
    a.serve_forever()


if __name__ == '__main__':
    main()
