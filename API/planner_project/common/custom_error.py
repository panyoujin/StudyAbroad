
class CustomFlaskErr(Exception):

    # 默认的返回码
    status_code = 500
    message = "系统异常"

    # 自己定义了一个 return_code，作为更细颗粒度的错误代码
    def __init__(self, return_code=None, status_code=None,message=None, payload=None):
        Exception.__init__(self)
        self.return_code = return_code
        if status_code is not None:
            self.status_code = status_code
        if status_code is not None:
            self.message = message
        self.payload = payload
