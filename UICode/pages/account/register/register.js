// register.js
//var app = getApp()
var common = require('../../../utils/common.js')
var md5 = require('../../../utils/md5.js')

Page({

  /**
   * 页面的初始数据
   */
  data: {
    userAccount:"",
    phoneMsg:"发送验证码",
    second: 60,
    bindSendVerificationCode:"sendVerificationCode"
  },

  /***发送验证码 */
  userAccountInput : function(e){
    //console.log(e);
    var that = this;
    this.setData({
      userAccount: e.detail.value
    });
  },
  sendVerificationCode: function(){
    var that = this;
    if (!validatemobile(that.data.userAccount)){
      return;
    }
    that.setData({ tip: '', bindSendVerificationCode: ""})
    common.POST({
      url: "/basic/get_vcode",
      params: {
        Phone: that.data.userAccount,
        CodeType: 1
      },
      success: function (res, s, m) {
        if (s) {
          countdown(that);
        } else {
          that.setData({
            tip: m,
            second: 60,
            phoneMsg: "发送验证码",
            bindSendVerificationCode: "sendVerificationCode"
          })
        }
      },
      fail: function () { }
    })
    // that.setData({
    //   tip: "手机号码：" + that.data.userAccount + "  验证码：" + Math.round(Math.random() * 1000000)
    // })
  },

  /** 表单按钮事件 */
  formSubmit: function (e) {
    var that = this;
    var userAccount = e.detail.value.userAccount;
    var userCheckCode = e.detail.value.userCheckCode;
    var userPwd = e.detail.value.userPwd;
    var userConfirmPwd = e.detail.value.userConfirmPwd;

    if (userAccount.length == 0 || userPwd.length == 0 || userCheckCode.length == 0 || userConfirmPwd.length == 0) {
      that.setData({
        tip: '提示：手机号、验证码、密码、不能为空！'
      })
    }
    else if (userPwd != userConfirmPwd) {
      that.setData({
        tip: '提示：密码不一致！'
      })
    }
    else {
      that.setData({
        tip: ''
      })
      common.POST({
        url: "/user/register",
        params: {
          Account: userAccount,
          Password: md5.hex_md5(userPwd),
          VCode: userCheckCode
        },
        success: function (res, s, m) {
          if (s) {
            that.setData({
              tip: "注册成功"
            })
          }else{
            that.setData({
              tip: m
            })
          }
        },
        fail: function () { }
      })
    }
  },
  formReset: function (e) {

  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
  
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
  
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
  
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {
  
  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {
  
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
  
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
  
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
  
  }
});

function validatemobile(mobile) {
  if (mobile.length == 0) {
    wx.showToast({
      title: '请输入手机号！',
      image: '/img/error.png',
      duration: 1500
    })
    return false;
  }
  if (mobile.length != 11) {
    wx.showToast({
      title: '手机号长度有误！',
      image: '/img/error.png',
      duration: 1500
    })
    return false;
  }
  var myreg = /^[1-9]+$/;
  if (!myreg.test(mobile)) {
    wx.showToast({
      title: '手机号有误！',
      image: '/img/error.png',
      duration: 1500
    })
    return false;
  }
  return true;
}

function countdown(that) {
   var second = that.data.second
   if (second == 0) {
      that.setData({
        phoneMsg: "发送验证码",
        bindSendVerificationCode:"sendVerificationCode",
        second: 60
      });
      return;
   }
   var time = setTimeout(function () {
      that.setData({
         second: second - 1,
         phoneMsg: "重新发送" + second + "s" 
      });
      countdown(that);
   }
     , 1000)
}