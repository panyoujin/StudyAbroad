// pages/sysInfo/contract/contract.js
var common = require('../../../utils/common.js')
Page({

  /**
   * 页面的初始数据
   */
  data: {
    name:"",
    content:"",
    checkContaact:[],
    items: [
      { name: '1', value: '是否同意该协议' },
    ]
  },

  btnNext:function(){
    if (this.data.checkContaact.length > 0){
      wx.navigateTo({
        url: '/pages/service/ServiceAdd/ServiceAdd?addType=1',
      })
    }
  },
  checkboxChange: function (e) {
    this.setData({
      checkContaact: e.detail.value
    })
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that=this;
    common.POST({
      url: "/userinfo/new_contract",
      params: {},
      success: function (res, s, m) {
        if (s) {
          that.setData({
            name: res.Name,
            content: res.Content
          })

        } else {
          common.AlertError("获取合同协议失败");
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