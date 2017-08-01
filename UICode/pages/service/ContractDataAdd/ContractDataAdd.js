// pages/service/ContractDataAdd/ContractDataAdd.js
var common = require('../../../utils/common.js')
Page({

  /**
   * 页面的初始数据
   */
  data: {
    imgUrl01:"",
    imgUrl02:"",
    clsImgUrl01:"hideTag",
    clsImgUrl02: "hideTag",
    clsChooseImg01: "clsIdCardImg",
    clsChooseImg02: "clsIdCardImg",
    btnTxt: "下一步",
    btnSubmit: "btnSubmit",
    headImage: "",
    pSex: 1,
    user: null
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this;
    var loginInfo = wx.getStorageSync('userLoginInfo');
    if (loginInfo == "") {
      wx.setStorageSync('backPage', "/pages/account/userInfo/userInfo")
      wx.redirectTo({
        url: "/pages/account/login/login"
      });
      return;
    } 

    var plannerId = options.plannerId;
    if (plannerId != undefined) {
      //已选择规划师的情况
      wx.setStorageSync('checkPlannerId', plannerId)
    }else{
      //没有选择择规划师的情况
      wx.setStorageSync('checkPlannerId', '')
    }


    common.POST({
      url: "/userinfo/get_user_info",
      params: {
        userid: loginInfo.Id,
      },
      success: function (res, s, m) {
        if (s) {
          that.setData({
            user: res,
            pSex: res.Sex
          })

          if (res.IDCardJust != null && res.IDCardJust !=""){
            that.setData({
              imgUrl01: common.apiUrl + "/" + res.IDCardJust,
              clsImgUrl01: "clsIdCardImg",
              clsChooseImg01: "hideTag",
            })
          }
          if (res.IDCardBack != null && res.IDCardBack != "") {
            that.setData({
              imgUrl02: common.apiUrl + "/" +res.IDCardBack,
              clsImgUrl02: "clsIdCardImg",
              clsChooseImg02: "hideTag",
            })
          }
        } else {
          wx.showToast({
            title: '获取个人基本信息失败！',
            image: '/img/error.png',
            duration: 1500
          })
        }
      },
      fail: function () { }
    })
  },

  btnSubmit:function(){
    wx.navigateTo({
      url: '/pages/service/ServiceAdd/ServiceAdd?addType=1',
    })
  },
  /**
   * 选择图片
   */
  btnChooseImage01: function () {
    chooseImage(this,1);
  },
  /**
   * 选择图片
   */
  btnChooseImage02: function () {
    chooseImage(this, 2);
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


function chooseImage(that, num){
  wx.chooseImage({
    count: 1, // 默认9
    sizeType: ['original', 'compressed'], // 可以指定是原图还是压缩图，默认二者都有
    sourceType: ['album', 'camera'], // 可以指定来源是相册还是相机，默认二者都有
    success: function (res) {
      //返回选定照片的本地文件路径列表，tempFilePath可以作为img标签的src属性显示图片
      uploadFileImg(that, res.tempFilePaths[0], num);     
    }
  })
}

function uploadFileImg(that,url,num){
  common.PostUpload({
    url: '/upload',
    filePath: url,
    params: {},
    success: function (res, s, m) {
      if (s) {
        if (num == 1) {
          that.setData({
            imgUrl01: common.apiUrl + "/" + res.file_path,
            clsImgUrl01: "clsIdCardImg",
            clsChooseImg01: "hideTag",
          })
        } else {
          that.setData({
            imgUrl02: common.apiUrl + "/" + res.file_path,
            clsImgUrl02: "clsIdCardImg",
            clsChooseImg02: "hideTag",
          })
        }
      }else{
        wx.showToast({
          title: '上传图片失败！',
          image: '/img/error.png',
          duration: 1500
        })
      }
    },
    fail: function () { }
  })
}