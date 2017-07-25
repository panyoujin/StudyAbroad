//index.js
//获取应用实例
//JSON.stringify() JSON.parse()
var app = getApp()
Page({
    data: {
        imgUrls: [
            {url: '', src: '/img/home/banner.png'}
        ],
        userInfo: {},
        hidden: true
    },
    //点击浮动按钮事件
    alertContent: function (e) {
        var that = this
        that.setData({
            hidden: false
        })
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
        console.log('onLoad')
        var that = this
        that.setData({
            userInfo: app.globalData.userInfo
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
