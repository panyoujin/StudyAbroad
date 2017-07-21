// pages/account/myImgs/myImgs.js
var common = require('../../../utils/common.js')
Page({

  /**
   * 页面的初始数据
   */
  data: {
    filePath:"/img/account/bannerReg.png"
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
  
  },

  //添加图片
  addBtnImg:function(){
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
              common.POST({
                url: "/planner/insert_album",
                params: {
                  PhotoName: Date.now() +"_"+ Math.round(Math.random() * 1000000),
                  Url: res.file_path,
                  Sort : 1
                },
                success: function (res, s, m) {
                  if (s) {
                    wx.showToast({
                      title: '图片上传成功！',
                      duration: 1000
                    })
                  } else {
                    wx.showToast({
                      title: '图片上传失败！' + m,
                      image: '/img/error.png',
                      duration: 1500
                    })
                  }
                },
                fail: function () { }
              })
              that.setData({
                filePath: common.apiUrl + "/" + 　res.file_path
              })
            }
            else {
              wx.showToast({
                title: '图片上传失败！' + m,
                image: '/img/error.png',
                duration: 1500
              })
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