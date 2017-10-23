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

    myInfo:null,
    myTeam:null,

    editTeamName: "",
    teamFocus: false,
    editTeamHidden:true,
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
   * 修改团队名称
   */
  bindKeyInputTeamName: function (e) {
    this.setData({
      editTeamName: e.detail.value
    })
  },
  btnEditTeamNameShow: function () {
    var that = this;
    if (that.data.myTeam.UserName != that.data.myInfo.Name)return;
    that.setData({
      editTeamHidden: !that.data.editTeamHidden,
      teamFocus: true
    })
  },
  btnEditTeamName:function(){
    var that = this;
    var myTeam = that.data.myTeam;
    if (that.data.editTeamName == "")
      return;
    common.POST({
      url: "/team/update_team_name",
      params: {
        TeamId: myTeam.Id,
        TeamName: that.data.editTeamName
      },
      success: function (res, s, m) {
        if (s) {
          common.Alert("修改成功");
          myTeam.TeamName = that.data.editTeamName;
          that.setData({
            myTeam: myTeam
          })
        } else {
          common.AlertError(m);
          
        }
      },
      fail: function () { }
    })
  },
  /**
   * 团队详情
   */
  btnLookTeam:function(){
    wx.navigateTo({
      url: '/pages/planner/plannerMy/plannerMy?url=team&temaId=' + this.data.myTeam.Id + '&temaName=' + this.data.myTeam.TeamName,
    })
  },
  btnDelTeam:function(){
    var that = this;
    wx.showModal({
      title: "退出团队",
      content: "你确定退出该团队？",
      success: function (res) {
        if (res.confirm) {
          common.POST({
            url: "/team/quit_team",
            params: {
              TeamId: that.data.myTeam.Id
            },
            success: function (res, s, m) {
              if (s) {
                common.Alert("成功");
                that.setData({
                  myTeam: null
                })
              } else {
                common.AlertError(m);
              }
            },
            fail: function () { }
          })
        }
      }
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
      common.Alert("已是团成员");
      return;
    }
    common.POST({
      url: "/team/join_team",
      params: {
        TeamId: e.currentTarget.dataset.id
      },
      success: function (res, s, m) {
        if (s) {
          common.Alert("申请成功");
        } else {
          common.AlertError('已加过团队');
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

    var loginInfo = wx.getStorageSync('userLoginInfo');
    if (loginInfo == "") {
      wx.redirectTo({
        url: "/pages/account/login/login"
      });
    } else {
      that.setData({
        myInfo: loginInfo,
      })
    }
    
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
    var that = this;
    searchList(that);

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