// pages/dynamic/dynamicAdd/dynamicAdd.js
var common = require('../../../utils/common.js')
Page({

  /**
   * 页面的初始数据
   */
  data: {
    imgUrl:[],
    imgUrlShow:[]
  },

  /**
     * 发布
     */
  btnSubmit: function (e) {
    var that = this;
    var content = e.detail.value.content;

    if (content.length == 0) {
      that.setData({
        tip: '提示：内容不能为空！'
      })
      return;
    }
    that.setData({
      tip: ''
    })
    if (that.data.imgUrl.length>0){
      postUploadImgAndData(that,content);
    }else{
      psotData(that, content, null);
    }
    
  },

  btnCleanImg:function(){
    this.setData({
      imgUrl: [],
      imgUrlShow: []
    })
  },

  btnAddImg:function(){
    var that = this;
    if (that.data.imgUrl.length>0){
      that.setData({
        tip: '提示：图片最多为1张！'
      })
        return;
    }
    wx.chooseImage({
      count: 1, // 默认9
      sizeType: ['original', 'compressed'], // 可以指定是原图还是压缩图，默认二者都有
      sourceType: ['album', 'camera'], // 可以指定来源是相册还是相机，默认二者都有
      success: function (res) {
        //返回选定照片的本地文件路径列表，tempFilePath可以作为img标签的src属性显示图片
        that.setData({
          imgUrl: that.data.imgUrl.concat(res.tempFilePaths),
          imgUrlShow: that.data.imgUrlShow.concat(res.tempFilePaths),
        })
        
      }
    })
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
  
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


function postUploadImgAndData(that, content){
  common.PostUpload({
    url: '/upload',
    filePath: that.data.imgUrl[0],
    params: {},
    success: function (res, s, m) {
      if (s) {
        psotData(that, content, res.file_path);
      }
      else {
        that.setData({
          tip: m
        })
      }
    },
    fail: function () { }
  })
}

function psotData(that, content, imgUrl){
  common.POST({
    url: "/dynamic/insert_dynanic",
    params: {
      content: content,
      imageUrl: imgUrl
    },
    success: function (res, s, m) {
      if (s) {
        wx.navigateTo({
          url: '/pages/dynamic/dynamicMy/dynamicMy'
        })
      } else {
        that.setData({
          tip: m
        })
      }
    },
    fail: function () { }
  })
}