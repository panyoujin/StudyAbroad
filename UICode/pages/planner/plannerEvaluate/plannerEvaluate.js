// pages/planner/plannerEvaluate/plannerEvaluate.js
var common = require('../../../utils/common.js')
Page({
  /**
   * 页面的初始数据
   */
  data: {
    orderId:"",

    synthesisNum:0,
    qualityNum:0,
    efficiencyNum:0,
    synthesisTxt: "很好",
    qualityTxt: "很好",
    efficiencyTxt: "很好",

    lables:["好美啊","悲催的","有效率","服务态度好","very good","非常的差"],

    lable:"",
    lableNum: [false, false, false, false, false, false, false, false, false, false, false, false, false, false, false]
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this;
    var id = options.id;
    if (id == undefined){
      id =""
    }
    that.setData({ 
      orderId: id
    })
    common.POST({
      url: "/planner/get_lable_list",
      params: {
        page:1,
        size:15,
      },
      success: function (res, s, m) {
        if (s) {
          that.setData({
            lables: res
          })
        } else {}
      },
      fail: function () { }
    })
  },

  btnSubmit:function(e){
    var that = this;
    var content = e.detail.value.content;
    var synthesisNum = that.data.synthesisNum;
    var qualityNum = that.data.qualityNum;
    var efficiencyNum = that.data.efficiencyNum;
    var lable = that.data.lable;
    var orderId = that.data.orderId;

    if (orderId == null || orderId.length == 0){
      that.setData({
        tip: '提示：评价订单不存在！'
      })
      return;
    }
    if (content.length == 0 || synthesisNum == 0 || qualityNum == 0 || efficiencyNum == 0 ) {
      that.setData({
        tip: '提示：综合评价、质量评价、效率评价、评价内容不能为空！'
      })
      return;
    }
    that.setData({
      tip: ''
    })
    common.POST({
      url: "/order/insert_evaluate",
      params: {
        orderId: orderId,
        content: content,
        lable: lable,
        Sort: 1,
        synthesis: synthesisNum,
        quality: qualityNum,
        efficiency: efficiencyNum,
      },
      success: function (res, s, m) {
        if (s) {
          wx.showToast({
            title: '评价成功！',
            duration: 1500
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

  btnEvaluateNum: function (e){
    var that = this;
    var key = e.currentTarget.dataset.key;
    var value = e.currentTarget.dataset.value;
    var txt ="很好";
    switch(value){
      case 1:
        txt = "很差"
        break;
      case 2:
        txt = "差"
        break;
      case 3:
        txt = "一般"
        break;
      case 4:
        txt = "好"
        break;
    }


    if (key == "synthesis"){
      that.setData({
        synthesisNum: value,
        synthesisTxt:txt,

      })
    } else if (key == "quality"){
      that.setData({
        qualityNum: value,
        qualityTxt: txt,
      })
    }else{
      that.setData({
        efficiencyNum: value,
        efficiencyTxt:txt,
      })
    }
  },


  btnLable: function(e){
    var that = this;
    var value = e.currentTarget.dataset.value;
    var key = e.currentTarget.dataset.key;

    var lable = that.data.lable;
    if(lable.indexOf("," + value + ",") >= 0){
      var lable = lable.replace(value + ",", "");
    }
    lable = lable + "," + value + ","
    lable = lable.replace(",,", ",");

    var lableNum = that.data.lableNum;
    lableNum[key] = !lableNum[key];

    that.setData({
      lable: lable,
      lableNum: lableNum,
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