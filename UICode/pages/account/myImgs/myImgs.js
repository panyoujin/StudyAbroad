// pages/account/myImgs/myImgs.js
var common = require('../../../utils/common.js')
Page({

  /**
   * 页面的初始数据
   */
  data: {
    filePath:"/img/account/bannerReg.png",
    apiUrl: common.apiUrl+"/",
    isSearch: true,
    searchCount: 1,
    pageIndex: 1,
    imgs: [],
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    searchList(this, 1)
  },

  btnDelImg:function(e){
    var that=this;
    wx.showModal({
      title: "删除",
      content: "确定删除照片？",
      success: function (res) {
        if (res.confirm) {
          common.POST({
            url: "/planner/delete_album",
            params: {
              Id: e.currentTarget.dataset.id
            },
            success: function (res, s, m) {
              if (s) {
                common.Alert("删除成功");
              } else {
                common.AlertError(m);
              }
              that.setData({
                imgs: [],
                isSearch: true,
                searchCount: 1,
                pageIndex: 1
              })
              searchList(that, 1);
            },
            fail: function () { }
          })
        }
      }
    })
    
  },

  //添加图片
  addBtnImg:function(){
    var that = this;
    wx.chooseImage({
      count: 1, // 默认9
      sizeType: ['compressed'], // 可以指定是原图还是压缩图，默认二者都有
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
                    common.Alert("上传成功");
                  } else {
                    common.Alert(m);
                  }
                  that.setData({
                    imgs: [],
                    isSearch: true,
                    searchCount: 1,
                    pageIndex: 1
                  })
                  searchList(that, 1);
                },
                fail: function () { }
              })
            }
            else {
              common.Alert("上传失败");
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
    this.setData({
      imgs: [],
      isSearch: true,
      searchCount: 1,
      pageIndex: 1
    })
    searchList(this, 1);
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
    searchList(this, 2)
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
  
  }
})

function searchList(that, sType) {
  if (!that.data.isSearch)
    return;
  common.POST({
    url: "/userinfo/user_album",
    params: {
      page: that.data.pageIndex,
      size: 6,
    },
    success: function (res, s, m) {
      if (s && res.length != 0) {
        that.setData({
          imgs: that.data.imgs.concat(res),
          pageIndex: that.data.pageIndex + 1,
          searchCount: res.length
        })
      } else {
        var sc = sType == 1 ? 0 : -1;
        that.setData({
          isSearch: false,
          searchCount: sc
        })
      }
    },
    fail: function () { }
  })
}