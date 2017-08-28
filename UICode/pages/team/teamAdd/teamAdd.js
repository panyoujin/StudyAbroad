// pages/team/teamAdd/teamAdd.js
var common = require('../../../utils/common.js')
Page({

  /**
   * 页面的初始数据
   */
  data: {
    apiUrl: common.apiUrl + "/",
    pArea: -1,
    areas: {}
  },
  /**
  * 认证服务区域
  */
  radioAreaChange: function (e) {
    this.setData({
      pArea: e.detail.value,
    });
  },
  /**
  * 提交
  */
  btnSubmit:function(e){
    var that = this;
    var name = e.detail.value.name;
    var teamContent = e.detail.value.teamContent;
    var pArea = that.data.pArea;

    if (name.length == 0 || pArea == -1 || teamContent.length == 0) {
      that.setData({
        tip: '提示：团队名字、认证服务区域、团队服务重点不能为空！'
      })
      return;
    }
    that.setData({
      tip: ''
    })
    common.POST({
      url: "/planner/insert_team",
      params: {
        name: name,
        serviceDescription: teamContent,
        serviceAreaId: pArea,
      },
      success: function (res, s, m) {
        if (s) {
          common.Alert('创建成功');
        } else {
          that.setData({
            tip: m
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
    var that=this;
    common.POST({
      url: "/basic/arealist",
      params: {},
      success: function (res, s, m) {
        if (s) {
          that.setData({
            areas: res
          })
        } else {
          that.setData({
            tip: m
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
  
  }
})