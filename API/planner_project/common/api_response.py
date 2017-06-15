import json
import time
from datetime import date, datetime

class ApiResponse(object):
    data = ""
    status = 200 #200 sussess,500 logic errors,600 no login errors, -99 unknow error
    message = "成功"


    def __init__(self,data="",status=200,message="成功"):
        self.data=data
        self.status = status
        self.message = message

def response_return(ApiResponse):
    return json.dumps({'status':ApiResponse.status,'message':ApiResponse.message,'data':ApiResponse.data}, ensure_ascii=False,cls=ComplexEncoder)

#需要解决bytes转换的问题
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')