// pages/planner/search/search.js
var common = require('../../utils/common.js')

Page({

  /**
   * 页面的初始数据
   */
  data: {
    apiUrl: common.apiUrl+"/",
    colorStr: ["clsLablesColor01", "clsLablesColor02","clsLablesColor03"],
    //search
    isSearch: true,
    searchCount: 1,
    pageIndex: 1,
    searchValue: "",
    planners:[],
    aa: '"帅","酷","漂亮"'
  },

  /**
   * 查询
   */
  searchBindfocus: function () {
    this.setData({
      cancelSearchHidden: "showTag",
    })
  },
  searchBindblur: function (e) {
    if (e.detail.value == "") {
      this.setData({
        cancelSearchHidden: "hideTag",
      })
    }
  },
  searchBindconfirm: function (e) {
    if (e.detail.value == "")
      return;
    var that = this;
    that.setData({
      pageIndex: 1,
      isSearch: true,
      searchValue: e.detail.value,
      planners: []      
    })
    searchList(this);
  },
  /**
   * 取消查询
   */
  cancelSearch: function () {
    wx.hideKeyboard();
    this.setData({
      searchTextAlign: "center",
      swiperHidden: "showTag",
      cancelSearchHidden: "hideTag",
      searchValue: ""
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
    searchList(this, 2)
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
  
  }
})

function searchList(that, sType=1) {
  if (!that.data.isSearch)
    return;
  common.POST({
    url: "/planner/search",
    params: {
      page: that.data.pageIndex,
      size: common.pageSize,
      name: that.data.searchValue
    },
    success: function (res, s, m) {
      if (s && res.length != 0) {
        that.setData({
          planners: that.data.planners.concat(res),
          pageIndex: that.data.pageIndex + 1,
          searchCount: res.length
        })
      }else{
        var sc = sType==1?0:-1;
        that.setData({
          isSearch: false,
          searchCount: sc
        })
      }
    },
    fail: function () { }
  })
}