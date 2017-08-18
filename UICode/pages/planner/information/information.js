// pages/planner/information/information.js
var common = require('../../../utils/common.js')
Page({

  /**
   * 页面的初始数据
   */
  data: {
    isSearch: true,
    searchCount: 1,
    pageIndex: 1,
    searchValue: "",
    informations: [],
  },

  openFile: function (e) {
    wx.downloadFile({
      url: common.apiUrl+"/"+e.currentTarget.dataset.url,
      success: function (res) {
        var filePath = res.tempFilePath
        wx.openDocument({
          filePath: filePath,
          success: function (res) {},
          fail: function () {
            common.AlertError("打开资料失败");
          }
        })
      }
    })
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    searchList(this, 1)
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
    searchList(this, 2)
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
  
  }
})


function searchList(that, sType = 1) {
  if (!that.data.isSearch)
    return;
  common.POST({
    url: "/userinfo/select_user_file",
    params: {
      page: that.data.pageIndex,
      size: 20
    },
    success: function (res, s, m) {
      if (s && res.length != 0) {
        that.setData({
          informations: that.data.informations.concat(res),
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