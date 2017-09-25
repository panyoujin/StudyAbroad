// pages/account/editUser/editUser.js
var common = require('../../../utils/common.js')
Page({

  /**
   * 页面的初始数据
   */
  data: {
    btnTxt:"保存修改",
    btnSubmit:"btnEditUser",
    headImage:"",
    pSex:1,
    user:null
  },


  /**
   * 性别选择
   */
  radioSexChange: function (e) {
    this.setData({
      pSex: e.detail.value
    });
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
    } else {
      that.setData({
        headImage: loginInfo.HeadImage
      })
      common.POST({
        url: "/userinfo/get_user_info",
        params: {
          userid: loginInfo.Id,
        },
        success: function (res, s, m) {
          if (s) {
            that.setData({
              user: res,
              pSex:res.Sex
            })
          } else {
            AlertError('获取信息失败！')
          }
        },
        fail: function () { }
      })
    }
  },

  // 修改
  btnEditUser: function (e) {
    var that = this;
    var pName = e.detail.value.name;
    var age = e.detail.value.age;
    var educational = e.detail.value.educational;
    var address = e.detail.value.address;
    var eMail = e.detail.value.eMail;

    if (pName.length == 0){
      that.setData({
        tip: '提示：姓名不能为空！'
      })
      return;
    }
    if (parseInt(age) < 18 || parseInt(age)>70) {
      that.setData({
        tip: '提示：年龄必须为18-70！'
      })
      return;
    }
    that.setData({
      tip: '',
      btnTxt: "保存修改中...",
      btnSubmit:''
    })
    common.POST({
      url: "/userinfo/updateuserinfo",
      params: {
        name: pName,
        sex: that.data.pSex,
        age: age,
        education: educational,
        address: address,
        email: eMail,
      },
      success: function (res, s, m) {
        if (s) {
          Alert('修改成功！')
          wx.navigateBack({})
        } else {
          AlertError('修改失败！')
        }
        that.setData({
          btnTxt: "保存修改",
          btnSubmit: 'btnEditUser'
        })
      },
      fail: function () {
        that.setData({
          btnTxt: "保存修改",
          btnSubmit: 'btnEditUser'
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