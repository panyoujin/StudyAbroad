//index.js
//获取应用实例
//JSON.stringify() JSON.parse()
var common = require('../../utils/common.js')
var app = getApp()
Page({
  data: {
    imgUrls: [],
    userInfo: {},
    plannerList:{},
    hidden: true,
    xuqiu: true,
    fuwu: true,
    dongtai: true,
    apiUrl: common.apiUrl+'/',

    phone:'',
    followUrl:"",
    vIcon:"",
    areas:[]

  },
  //点击浮动按钮事件
  alertContent: function (e) {
    //判断用户是否已经登陆
    common.CheckLogin("");

    var loginInfo = wx.getStorageSync('userLoginInfo');
    var that = this
    that.setData({
      hidden: false
    })
    //普通用户
    if (loginInfo.UserType == 1) {
      that.setData({
        xuqiu: false
      })
    } else {
      that.setData({
        fuwu: false,
        dongtai: false
      })
    }
  },
  //点击弹窗的确定事件
  confirm: function (e) {
    this.setData({
      hidden: true
    });
  },
  //点击后隐藏
  btnHideWindows:function(){
    this.setData({
      hidden: true
    });
  },
  payPhoneNum: function (e) {
    wx.makePhoneCall({
      phoneNumber: this.data.phone,
    })
  },

  //banner图跳转
  swipclick: function (e) {
    
  },
  //查询
  searchBtnClick: function () {
    wx.navigateTo({
      url: "/pages/planner/plannerSearch/plannerSearch"
    })
  },

  bindViewTap: function () {
    wx.switchTab({
      url: '../logs/logs'
    })
  },

  //流程
  btnProcess:function(){
    wx.navigateTo({
      url: '/pages/sysInfo/process/process?img=' + this.data.followUrl,
    })
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
    init(this);
  },

  onLoad: function () {
    var that = this

    init(that);

    // that.setData({
    //   userInfo: app.globalData.userInfo
    // })

    //获取首页banner
    common.POST({
      url: "/home/carousel",
      params: {
        count:5
      },
      success: function (res, s, m) {
        if (s && res.length != 0) {
          that.setData({
            imgUrls: res
          })
        } else {
        }
      },
      fail: function () { }
    })
  }


})

function init(that){
  //获取首页banner
  common.POST({
    url: "/home/carousel",
    params: {
      count: 5
    },
    success: function (res, s, m) {
      if (s && res.length != 0) {
        that.setData({
          imgUrls: res
        })
      } else {
      }
    },
    fail: function () { }
  })
  //配置信息
  common.POST({
    url: "/basic/get_config_all",
    params: {},
    success: function (res, s, m) {
      if (s) {
        var config = res;
        for (var i in config) {
          switch (config[i].Key) {
            case 'phone':
              that.setData({
                phone: config[i].Value
              })
              break;
            case 'follow':
              that.setData({
                followUrl: common.apiUrl + '/' + config[i].Img
              })
              break;
            case 'vIcon':
              that.setData({
                vIcon: common.apiUrl + '/' + config[i].Img
              })
              break;
            case 'areas':
              that.setData({
                areas: config[i].Value.split(',')
              })
              break;
          }
        }
      } else {
      }
    },
    fail: function () { }
  })

  //获取首页规划师
  common.POST({
    url: "/home/planner",
    params: {
      count: 6
    },
    success: function (res, s, m) {
      if (s && res.length != 0) {
        for (var i = 0; i < res.length;i++){
          if (res[i].Name.length>3){
            res[i].Name = res[i].Name.substring(0,2)+'..'
            }
        }
        that.setData({
          plannerList: res
        })
      } else {
      }
    },
    fail: function () { }
  })
}
