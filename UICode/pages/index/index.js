//index.js
//获取应用实例
//JSON.stringify() JSON.parse()
var common = require('../../utils/common.js')
var app = getApp()
Page({
  data: {
    imgUrls: [
      { url: '', src: '/img/home/banner.png' }
    ],
    userInfo: {},
    plannerList:{},
    hidden: true,
    xuqiu: true,
    fuwu: true,
    dongtai: true,
    apiUrl: common.apiUrl+'/'
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
  payPhoneNum: function (e) {
    wx.makePhoneCall({
      phoneNumber: '0752-123456',
    })
  },
  //事件处理函数
  //banner图跳转
  swipclick: function (e) {
    wx.switchTab({
      url: e.currentTarget.dataset.url
    })
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
  onLoad: function () {
    
    // wx.downloadFile({
    //   url: 'http://www.sz.gov.cn/hjbhj/ghjh/zcqjh/200911/P020091106639455042832.pdf',
    //   success: function (res) {
    //     var filePath = res.tempFilePath
    //     wx.openDocument({
    //       filePath: filePath,
    //       success: function (res) {
    //         console.log('打开文档成功')
    //       }
    //     })
    //   }
    // })


    var that = this
    that.setData({
      userInfo: app.globalData.userInfo
    })
    //获取首页规划师
    common.POST({
      url: "/home/planner",
      params: {
        count: 6
      },
      success: function (res, s, m) {
        console.log(res)
        if (s && res.length != 0) {
          that.setData({
            plannerList: res
          })
        } else {
          // var sc = sType == 1 ? 0 : -1;
          // that.setData({
          //   isSearch: false,
          //   searchCount: sc
          // })
        }
      },
      fail: function () { }
    })

    //调用应用实例的方法获取全局数据
    // app.getUserInfo(function(userInfo){
    //   //更新数据
    //   that.setData({
    //     userInfo:userInfo
    //   })
    // })
  }
})
