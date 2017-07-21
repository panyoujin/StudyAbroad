// pages/service/serviceDetails/serviceDetails.js
var common = require('../../../utils/common.js')
Page({

  /**
   * 页面的初始数据
   */
  data: {
    isOK: true,
    service:[]
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this;
    var id = options.id;
    if (id == "" || id == null) {
      that.setData({ isOK: false })
      return;
    }
    var services = wx.getStorageSync("queryServices");
    var service = null;
    var i = 0
    while (i< services.length){
      if (services[i].Id == id){
        service = services[i];
        break;
      }
      i++;
    }
    if (service == "" || service == null) {
      that.setData({ isOK: false })
      return;
    }
    service.HeadImage = common.apiUrl+"/" + service.HeadImage;
    that.setData({
      service: service
    })

    //添加浏览历史
    common.POST({
      url: "/demand_service/browse",
      params: {
        demandServiceId: id
      },
      success: function (res, s, m) {},
      fail: function () { }
    })
  },

  /**
   * 关注
   */
  btnFollow: function () {
    var that = this;
    wx.showModal({
      title: '关注',
      content: '确定关注该需求/服务？',
      success: function (res) {
        if (res.confirm) {
          common.POST({
            url: "/demand_service/collection",
            params: {
              demandServiceId: that.data.service.Id
            },
            success: function (res, s, m) {
              if (s) {
                wx.showToast({
                  title: '成功关注！',
                  duration: 1500
                })
              } else {
                wx.showToast({
                  title: '关注失败！',
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

  btnSelect: function () {
    wx.navigateTo({
      url: "/pages/account/applyDemand/applyDemand",
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
    var desc = '分享需求/服务：' + this.data.planner.Name;
    var url = '/pages/service/serviceDetails/serviceDetails?id=' + this.data.service.Id;
    return {
      title: common.programName,
      desc: desc,
      path: url
    }
  }
})