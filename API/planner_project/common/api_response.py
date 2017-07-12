import json
import time,decimal
from datetime import date, datetime

class ApiResponse(object):
    listCount=0
    data = ""
    status = 200 #200 sussess,500 logic errors,600 no login errors, -99 unknow error
    message = "成功"


    def __init__(self,data="",status=200,message="成功",listCount=0):
        self.data=data
        self.listCount = listCount
        self.status = status
        self.message = message

def response_return(ApiResponse):
    return json.dumps({'status':ApiResponse.status,'message':ApiResponse.message,'data':ApiResponse.data,'listCount':ApiResponse.listCount}, ensure_ascii=False,cls=ComplexEncoder)

#需要解决bytes转换的问题
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, decimal.Decimal):
            return "%.2f" % obj
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        # return json.JSONEncoder.default(self, obj)