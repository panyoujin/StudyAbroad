// pages/demand/orderDetails/orderDetails.js
var common = require('../../../utils/common.js')
Page({

  /**
   * 页面的初始数据
   */
  data: {
    name:'',
    phone:"",
    description:"",
    headImage:"",
    orderId:"",

    statuss:[]
  },

  btnUpdata:function(){
    wx.navigateTo({
      url: '/pages/demand/updateOrder/updateOrder',
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
      name: options.name == 'null' ? '':options.name,
      phone: options.phone == 'null' ? '' : options.phone,
      description: options.description == 'null' ? '' : options.description,
      headImage: options.headImage == 'null'?"/img/person.jpg":common.apiUrl + "/" + options.headImage,
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
            statuss: res
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