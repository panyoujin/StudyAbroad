// pages/planner/plannerList/plannerList.js
var common = require('../../../utils/common.js')

Page({

  /**
   * 页面的初始数据
   */
  data: {
    page : 1,
    isSearch: true,
    planners:[]
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    plannerList(this);
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
    plannerList(this);
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
  
  }
})

/**
 * 查询
 */
function plannerList(that) {
  if (!that.data.isSearch)
    return;
  var planners = that.data.planners;
  common.POST({
    url: "/planner/search",
    params: {
      page: that.data.page,
      size: 1
    },
    success: function (res, s, m) {
      if (s && res.length != 0) {
        that.setData({
          planners: planners.concat(res),
          page: that.data.page + 1
        })
      }else{
        that.setData({
          isSearch: false
        })
      }
    },
    fail: function () { }
  })
}
