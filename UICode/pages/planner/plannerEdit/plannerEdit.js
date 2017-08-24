// pages/planner/plannerEdit/plannerEdit.js
var common = require('../../../utils/common.js')
Page({

  /**
   * 页面的初始数据
   */
  data: {
    isOK: true,
    planner: null,
    educations: null,
    societys: null,
    resours: null
  },


  btnAddEducation:function(){
    wx.redirectTo({
      url: '/pages/account/educationEdit/educationEdits',
    })
  },
  btnAddSociology: function () {
    wx.redirectTo({
      url: '/pages/account/sociologyEdit/sociologyEdit',
    })
  },
  btnAddResources: function () {
    wx.redirectTo({
      url: '/pages/account/resourcesEdit/resourcesEdit',
    })
  },

  btnEditEducation: function (e) {
    wx.redirectTo({
      url: '/pages/account/educationEdit/educationEdits?timeStart=' + e.currentTarget.dataset.timestart + '&timeEnd=' + e.currentTarget.dataset.timeend + '&university=' + e.currentTarget.dataset.university + '&degree=' + e.currentTarget.dataset.degree+'&id=' + e.currentTarget.dataset.id,
    })
  },
  btnEditSociology: function (e) {
    wx.redirectTo({
      url: '/pages/account/sociologyEdit/sociologyEdit?timeStart=' + e.currentTarget.dataset.timestart + '&timeEnd=' + e.currentTarget.dataset.timeend + '&description=' + e.currentTarget.dataset.description + '&id=' + e.currentTarget.dataset.id,
    })
  },
  btnEditResources: function (e) {
    wx.redirectTo({
      url: '/pages/account/resourcesEdit/resourcesEdit?timeStart=' + e.currentTarget.dataset.timestart + '&timeEnd=' + e.currentTarget.dataset.timeend + '&description=' + e.currentTarget.dataset.description + '&&id=' + e.currentTarget.dataset.id,
    })
  },


  btnDelEducation: function (e) {
    var that = this;
    common.POST({
      url: "/planner/delete_education",
      params: {
        Id: e.currentTarget.dataset.id
      },
      success: function (res, s, m) {
        if (s) {
          var educations = that.data.educations;
          for (var i = 0; i < educations.length;i++){
            if (educations[i].Id == e.currentTarget.dataset.id){
              educations.splice(i, 1)
              break;
            }
          }
          that.setData({
            educations: educations
          })
        } else {
          common.AlertError("删除失败");
        }
      },
      fail: function () { }
    })
  },
  btnDelSociology: function (e) {
    var that = this;
    common.POST({
      url: "/planner/delete_society",
      params: {
        Id: e.currentTarget.dataset.id
      },
      success: function (res, s, m) {
        if (s) {
          var societys = that.data.societys;
          for (var i = 0; i < societys.length; i++) {
            if (societys[i].Id == e.currentTarget.dataset.id) {
              societys.splice(i, 1)
              break;
            }
          }
          that.setData({
            societys: societys
          })
        } else {
          common.AlertError("删除失败");
        }
      },
      fail: function () { }
    })
  },
  btnDelResources: function (e) {
    var that=this;
    common.POST({
      url: "/planner/delete_resour",
      params: {
        Id: e.currentTarget.dataset.id
      },
      success: function (res, s, m) {
        if (s && res.length != 0) {
          var resours = that.data.resours;
          for (var i = 0; i < resours.length; i++) {
            if (resours[i].Id == e.currentTarget.dataset.id) {
              resours.splice(i, 1)
              break;
            }
          }
          that.setData({
            resours: resours
          })
        } else {
          common.AlertError("删除失败");
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
    var loginInfo = wx.getStorageSync('userLoginInfo');
    if (loginInfo == "") {
      wx.redirectTo({
        url: "/pages/account/login/login"
      });
    } else {
      that.setData({
        planner: loginInfo,
        headImage: loginInfo.HeadImage,
        UserType: loginInfo.UserType
      })
    }

    common.POST({
      url: "/planner/qualifications",
      params: {
        page: 1,
        size: 10,
        plannerId: loginInfo.Id
      },
      success: function (res, s, m) {
        if (s && res.length != 0) {
          that.setData({
            educations: res.education,
            societys: res.society,
            resours: res.resour,
          })
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