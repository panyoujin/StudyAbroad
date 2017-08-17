// pages/dynamic/dynamicDetails/dynamicDetails.js
var common = require('../../../utils/common.js')
Page({

  /**
   * 页面的初始数据
   */
  data: {
    id:"",
    dynamic:null
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
      id: id
    })

    common.POST({
      url: "/dynamic/select_dynamic_info",
      params: {
        dynamicId:id,
      },
      success: function (res, s, m) {
        if (s && res.length != 0) {
          var data = res[0];
          data.HeadImage = common.apiUrl + "/"+data.HeadImage;
          that.setData({
            dynamic: data,
          })
        } else {
          wx.showToast({
            title: '获取动态详情失败',
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
    var desc = '分享动态';
    var url = '/pages/dynamic/dynamicDetails/dynamicDetails?id=' + this.data.id;
    return {
      title: common.programName,
      desc: desc,
      path: url
    }
  }
})