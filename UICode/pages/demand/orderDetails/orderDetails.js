// pages/demand/orderDetails/orderDetails.js
var common = require('../../../utils/common.js')
Page({

  /**
   * 页面的初始数据
   */
  data: {
    orderId:"",
    headImage:"",
    datas:[]
  },

  btnUpdata:function(){
    wx.navigateTo({
      url: '/pages/demand/updateOrder/updateOrder?orderId=' + this.data.orderId + "&orderStatus=" + this.data.datas.OrderStatus,
    })
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this;
    var id = options.id;
    var content = options.content;
    if (id == undefined) {
      return;
    }
    that.setData({
      orderId: id,
      headImage: options.headImage == 'null' ? "/img/person.jpg" : common.apiUrl + "/" + options.headImage,
    })

    common.POST({
      url: "/planner/get_order_detail",
      params: {
        OrderId: id
      },
      success: function (res, s, m) {
        if (s) {
          that.setData({
            datas: res,
          })
        } else {
          wx.showToast({
            title: m,
            image: '/img/error.png',
            duration: 1500
          })
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
    var that=this;
    common.POST({
      url: "/planner/get_order_detail",
      params: {
        OrderId: that.data.orderId
      },
      success: function (res, s, m) {
        if (s) {
          that.setData({
            datas: res,
          })
        } else {
          wx.showToast({
            title: m,
            image: '/img/error.png',
            duration: 1500
          })
        }
      },
      fail: function () { }
    })
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