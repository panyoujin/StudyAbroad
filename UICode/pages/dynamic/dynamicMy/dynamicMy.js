// pages/dynamic/dynamicMy/dynamicMy.js
var common = require('../../../utils/common.js')
Page({

  /**
   * 页面的初始数据
   */
  data: {
    apiUrl: common.apiUrl + "/",
    isSearch: true,
    searchCount: 1,
    pageIndex: 1,
    dynamics: [],
    id:''
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var loginInfo = wx.getStorageSync('userLoginInfo');
    if (loginInfo == "") {
      wx.redirectTo({
        url: "/pages/account/login/login"
      });
    } else {
      this.setData({
        id: loginInfo.Id,
      })
    }
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
    this.setData({
      dynamics: [],
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

function searchList(that, sType = 1) {
  if (!that.data.isSearch)
    return;
  common.POST({
    url: "/dynamic/select_user_dynamic_list",
    params: {
      page: that.data.pageIndex,
      size: common.pageSize,
      userid: that.data.id,
    },
    success: function (res, s, m) {
      if (s && res.length != 0) {
        that.setData({
          dynamics: that.data.dynamics.concat(res),
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