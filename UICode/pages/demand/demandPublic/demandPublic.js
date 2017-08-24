// pages/demand/demandPublic/demandPublic.js
var common = require('../../../utils/common.js')
Page({

  /**
   * 页面的初始数据
   */
  data: {
    userType: 1,

    isSearch: true,
    searchCount: 1,
    pageIndex: 1,
    demands: [],
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var loginInfo = wx.getStorageSync('userLoginInfo');
    if (loginInfo != null && loginInfo != "")[
      this.setData({
        userType: loginInfo.UserType
      })
    ]
    if (this.data.userType!=1){
      wx.setNavigationBarTitle({
        title: '我发布的服务',
      })
    }
    searchList(this, 1)
  },

  lookDemand: function(e){
    wx.navigateTo({
      url: "/pages/service/serviceDetails/serviceDetails?id=" + e.currentTarget.dataset.id,
    })
  },
  lookJinDu: function (e) {
    wx.navigateTo({
      url: "/pages/account/applyPlanner/applyPlanner?id=" + e.currentTarget.dataset.id,
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
    this.setData({
      demands: [],
      isSearch: true,
      searchCount: 1,
      pageIndex: 1
    })
    searchList(this, 1);
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
    searchList(this, 2)
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
  
  }
})

function searchList(that, sType = 1) {
  if (!that.data.isSearch)
    return;
  common.POST({
    url: "/demand_service/mydemand",
    params: {
      page: that.data.pageIndex,
      size: common.pageSize,
    },
    success: function (res, s, m) {
      if (s && res.length != 0) {
        that.setData({
          demands: that.data.demands.concat(res),
          pageIndex: that.data.pageIndex + 1,
          searchCount: res.length
        })
      } else {
        var sc = sType == 1 ? 0 : -1;
        that.setData({
          isSearch: false,
          searchCount: sc
        })
      }
    },
    fail: function () { }
  })
}