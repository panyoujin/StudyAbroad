// pages/team/teamManage/teamManage.js
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
    teams:[],

    myTeam:null,
  },
  /**
   * 查询
   */
  searchBindconfirm: function (e) {
    var that = this;
    if (e.detail.value == "") {
      that.setData({
        searchCount: -2
      })
      return;
    }
    that.setData({
      pageIndex: 1,
      isSearch: true,
      searchValue: e.detail.value,
      teams: []
    })
    searchList(this);
  },

  /**
   * 团队详情
   */
  btnLookTeam:function(){
    wx.navigateTo({
      url: '/pages/planner/plannerMy/plannerMy?url=team&temaId=1&temaName=团队001',
    })
  },
  /**
  * 团队创建
  */
  btnTeamAdd: function () {
    wx.navigateTo({
      url: '/pages/team/teamAdd/teamAdd',
    })
  },
  /**
   * 团队申请加入
   */
  btnJoin:function(e){
    var that = this;
    if (e.currentTarget.dataset.Isjoin == 1){
      wx.showToast({
        title: '您已经是该团队成员',
        duration: 1500
      })
      return;
    }
    common.POST({
      url: "/team/join_team",
      params: {
        TeamId: e.currentTarget.dataset.id
      },
      success: function (res, s, m) {
        if (s) {
          wx.showToast({
            title: '已申请加入改团队',
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
    var that = this;
    var value = options.value;
    if (value == undefined) {
      value = ""
    }
    that.setData({
      searchValue: value
    })
    searchList(this);

    var loginInfo = wx.getStorageSync('userLoginInfo');
    if (loginInfo == "") {
      wx.redirectTo({
        url: "/pages/account/login/login"
      });
    } 
    common.POST({
      url: "/planner/select_user_team",
      params: {
        userid: loginInfo.Id
      },
      success: function (res, s, m) {
        if (s) {
          that.setData({
            myTeam: res
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
    this.setData({
      teams: [], 
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
    url: "/team/team_list",
    params: {
      page: that.data.pageIndex,
      size: common.pageSize,
      name: that.data.searchValue
    },
    success: function (res, s, m) {
      if (s && res.length != 0) {
        that.setData({
          teams: that.data.teams.concat(res),
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