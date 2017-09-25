// pages/planner/evaluateDetails/evaluateDetails.js
var common = require('../../../utils/common.js')
Page({

  /**
   * 页面的初始数据
   */
  data: {
    orderId:"",

    apiUrl: common.apiUrl + "/",
    isSearch: true,
    searchCount: 1,
    pageIndex: 1,
    evaluates: [],

    msg:""
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this;
    var id = options.id;
    if (id == undefined) {
      id = ""
    }
    that.setData({
      orderId: id
    })
    searchList(this, 1)
  },

  bindKeyInputMsg:function(e){
    this.setData({
      msg: e.detail.value
    })
  },
  sendMsg:function(e){
    var that=this;
    if (that.data.msg =="")
      return;
    common.POST({
      url: "/order/replay_evaluate",
      params: {
        orderId: that.data.orderId,
        content: that.data.msg,
        lable: "",
        Sort: 1
      },
      success: function (res, s, m) {
        if (s && res.length != 0) {
          that.setData({
            msg: ''
          })
          Alert('发送成功')
        } else {
          AlertError(m)
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
    this.setData({
      evaluates: [],
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


function searchList(that, sType) {
  if (!that.data.isSearch)
    return;
  common.POST({
    url: "/order/select_evaluate_info",
    params: {
      page: that.data.pageIndex,
      size: common.pageSize,
      orderId: that.data.orderId
    },
    success: function (res, s, m) {
      if (s && res.length != 0) {
        that.setData({
          evaluates: that.data.evaluates.concat(res),
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