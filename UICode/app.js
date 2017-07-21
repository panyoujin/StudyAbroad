//app.js
App({
  globalData: {
    userInfo: null,
    wxSessionKey :"",
    wxOpenId:""
  },
  onLaunch: function () {
    //调用API从本地缓存中获取数据
    var logs = wx.getStorageSync('logs') || []
    logs.unshift(Date.now())
    wx.setStorageSync('logs', logs)
    
    var that = this
    if (this.globalData.userInfo) {
      typeof cb == "function" && cb(this.globalData.userInfo)
    } else {
      //调用登录接口
      wx.login({
        success: function (rr) {
          /*if (rr.code) {
            //发起网络请求
            wx.request({
              url: 'https://api.weixin.qq.com/sns/jscode2session?appid=wxdee612b8de237c27&secret=db3131348210e0152992b74e2f5d73ee&js_code=' + rr.code+'&grant_type=authorization_code',
              data: {
                code: rr.code
              },
              success :function(rrr){
                that.globalData.wxSessionkey = rrr.data.sessionkey_key
                that.globalData.wxOpenId = rrr.data.openid
              }
            })
          } else {
            console.log('获取用户登录态失败！' + res.errMsg)
          }*/

          wx.getUserInfo({
            success: function (res) {
              that.globalData.userInfo = res.userInfo
              typeof cb == "function" && cb(that.globalData.userInfo)


            }
          })
        }
      })
    }
  },
  getUserInfo:function(cb){
    
  }
})