// pages/account/applyDemand/applyDemand.js
var common = require('../../../utils/common.js')
Page({

  /**
   * 页面的初始数据
   */
  data: {
    demandId:"",
    orderId: "",
    btnTxt: "点击评价",
    btnSubmit: "btnEditUser",
    schedule: []
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this;
    var id = options.id;
    var demandId = options.demandId
    if (id == undefined) {
      id = ""
    }
    if (demandId == undefined) {
      demandId = ""
      that.setData({
        orderId: id,
        demandId: demandId
      })
    }else{
      that.setData({
        orderId: id,
        demandId: demandId
      })
      return;
    }
    
    common.POST({
      url: "/order/get_order_status",
      params: {
        OrderId: '34c6f07a-66db-11e7-952e-1c1b0d79990b'
      },
      success: function (res, s, m) {
        if (s) {
          that.setData({
            schedule: res
          })
        } else {
          wx.showToast({
            title: '获取信息失败',
            image: '/img/error.png',
            duration: 1500
          })
        }
      },
      fail: function () { }
    })
  },

  btnApply:function(){
    var that = this;
    if (that.data.demandId == ""){
      that.setData({
        tip: "申请的需求不存在！"
      })
      return;
    }
    common.POST({
      url: "/demand_undertake/insert_undertake",
      params: {
        DemandId: that.data.demandId,
        ContractId:"12345678"
      },
      success: function (res, s, m) {
        if (s) {
          wx.showToast({
            title: '申请成功',
            duration: 1500
          })
        } else {
          wx.showToast({
            title: '获取信息失败',
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