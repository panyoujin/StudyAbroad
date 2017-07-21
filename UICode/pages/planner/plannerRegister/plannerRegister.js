// pages/planner/plannerRegister/plannerRegister.js
var common = require('../../../utils/common.js')

Page({

  /**
   * 页面的初始数据
   */
  data: {
    apiUrl: common.apiUrl + "/",
    pSex: 1,
    pServeice: -1,
    services:{},
    pArea:-1,
    areas:{}
  },

  /**
   * 选择图片
   */
  btnChooseImage : function(){
    var that = this;
    wx.chooseImage({
      count: 1, // 默认9
      sizeType: ['original', 'compressed'], // 可以指定是原图还是压缩图，默认二者都有
      sourceType: ['album', 'camera'], // 可以指定来源是相册还是相机，默认二者都有
      success: function (res) {
        //返回选定照片的本地文件路径列表，tempFilePath可以作为img标签的src属性显示图片
        that.setData({
          tempFilePaths : res.tempFilePaths[0]
        })
      }
    })
  },
/**
 * 上传图片
 */
  btnUploadImg:function(e){
    var that = this;
    common.PostUpload({
      url: '/upload',
      filePath: e.currentTarget.dataset.imgurl,
      params: {},
      success: function (res, s, m) {
        if (s) {
          that.setData({
            filePath: common.apiUrl +"/" +　res.file_path
          })
        }
      },
      fail: function () { }
    })
  },

  /**
   * 注册
   */
  btnPlannerregister : function(e){
    var that = this;
    var pName = e.detail.value.pName;
    var idCardImgUrl = e.detail.value.idCardImgUrl;
    var address = e.detail.value.address;
    var record = e.detail.value.record;
    var email = e.detail.value.email;
    var pSex = that.data.pSex;
    var pServeice = that.data.pServeice;
    var pArea = that.data.pArea;

    if (pName.length == 0 || idCardImgUrl.length == 0 || address.length == 0 || record.length == 0 || email.length == 0 || pServeice == -1 || pArea==-1){
      that.setData({
        tip: '提示：姓名、身份证、所在地、资历、服务区域、邮箱、服务不能为空！'
      })
    }
    else {
      that.setData({
        tip: ''
      })
      common.POST({
        url: "/userinfo/upgrade_user",
        params: {
          Sex: pSex,
          Name: pName,
          Address: address,
          ServiceId: pServeice,
          ServiceAreaId: pArea,
          Email: email,
          Experience: record,
          IDCardPic: idCardImgUrl
        },
        success: function (res, s, m) {
          if (s) {
            wx.navigateTo({
              url: '/pages/planner/plannerRegisterSucceed/plannerRegisterSucceed'
            })
          }else{
            that.setData({
              tip: m
            })
          }
        },
        fail: function () { }
      })
    }
  },

  /**
   * 性别选择
   */
  radioSexChange:function(e){
    this.setData({
      pSex: e.detail.value
    });
  },
  /**
  * 认证服务区域
  */
  radioAreaChange: function (e) {
    this.setData({
      pArea: e.detail.value
    });
  },
  /**
  * 认证服务
  */
  radioServiceChange: function (e) {
    this.setData({
      pServeice: e.detail.value
    });
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this;
    common.POST({
      url: "/basic/servicelist",
      params: {},
      success: function (res, s, m) {
        if (s) {
          that.setData({
            services : res
          })
        } else {
          that.setData({
            tip: m
          })
        }
      },
      fail: function () { }
    }),
    common.POST({
      url: "/basic/arealist",
      params: {},
      success: function (res, s, m) {
        if (s) {
          that.setData({
            areas: res
          })
        } else {
          that.setData({
            tip: m
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