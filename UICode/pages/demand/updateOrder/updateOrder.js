// pages/demand/updateOrder/updateOrder.js
var common = require('../../../utils/common.js')
Page({

  /**
   * 页面的初始数据
   */
  data: {
    orderId:"",
    def:0,
    pService:1,
    services: [{ Name: "通知后台", Id: 1 }, { Name: "客服回访", Id: 2 }, { Name: "拟定合同", Id: 3 }, { Name: "线下签约", Id: 4 }, { Name: "平台审查", Id: 5 }, { Name: "付款确认", Id: 6 }, { Name: "服务完成", Id: 7 }]
  },

  bindChangeService: function (e) {
    console.log(e.detail.value);
    this.setData({
      pService: e.detail.value
    })
  },

  btnSubmit:function(){
    var that=this;
    var pService = that.data.pService;
    var def = that.data.def;
    if (pService <= def){
      that.setData({
        tip: '进度不能往后更新',
      })
      return;
    }
    common.POST({
      url: "/order/planer_update_order_status",
      params: {
        OrderId: that.data.orderId,
        StartStatus: 1,
        EndStatus:1
      },
      success: function (res, s, m) {
        if (s) {
          wx.showToast({
            title: '更新成功！',
            duration: 1500
          })
        } else {
          that.setData({
            tip: m,
          })
        }
      },
      fail: function () {
        that.setData({
          tip: m,
        })
      }
    })
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