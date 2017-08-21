// pages/account/resourcesEdit/resourcesEdit.js
var common = require('../../../utils/common.js')
Page({

  /**
   * 页面的初始数据
   */
  data: {
    id: '',
    description: '',

    formSubmit: "formSubmit",
    formSubmitTxt: "新增",
    dateNow: "1900-01-01",
    timeStart: "1990-01-01",
    timeEnd: "1990-01-01",
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this;
    var id = options.id;
    if (id != undefined) {
      that.setData({
        id: id,
        description: options.description,
        timeStart: options.timeStart,
        timeEnd: options.timeEnd,
        formSubmitTxt: '编辑'
      })
    } else {
      var date = new Date();
      var year = date.getFullYear();
      var month = date.getMonth() + 1;
      var day = date.getDate();
      var dateNow = [year, month, day].map(formatNumber).join('-');
      that.setData({
        // dateNow: dateNow,
        timeStart: dateNow,
        timeEnd: dateNow,
      })
    }
  },

  bindTimeStartChange: function (e) {
    this.setData({
      timeStart: e.detail.value
    })
  },
  bindTimeEndChange: function (e) {
    this.setData({
      timeEnd: e.detail.value
    })
  },

  /** 表单按钮事件 */
  formSubmit: function (e) {
    var that = this;
    var description = e.detail.value.Description;

    if (description.length==0) {
      that.setData({
        tip: '提示：资源详情不能为空！'
      })
      return;
    }
    that.setData({
      tip: '',
      formSubmit: '',
      formSubmitTxt: "提交中..."
    })
    var url = "/planner/insert_resour";
    var txt = "新增";
    if (that.data.id != '') {
      url = "/planner/update_resour";
      txt = "编辑";
    }
    common.POST({
      url: url,
      params: {
        Id:that.data.id,
        TimeStart: that.data.timeStart,
        TimeEnd: that.data.timeEnd,
        Description: description,
        Sort: 0
      },
      success: function (res, s, m) {
        if (s) {
          that.setData({
            formSubmit: 'formSubmit',
            formSubmitTxt: txt
          })
          wx.redirectTo({
            url: '/pages/planner/plannerEdit/plannerEdit',
          })
        } else {
          that.setData({
            tip: m,
            formSubmit: 'formSubmit',
            formSubmitTxt: txt
          })
        }
      },
      fail: function () {
        that.setData({
          tip: m,
          formSubmit: 'formSubmit',
          formSubmitTxt: txt
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

function formatNumber(n) {
  n = n.toString()
  return n[1] ? n : '0' + n
}