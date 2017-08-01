// pages/planner/plannerDetails/plannerDetails.js
var common = require('../../../utils/common.js')
Page({

  /**
   * 页面的初始数据
   */
  data: {
    apiUrl: common.apiUrl +"/",
    isOK : true,
    plannerId:'',
    planner:null,
    evaluate:null,
    lables: null,
    order: null,
    qualifications: null,
    teamlist: null
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this;
    var plannerId = options.id;
    if (plannerId == "" || plannerId== null){
      that.setData({isOK: false })
      return;
    }
    that.setData({ plannerId: plannerId })
    common.POST({
      url: "/planner/plannerinfo",
      params: {
        page: 1,
        size: 1,
        plannerId: plannerId
      },
      success: function (res, s, m) {
        if (s && res.length != 0) {
          if (res != null && res.planner != null) {
            res.planner.HeadImage = common.apiUrl + "/" + res.planner.HeadImage
          }
          that.setData({
            planner: res.planner,
            evaluate: res.evaluate,
            lables: res.lables,
            order: res.order,
            qualifications: res.qualifications,
            teamlist: res.teamlist
          })
          wx.setStorageSync('planner', res.planner);
        } else {
          wx.showToast({
            title: '获取数据失败！' + m,
            image: '/img/error.png',
            duration: 1500
          })
        }
      },
      fail: function () { }
    })
  },

  /**
   * 分享
   */
  btnShare:function(){
    
  },

  /**
   * 关注
   */
  btnFollow: function () {
    var that = this;
    wx.showModal({
      title: '关注',
      content: '确定关注该规划师？',
      success: function (res) {
        if (res.confirm) {
          common.POST({
            url: "/planner/follow",
            params: {
              plannerId: that.data.plannerId
            },
            success: function (res, s, m) {
              if (s) {
                wx.showToast({
                  title: '成功关注该规划师！',
                  duration: 1500
                })
              } else {
                wx.showToast({
                  title: '关注该规划师失败！',
                  image: '/img/error.png',
                  duration: 1500
                })
              }
            },
            fail: function () { }
          })
        }
      }
    })
  },

  btnSelect: function(){
    wx.navigateTo({
      url: "/pages/service/ContractDataAdd/ContractDataAdd?plannerId=" + this.data.plannerId,
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
    var desc = '分享规划师：' + this.data.planner.Name;
    var url = '/pages/planner/plannerDetails/plannerDetails?id=' + this.data.planner.plannerId;
    return {
      title: common.programName,
      desc: desc,
      path: url
    }
  }
})
