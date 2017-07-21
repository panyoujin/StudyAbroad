// login.js
//var app = getApp()
var common = require('../../../utils/common.js')
var md5 = require('../../../utils/md5.js')
Page({

  /**
   * 页面的初始数据
   */
  data: {
    tip:""
  },

  /** 表单按钮事件 */
  formSubmit: function (e) {
    var that = this;
    var userAccount = e.detail.value.userAccount;
    var userPwd = e.detail.value.userPwd;

    if (userAccount.length == 0 || userPwd.length == 0){
      that.setData({
        tip: '提示：用户名和密码不能为空！'
      })
    }
    else{
      that.setData({
        tip: ''
      })
      common.POST({
        url: "/user/login",
        params: {
          Account: userAccount,
          Password: md5.hex_md5(userPwd)
        },
        success: function (res, s, m) {
          if (s) {
            wx.setStorageSync('userLoginToken', res.token)
            res.user.HeadImage = common.apiUrl + "/" + res.user.HeadImage ;
            wx.setStorageSync('userLoginInfo', res.user)
            
            var backPage = wx.getStorageSync('backPage');
            if (backPage==""){
              backPage ="/pages/index/index";
            }
            wx.reLaunch({
              url: backPage
            });
          } else {
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
})