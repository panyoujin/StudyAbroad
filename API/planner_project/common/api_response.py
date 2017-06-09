import json

class ApiResponse(object):
    data = ""
    status = 1 #0:失败 1:成功
    message = "成功"

def response_return(ApiResponse):
    return json.dumps({'status':ApiResponse.status,'message':ApiResponse.message,'data':ApiResponse.data}, ensure_ascii=False)