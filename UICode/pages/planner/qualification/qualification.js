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
    data:null,
    educations: null,
    societys: null,
    resours: null,
    colorStr: ["clsLablesColor01", "clsLablesColor02", "clsLablesColor03",
      "clsLablesColor04", "clsLablesColor05", "clsLablesColor06", "clsLablesColor07"],
    imgUrls: [
      'files/2017-08-25/5f1ced9a-894d-11e7-8d3a-00163e08b8b6.png',
      "files/2017-08-28/78d06592-8bfe-11e7-8d3a-00163e08b8b6.png",
      "files/2017-08-28/3ad7f7b4-8bfe-11e7-8d3a-00163e08b8b6.jpg"]
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
    var ServiceAreaList = wx.getStorageSync('ServiceAreaList');
    var ServiceTypeList = wx.getStorageSync('ServiceTypeList');

    that.setData({ 
      planner: planner,
      isfllow: isfllow,
      ServiceAreaList: ServiceAreaList,
      ServiceTypeList: ServiceTypeList
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
    var title = '收藏';
    var content = '确定收藏该规划师？';
    var msg = "";
    var url = '/planner/follow';
    var isfllow = 1;
    if (that.data.isfllow == 1) {
      title = '取消收藏';
      content = '确定取消收藏该规划师？';
      url = '/planner/unfollow';
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