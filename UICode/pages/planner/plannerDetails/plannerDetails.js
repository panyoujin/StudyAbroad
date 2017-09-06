// pages/planner/plannerDetails/plannerDetails.js
var common = require('../../../utils/common.js')
Page({

  /**
   * 页面的初始数据
   */
  data: {
    apiUrl: common.apiUrl +"/",
    isOK : true,
    plannerId:'',
    data:null,
    checkPlannerImgs:true,
    checkLable:true,
    isfllow:0,
    userId:"",
    userType:1,
    hidMsgView:true,
    msgFocus:false,
    msg: "",
    colorStr: ["clsLablesColor01", "clsLablesColor02", "clsLablesColor03", 
      "clsLablesColor04", "clsLablesColor05", "clsLablesColor06", "clsLablesColor07"],
    imgUrls: [
      'files/2017-08-25/5f1ced9a-894d-11e7-8d3a-00163e08b8b6.png', 
      "files/2017-08-28/78d06592-8bfe-11e7-8d3a-00163e08b8b6.png", 
    "files/2017-08-28/3ad7f7b4-8bfe-11e7-8d3a-00163e08b8b6.jpg"]
  },

  showSendMsg:function(){
    this.setData({
      hidMsgView: false,
      msgFocus:true
    })
  },
  bindblurMsg: function(){
    this.setData({
      hidMsgView: true,
      msgFocus: false
    })
  },
  bindKeyInputMsg: function (e) {
    this.setData({
      msg: e.detail.value
    })
  },
  sendMsg:function(){
    var that=this;
    if (that.data.msg == "")
      return;
    common.POST({
      url: "/notice/insert_chat",
      params: {
        ReceiveUserId:that.data.plannerId,
        Content: that.data.msg
      },
      success: function (res, s, m) {
        if (s) {
          that.setData({
            hidMsgView: true,
            msgFocus: false,
            msg:''
          })
          wx.showToast({
            title: "发送成功",
            duration: 1500
          })
        } else {
          wx.showToast({
            title: '发送消息失败！' + m,
            image: '/img/error.png',
            duration: 1500
          })
        }
      },
      fail: function () { }
    })
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this;

    var loginInfo = wx.getStorageSync('userLoginInfo');
    if (loginInfo!=""){
      that.setData({ 
        userType: loginInfo.UserType,
        userId: loginInfo.Id
      })
    }

    var plannerId = options.id;
    if (plannerId == "" || plannerId== null){
      that.setData({isOK: false })
      return;
    }
    that.setData({ plannerId: plannerId })
    common.POST({
      url: "/planner/plannerinfo",
      params: {
        page: 1,
        size: 1,
        plannerId: plannerId
      },
      success: function (res, s, m) {
        if (s && res.length != 0) {
          if (res != null && res.planner != null) {
            res.planner.HeadImage = common.apiUrl + "/" + res.planner.HeadImage
          }
          that.setData({
            isfllow: res.fllow_count,
            data:res,
            checkPlannerImgs: res.albumList.length==0?true:false,
            checkLable: res.lables.length != 0 ? true : false
          })
          wx.setStorageSync('planner', res.planner);
          wx.setStorageSync('isfllow', res.fllow_count);
          wx.setStorageSync('ServiceAreaList', res.ServiceAreaList);
          wx.setStorageSync('ServiceTypeList', res.ServiceTypeList);
          wx.setNavigationBarTitle({ title: '规划师 '+res.planner.Name});
        } else {
          common.AlertError(m);
        }
      },
      fail: function () { }
    })
  },

  /**
   * 分享
   */
  btnShare:function(){
    
  },

  /**
   * 关注
   */
  btnFollow: function () {
    var that = this;
    var title ='关注';
    var content = '确定关注该规划师？';
    var msg ="";
    var url = '/planner/follow';
    var isfllow=1;
    if(that.data.isfllow==1){
      title = '取消关注';
      content = '确定取消关注该规划师？';
      url = '/planner/unfollow';
      isfllow=0;
    }
    wx.showModal({
      title: title,
      content: content,
      success: function (res) {
        if (res.confirm) {
          common.POST({
            url: url,
            params: {
              plannerId: that.data.plannerId
            },
            success: function (res, s, m) {
              if (s) {
                common.Alert("成功" + msg);
                that.setData({
                  isfllow: isfllow
                })
                wx.setStorageSync('isfllow', isfllow);
              } else {
                common.AlertError(msg + '失败');
              }
            },
            fail: function () { }
          })
        }
      }
    })
  },

  btnSelect: function(){
    wx.navigateTo({
      url: "/pages/service/ContractDataAdd/ContractDataAdd?plannerId=" + this.data.plannerId,
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
    var isfllow = wx.getStorageSync('isfllow');
    this.setData({
      isfllow: isfllow
    })
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
    var desc = '分享规划师：' + this.data.planner.Name;
    var url = '/pages/planner/plannerDetails/plannerDetails?id=' + this.data.planner.plannerId;
    return {
      title: common.programName,
      desc: desc,
      path: url
    }
  }
})
