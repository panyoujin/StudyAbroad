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
      url: '/pages/account/educationEdit/educationEdits?timeStart=2017&timeEnd=2017&university=清华大学&degree=博士&id=' + e.currentTarget.dataset.id,
    })
  },
  btnEditSociology: function (e) {
    wx.redirectTo({
      url: '/pages/account/sociologyEdit/sociologyEdit?timeStart=2017&timeEnd=2017&description=社会信息&id=' + e.currentTarget.dataset.id,
    })
  },
  btnEditResources: function (e) {
    wx.redirectTo({
      url: '/pages/account/resourcesEdit/resourcesEdit?timeStart=2017&timeEnd=2017&description=资源信息&&id=' + e.currentTarget.dataset.id,
    })
  },


  btnDelEducation: function (e) {
    common.POST({
      url: "/delete_education",
      params: {
        Id: e.currentTarget.dataset.id
      },
      success: function (res, s, m) {
        if (s && res.length != 0) {
          var educations = this.data.educations;
          for (var i = 0; i < educations.length;i++){
            if (educations[i].Id == e.currentTarget.dataset.id){
              educations.splice(i, 1)
              break;
            }
          }
          this.setData({
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
    common.POST({
      url: "/delete_society",
      params: {
        Id: e.currentTarget.dataset.id
      },
      success: function (res, s, m) {
        if (s && res.length != 0) {
          var societys = this.data.societys;
          for (var i = 0; i < societys.length; i++) {
            if (societys[i].Id == e.currentTarget.dataset.id) {
              societys.splice(i, 1)
              break;
            }
          }
          this.setData({
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
    common.POST({
      url: "/delete_resour",
      params: {
        Id: e.currentTarget.dataset.id
      },
      success: function (res, s, m) {
        if (s && res.length != 0) {
          var resours = this.data.resours;
          for (var i = 0; i < resours.length; i++) {
            if (resours[i].Id == e.resours.dataset.id) {
              resours.splice(i, 1)
              break;
            }
          }
          this.setData({
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