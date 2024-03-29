# !/usr/bin python3
# encoding: utf-8 -*-
# @author:   wsj QQ：3512937625
# @Time:   2021-07-04
# @Copyright：


import requests

#登录接口
global token
global uid
token = ''
uid = ''
def loginEc(mobile=15117905676,password='Wsj@123456'):
    url = "http://192.168.200.123:8080/user/login"
    # 接口头信息
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    # 表单参数
    body = {
        "mobile": mobile,
        "password": password,
        "channel": "pc"

    }
    # 发起接口调用，拿到响应结果
    resp = requests.post(url=url, data=body, headers=headers)
    # 得到响应状态码
    stats_code = resp.status_code
    print(f'返回响应的状态码为：{stats_code}')
    # # 获取响应body信息的字符串类型数据
    # resp_text = resp.text
    # print(f'body信息的字符串类型数据为：{resp_text}')
    # 获取响应body信息的json类型数据，对应的就是python里的字典嵌套或者列表嵌套
    resp_json = resp.json()

    print(f'取响应body信息的json类型数据:{resp_json}')
    #获取token的值
    global token
    global uid
    token =resp_json['data']['token']
    uid = resp_json['data']['uid']
    # print(token)
    # print(uid)
    return resp


#获取商品接口
def GetProduct(token='9789213cc2994166a2a4d536726cf839',uid=9206):
    url = "http://192.168.200.123:8080/shop/product/selectAuthProductListByUid"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'charset' : 'UTF-8'
    }
    body = {
        "token": token,
        "uid" : uid

    }
    # print(token)
    # print(uid)

    resp = requests.post(url=url, data=body, headers=headers)
    #获取响应状态码
    status_code = resp.status_code
    print(f'返回响应的状态码为：{status_code}')
    # 获取响应body信息的字符串类型数据
    # resp_text = resp.text
    # print(f'body信息的字符串类型数据为：{resp_text}')
    # 获取响应body信息的json类型数据，对应的就是python里的字典嵌套或者列表嵌套
    resp_json = resp.json()
    print(f'取响应body信息的json类型数据:{resp_json}')
    return resp

#获取供货地址
def GetAddress(token='9789213cc2994166a2a4d536726cf839',uid=9206):
    url='http://192.168.200.123:8080/user/address/selectUserAddressByUid'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'charset': 'UTF-8'
    }
    body = {
        "token": token,
        "uid": uid,
        "addressType" :2

    }

    resp = requests.post(url=url, data=body,headers=headers)
    # 获取响应状态码
    status_code = resp.status_code
    print(f'返回响应的状态码为：{status_code}')
    # 获取响应body信息的字符串类型数据
    # resp_text = resp.text
    # print(f'body信息的字符串类型数据为：{resp_text}')
    # 获取响应body信息的json类型数据，对应的就是python里的字典嵌套或者列表嵌套
    resp_json = resp.json()
    print(f'取响应body信息的json类型数据:{resp_json}')
    return resp


#获取商城的商品
def GetDirectSaleProductList():
    url ='http://192.168.200.123:8080/directSale/getDirectSaleProductList'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'charset': 'UTF-8'
    }
    body = {
        "token": token,
        "uid": uid,
        "page": 1,
        "rows": 10,
        "status" : 2
    }
    resp = requests.post(url=url, data=body,headers=headers)
    # 获取响应状态码
    status_code = resp.status_code
    print(f'返回响应的状态码为：{status_code}')
    # 获取响应body信息的字符串类型数据
    resp_text = resp.text
    print(f'body信息的字符串类型数据为：{resp_text}')
    resp_json = resp.json()
    print(f'取响应body信息的json类型数据:{resp_json}')
    return resp
    global  saleProductId
    saleProductId=''
    saleProductId = resp_json[data][id][0]
    print(saleProductId)


#加入购物车
def AddCart(id=182):
    url ='http://192.168.200.123:8080/directSale/insertVehicle'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'charset': 'UTF-8'
    }
    body = {
        "token": token,
        "uid": uid,
        "saleProductId": id,
        "productNum" : 1

    }
    resp = requests.post(url=url, data=body,headers=headers)
    # 获取响应状态码
    status_code = resp.status_code
    print(f'返回响应的状态码为：{status_code}')
    # 获取响应body信息的字符串类型数据
    resp_text = resp.text
    print(f'body信息的字符串类型数据为：{resp_text}')
    return resp
if __name__ == '__main__':
    loginEc()
    GetProduct()
    GetAddress()
    GetDirectSaleProductList()
    AddCart()