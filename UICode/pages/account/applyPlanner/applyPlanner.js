// pages/account/applyPlanner/applyPlanner.js
var common = require('../../../utils/common.js')
Page({

  /**
   * 页面的初始数据
   */
  data: {
    orderId:"",
    btnTxt: "点击评价",
    btnSubmit: "btnSubmit",
    schedule:[]
  },

  btnSubmit:function(){
    wx.navigateTo({
      url: '/pages/planner/plannerEvaluate/plannerEvaluate?id=' + this.data.orderId,
    })
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this;
    var id = options.id;
    if (id == undefined) {
      return;
    }
    that.setData({
      orderId: id
    })

    common.POST({
      url: "/order/get_order_status",
      params: {
        OrderId: id
      },
      success: function (res, s, m) {
        if (s) {
          that.setData({
            schedule: res
          })
        } else {
          AlertError('获取信息失败')
        }
      },
      fail: function () { }
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