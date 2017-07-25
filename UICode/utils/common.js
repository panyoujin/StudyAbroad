
var apiUrl = "http://39.108.125.58";
var programName = "规划师";
var pageSize = 1;

//http请求封装
var requestHandler = {
  url :"",
  filePath:"",    //上传才使用的参数
  params: {},
  success: function (res, status, errMsg) {
    // success 
  },
  fail: function () {
    // fail
  },
}
//GET请求  
function GET(requestHandler) {
  request('GET', requestHandler)
}
//POST请求  
function POST(requestHandler) {
  request('POST', requestHandler)
}
//PostUpload请求
function PostUpload(requestHandler) {
  uploadFile(requestHandler)
}

//请求
function request(method, requestHandler) {
  //注意：可以对params加密等处理  
  var params = requestHandler.params;
  wx.request({
    url: apiUrl + requestHandler.url,
    data: params,
    method: method,
    header: {
      'content-type': 'application/x-www-form-urlencoded',//'application/json',
      'Cookie': "token="+getToken()
    },
    dataType : "json",
    success: function (res) {
      var msg = getHttpRequestStatus(res.statusCode);
      var status = true;
      if (msg != '') {  //请求错误
        status = false;
        requestHandler.success(res, status, msg);
      } else if (!getUserHttpRequestInfo(res.data.status)){ //业务错误
        status = false;
        requestHandler.success(res, status, res.data.message);
      }else{  //成功
        if (res.data.data == "" || typeof (res.data.data) == "object")
          requestHandler.success(res.data.data, status, '');
        else
          requestHandler.success(JSON.parse(res.data.data), status, '');
      }
    },
    fail: function () {
      wx.showModal({
        title: '提示',
        content: '页面发生未知的错误，请刷新重试',
        success: function (res) {
          // if (res.confirm) {
          //   console.log('确定')
          // } else if (res.cancel) {
          //   console.log('取消')
          // }
        }
      });
      requestHandler.fail()
    },
    complete: function () {
      // complete  
    }
  })
}
module.exports = {
  GET: GET,
  POST: POST
}

//上传
function uploadFile(requestHandler) {
  wx.uploadFile({
    url: apiUrl + requestHandler.url,
    filePath: requestHandler.filePath,
    name: 'file',
    header: { 
      "Content-Type": "multipart/form-data" ,
      'Cookie': getToken()
    },
    formData: requestHandler.params,
    success: function (res) {
      var msg = getHttpRequestStatus(res.statusCode);
      var status = true;
      if (msg != '') {  //请求错误
        status = false;
        requestHandler.success(res, status, msg);
      } else if (!getUserHttpRequestInfo(JSON.parse(res.data).status)) { //业务错误
        status = false;
        requestHandler.success(res, status, res.data.message);
      } else {  //成功
        requestHandler.success(JSON.parse(res.data).data, status, '');
      }
    },
    fail: function () {
      wx.showModal({
        title: '提示',
        content: '页面发生未知的错误，请刷新重试',
        success: function (res) {
          // if (res.confirm) {
          //   console.log('确定')
          // } else if (res.cancel) {
          //   console.log('取消')
          // }
        }
      });
      requestHandler.fail()
    },
    complete: function () {
      // complete  
    }
  })
}

//根据http返回状态返回信息
function getHttpRequestStatus(status) {
  var msg = "未知错误0x0000"
  switch (status) {
    case 200:
      msg = "";
      break;
    case 400:
      msg = "请求页面无效";
      break;
    case 401:
      msg = "请求页面未授权";
      break;
    case 404:
      msg = "请求页面不存在";
      break;
    case 404:
      msg = "上传的文件超过3M限制";
      break;
    case 505:
      msg = "请求服务器内部错误";
      break;
    case 504:
      msg = "请求网关超时";
      break;
  }
  return msg;
}

//根据用户设定返回状态返回信息
function getUserHttpRequestInfo(status) {
  var isok = false;
  switch (status) {
    case 200:
      isok = true;
      break;
    case 600:
      isok = false;
      wx.navigateTo({
        url: "/pages/account/login/login"
      });
      break;
  }
  return isok;
}

/**
 * 登录token
 */
function getToken(){
  var token = "";
  try {
    token = wx.getStorageSync('userLoginToken')
  } catch (e) {
  }
  //return token;
  return token;
}
/**
 * 去除空格
 */
function Trim(str) {
  return str.replace(/(^\s*)|(\s*$)/g, "");
}

module.exports = {
  apiUrl: apiUrl,
  programName: programName,
  pageSize: pageSize,
  //getHttpRequestStatus: getHttpRequestStatus,
  GET: GET,
  POST: POST,
  PostUpload: PostUpload,
  Trim: Trim,
}