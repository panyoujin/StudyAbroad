// pages/planner/plannerRegister/plannerRegister.js
var common = require('../../../utils/common.js')

Page({

  /**
   * 页面的初始数据
   */
  data: {
    user:null,

    imgUrl01: "",
    imgUrl02: "",
    imgSaveUrl01: "",
    imgSaveUrl02: "",
    clsImgUrl01: "hideTag",
    clsImgUrl02: "hideTag",
    clsChooseImg01: "clsIdCardImg",
    clsChooseImg02: "clsIdCardImg",

    apiUrl: common.apiUrl + "/",
    pSex: 1,
    pServeice: '',
    pServeiceNum:[],
    services:{},
    pArea:'',
    pAreaNum:[],
    areas:{}
  },

  

  /**
   * 注册
   */
  btnPlannerregister : function(e){
    var that = this;
    var pName = e.detail.value.pName;
    var imgSaveUrl01 = that.data.imgSaveUrl01;
    var imgSaveUrl02 = that.data.imgSaveUrl02;
    var address = e.detail.value.address;
    var record = e.detail.value.record;
    var email = e.detail.value.email;
    var idcard = e.detail.value.idcard;
    var pSex = that.data.pSex;
    var pServeice = that.data.pServeice;
    var pArea = that.data.pArea; 
    if (pName.length == 0 || idcard.length == 0|| imgSaveUrl01.length == 0 || address.length == 0 || record.length == 0 || email.length == 0 || pServeice == -1 || pArea==-1){
      that.setData({
        tip: '提示：姓名、身份证号码、身份证图片、所在地、资历、服务区域、邮箱、服务不能为空！'
      })
      return;
    }
    pServeice = pServeice.substring(0, pServeice.length - 1).substr(1);
    pArea = pArea.substring(0, pArea.length - 1).substr(1)
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
        IDCard: idcard,
        Experience: record,
        IDCardPic: imgSaveUrl01,
        IDCardBackPic: imgSaveUrl02
      },
      success: function (res, s, m) {
        if (s) {
          // var user = wx.getStorageSync('userLoginInfo');
          // if (user !=''){
          //   user.UserType = 2;
          //   wx.setStorageSync('userLoginInfo', user)
          // }

          wx.redirectTo({
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
  },


  /**
     * 选择图片
     */
  btnChooseImage01: function () {
    chooseImage(this, 1);
  },
  /**
   * 选择图片
   */
  btnChooseImage02: function () {
    chooseImage(this, 2);
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
      pArea: e.detail.value,
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
* 认证服务区域
*/
  btnAreaChange: function (e) {
    var that = this;
    var key = e.currentTarget.dataset.key;
    var value = that.data.areas[key].Id;

    var pArea = that.data.pArea;
    if (pArea.indexOf("," + value + ",") >= 0) {
      pArea = pArea.replace(value + ",", "");
    }else{
      pArea = pArea + "," + value + ",";
    }
    pArea = pArea.replace(",,", ",");

    var pAreaNum = that.data.pAreaNum;
    pAreaNum[key] = !(pAreaNum[key] == null ? false : pAreaNum[key]);

    that.setData({
      pArea: pArea,
      pAreaNum: pAreaNum,
    })

    //console.log(pArea.substring(0, pArea.length-1).substr(1));
  },
  /**
  * 认证服务
  */
  btnServiceChange: function (e) {
    var that = this;
    var key = e.currentTarget.dataset.key;
    var value = that.data.services[key].Id;

    var pServeice = that.data.pServeice;
    if (pServeice.indexOf("," + value + ",") >= 0) {
      pServeice = pServeice.replace(value + ",", "");
    }else{
      pServeice = pServeice + "," + value + ",";
    }
    pServeice = pServeice.replace(",,", ",");

    var pServeiceNum = that.data.pServeiceNum;
    pServeiceNum[key] = !(pServeiceNum[key] == null ? false : pServeiceNum[key]);

    that.setData({
      pServeice: pServeice,
      pServeiceNum: pServeiceNum,
    })

    //console.log(pServeice.substring(0, pServeice.length-1).substr(1));
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this;

    var that = this;
    var loginInfo = wx.getStorageSync('userLoginInfo');
    if (loginInfo == "") {
      wx.setStorageSync('backPage', "/pages/planner/plannerRegister/plannerRegister")
      wx.redirectTo({
        url: "/pages/account/login/login"
      });
      return;
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
          if (res.IDCardJust != null && res.IDCardJust != "") {
            that.setData({
              imgUrl01: common.apiUrl + "/" + res.IDCardJust,
              imgSaveUrl01: res.IDCardJust,
              clsImgUrl01: "clsIdCardImg",
              clsChooseImg01: "hideTag",
            })
          }
          if (res.IDCardBack != null && res.IDCardBack != "") {
            that.setData({
              imgUrl02: common.apiUrl + "/" + res.IDCardBack,
              imgSaveUrl02: res.IDCardBack,
              clsImgUrl02: "clsIdCardImg",
              clsChooseImg02: "hideTag",
            })
          }
        }
      },
      fail: function () { }
    })

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

function chooseImage(that, num) {
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

function uploadFileImg(that, url, num) {
  common.PostUpload({
    url: '/upload',
    filePath: url,
    params: {},
    success: function (res, s, m) {
      if (s) {
        if (num == 1) {
          that.setData({
            imgUrl01: common.apiUrl + "/" + res.file_path,
            imgSaveUrl01: res.file_path,
            clsImgUrl01: "clsIdCardImg",
            clsChooseImg01: "hideTag",
          })
        } else {
          that.setData({
            imgUrl02: common.apiUrl + "/" + res.file_path,
            imgSaveUrl02: res.file_path,
            clsImgUrl02: "clsIdCardImg",
            clsChooseImg02: "hideTag",
          })
        }
      } else {
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