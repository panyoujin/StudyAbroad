// pages/demand/updateOrder/updateOrder.js
var common = require('../../../utils/common.js')
Page({

  /**
   * 页面的初始数据
   */
  data: {
    orderId:"",
    orderStatus: 0,
    pService:0,
    services: [{ Name: "通知后台", Id: 1 }, { Name: "客服回访", Id: 2 }, { Name: "拟定合同", Id: 3 }, { Name: "线下签约", Id: 4 }, { Name: "平台审查", Id: 5 }, { Name: "付款确认", Id: 6 }, { Name: "服务完成", Id: 7 }]
  },

  bindChangeService: function (e) {
    //console.log(this.data.services[e.detail.value].Id);
    this.setData({
      pService: e.detail.value
    })
  },

  btnSubmit:function(){
    var that=this;
    var pService = that.data.pService;
    var def = that.data.orderStatus;
    if (that.data.orderId == "") {
      that.setData({
        tip: '订单不存在',
      })
      return;
    }
    if (pService+1 <= def){
      that.setData({
        tip: '进度只能往前更新',
      })
      return;
    }
    that.setData({
      tip: '',
    })
    common.POST({
      url: "/order/planer_update_order_status",
      params: {
        OrderId: that.data.orderId,
        StartStatus: that.data.orderStatus,
        EndStatus: that.data.services[that.data.pService].Id
      },
      success: function (res, s, m) {
        if (s) {
          common.Alert('更新成功！')
          that.setData({
            orderStatus: that.data.orderStatus+1,
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
    var that = this;
    var id = options.orderId;
    var orderStatus = options.orderStatus;
    var content = options.content;
    if (id == undefined || id == "undefined" || id == "null") {
      return;
    }
    if (orderStatus == undefined || orderStatus == "undefined" || orderStatus == "null") {
      orderStatus = 0;
    }
    that.setData({
      orderId: id,
      orderStatus: parseInt(orderStatus),
      pService: parseInt(orderStatus)-1
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