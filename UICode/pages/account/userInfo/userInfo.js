// pages/account/userInfo/userInfo.js

var common = require('../../../utils/common.js')
Page({

  /**
   * 页面的初始数据
   */
  data: {
    UserType:1,
    myInfo:null,
    headImage: "",
    isFirst: true
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    //判断用户是否已经登陆
    common.CheckLogin("/pages/account/userInfo/userInfo");
    initData(this);
  },

  logOut:function(){
    wx.setStorageSync('userLoginToken','');
    wx.setStorageSync('userLoginInfo', '');

    common.POST({
      url: "/user/logout",
      params: {},
      success: function (res, s, m) {},
      fail: function () { }
    })

    wx.navigateTo({
      url: '/pages/account/login/login',
    })
  },
  editHeadImg:function(){
    // wx.removeStorageSync("userLoginInfo")
    var that = this;
    wx.chooseImage({
      count: 1, // 默认9
      sizeType: ['original', 'compressed'], // 可以指定是原图还是压缩图，默认二者都有
      sourceType: ['album', 'camera'], // 可以指定来源是相册还是相机，默认二者都有
      success: function (res) {
        //返回选定照片的本地文件路径列表，tempFilePath可以作为img标签的src属性显示图片
        common.PostUpload({
          url: '/upload',
          filePath: res.tempFilePaths[0],
          params: {},
          success: function (res, s, m) {
            if (s) {
              that.setData({ headImage : res.file_path})
              common.POST({
                url: "/userinfo/updateheadimage",
                params: {
                  headimage: res.file_path,
                },
                success: function (res, s, m) {
                  if (s) {
                    var myinfo = that.data.myInfo;
                    myinfo.HeadImage = common.apiUrl + "/" + that.data.headImage;
                    that.setData({
                      myInfo: myinfo
                    })
                    wx.setStorageSync('userLoginInfo', myinfo)
                    common.Alert('修改成功！')
                  } else {
                    common.AlertError('修改失败！')
                  }
                },
                fail: function () { }
              })
            }
            else{
              common.AlertError('修改失败！')
            }
          },
          fail: function () { }
        })
      }
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
    if (!this.data.isFirst){
      init(this);
    }else{
      this.setData({
        isFirst: false
      });
    }
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
    init(this);
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

function init(that){
  //判断用户是否已经登陆
  common.CheckLogin("/pages/account/userInfo/userInfo");
  setTimeout(function () {
    initData(that);
  }, 1000);
}

function initData(that){
  var loginInfo = wx.getStorageSync('userLoginInfo');
  if (loginInfo == "") {
    wx.redirectTo({
      url: "/pages/account/login/login"
    });
  } else {
    that.setData({
      myInfo: loginInfo,
      headImage: loginInfo.HeadImage,
      UserType: loginInfo.UserType
    })
  }
}