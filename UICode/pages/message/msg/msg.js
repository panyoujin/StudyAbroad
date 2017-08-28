// pages/message/msg/msg.js
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
    msgs: [],

    userName:"",
    receiveUserId:"",
    msg:""
  },

  bindKeyInputMsg: function (e) {
    this.setData({
      msg: e.detail.value
    })
  },
  sendMsg: function () {
    var that = this;
    if (that.data.msg == "")
      return;
    common.POST({
      url: "/notice/insert_chat",
      params: {
        ReceiveUserId: that.data.receiveUserId,
        Content: that.data.msg
      },
      success: function (res, s, m) {
        if (s) {
          var msgs = that.data.msgs;
          msgs.splice(0, 0, { UserId: '', Content: that.data.msg, Type: '1', Name: that.data.userName })
          that.setData({
            msgs: msgs,
            msg: ''
          })
          common.Alert("发送成功");
        } else {
          common.AlertError(m);
        }
      },
      fail: function () { }
    })
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this;
    var receiveUserId = options.receiveUserId;
    var id = options.id;
    if (id == "undefined" ||　receiveUserId == "undefined") {
      return;
    }
    that.setData({
      receiveUserId:receiveUserId
    })

    var loginInfo = wx.getStorageSync('userLoginInfo');
    if (loginInfo != null && loginInfo != "")[
      this.setData({
        userName: loginInfo.Name
      })
    ]

    common.POST({
      url: "/notice/update_system_notice_status",
      params: {
        Id: id
      },
      success: function (res, s, m) { },
      fail: function () { }
    })

    searchList(that, 1)
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
    url: "/notice/get_chat_list",
    params: {
      ReceiveUserId: that.data.receiveUserId,
      page: that.data.pageIndex,
      size: 20
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