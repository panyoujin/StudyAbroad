// pages/planner/qualification/qualification.js
var common = require('../../../utils/common.js')
Page({

  /**
   * 页面的初始数据
   */
  data: {
    isOK: true,
    planner:null,
    educations: null,
    societys: null,
    resours: null
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this;
    var planner = wx.getStorageSync('planner');
    if (planner == "" || planner == null) {
      that.setData({ isOK: false })
      return;
    }
    that.setData({ planner: planner })
    common.POST({
      url: "/planner/qualifications",
      params: {
        page: 1,
        size: 10,
        plannerId: planner.UserId
      },
      success: function (res, s, m) {
        if (s && res.length != 0) {
          that.setData({
            educations: res.education,
            societys: res.society,
            resours: res.resour,
          })
        } else {
          wx.showToast({
            title: '获取数据失败！' + m,
            image: '/img/error.png',
            duration: 1500
          })
        }
      },
      fail: function () { }
    })
  },

  /**
   * 关注
   */
  btnFollow: function () {
    var that = this;
    wx.showModal({
      title: '关注',
      content: '确定关注该规划师？',
      success: function (res) {
        if (res.confirm) {
          common.POST({
            url: "/planner/follow",
            params: {
              plannerId: that.data.planner.UserId
            },
            success: function (res, s, m) {
              if (s) {
                wx.showToast({
                  title: '成功关注该规划师！',
                  duration: 1500
                })
              } else {
                wx.showToast({
                  title: '关注该规划师失败！',
                  image: '/img/error.png',
                  duration: 1500
                })
              }
            },
            fail: function () { }
          })
        }
      }
    })
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