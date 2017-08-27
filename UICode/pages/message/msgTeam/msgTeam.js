// pages/message/msgTeam/msgTeam.js
var common = require('../../../utils/common.js')
Page({

  /**
   * 页面的初始数据
   */
  data: {
    userType:1,

    isSearch: true,
    searchCount: 1,
    pageIndex: 1,
    searchValue: "",
    msgs: [],
  },

  btnOk: function (e) {
    common.POST({
      url: "/team/agree_join_team",
      params: {
        NoticeId: e.currentTarget.dataset.id
      },
      success: function (res, s, m) {
        if (s) {
          wx.showToast({
            title: '申请已通过',
            duration: 1500
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
  btnCancel:function(e){
    common.POST({
      url: "/team/disagree_join_team",
      params: {
        NoticeId: e.currentTarget.dataset.id
      },
      success: function (res, s, m) {
        if (s) {
          wx.showToast({
            title: '申请已拒接',
            duration: 1500
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
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

    var loginInfo = wx.getStorageSync('userLoginInfo');
    if (loginInfo != null&& loginInfo != "")[
      this.setData({
        userType: loginInfo.UserType
      })
    ]
    
    //searchList(this, 1)
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
    this.setData({
      msgs: [],
      isSearch: true,
      searchCount: 1,
      pageIndex: 1
    })
    searchList(this, 1);
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
      msgs: [],
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
    url: "/team/get_team_notice",
    params: {
      page: that.data.pageIndex,
      size: common.pageSize
    },
    success: function (res, s, m) {
      if (s && res.length != 0) {
        that.setData({
          msgs: that.data.msgs.concat(res),
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