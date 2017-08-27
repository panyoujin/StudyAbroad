// pages/planner/qualification/qualification.js
var common = require('../../../utils/common.js')
Page({

  /**
   * 页面的初始数据
   */
  data: {
    isfllow: 0,
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
    var isfllow = wx.getStorageSync('isfllow');
    that.setData({ 
      planner: planner,
      isfllow: isfllow
    })
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
    var title = '关注';
    var content = '确定关注该规划师？';
    var msg = "关注该规划师";
    var url = '/planner/follow';
    var isfllow = 1;
    if (that.data.isfllow == 1) {
      title = '取消关注';
      content = '确定取消关注该规划师？';
      url = '/planner/unfollow';
      msg = "取消关注该规划师";
      isfllow = 0;
    }
    wx.showModal({
      title: title,
      content: content,
      success: function (res) {
        if (res.confirm) {
          common.POST({
            url: url,
            params: {
              plannerId: that.data.planner.UserId
            },
            success: function (res, s, m) {
              if (s) {
                common.Alert("成功" + msg);
                that.setData({
                  isfllow: isfllow
                })
                wx.setStorageSync('isfllow', isfllow);
              } else {
                common.AlertError(msg + '失败');
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