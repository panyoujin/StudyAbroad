// pages/service/ServiceAdd/ServiceAdd.js
var common = require('../../../utils/common.js')
Page({

  /**
   * 页面的初始数据
   */
  data: {
    addType:2,  //1需求2服务
    checkPlannerId:"",
    formSubmit: "formSubmit",
    formSubmitTxt:"确认发布",
    dateNow:"1990-01-01",
    timeStart:"1990-01-01",
    timeEnd: "1990-01-01",
    pService: 0,
    services: {},
    pArea: 0,
    areas: {}
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this;

    var addType = options.addType;
    //需求才需要
    if (addType==1){
      var checkPlannerId = wx.getStorageSync('checkPlannerId');
      if (checkPlannerId == undefined) {
        //已经选择规划师
        checkPlannerId ="";
      }
      that.setData({
        checkPlannerId: checkPlannerId,
        addType:1
      })
    }else{
      wx.setNavigationBarTitle({
        title: '发布服务',
      })
    }

    var date = new Date();
    var year = date.getFullYear();
    var month = date.getMonth() + 1;
    var day = date.getDate();
    var dateNow = [year, month, day].map(formatNumber).join('-');
    that.setData({
      dateNow: dateNow,
      timeStart: dateNow,
      timeEnd: dateNow,
    })


    common.POST({
      url: "/basic/servicelist",
      params: {},
      success: function (res, s, m) {
        if (s) {
          that.setData({
            services: res
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

  bindChangeArea: function(e){
    this.setData({
      pArea: e.detail.value
    })
  },
  bindChangeService: function (e) {
    this.setData({
      pService: e.detail.value
    })
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
    var priceStart = e.detail.value.PriceStart;
    var priceEnd = e.detail.value.PriceEnd;
    var name = e.detail.value.Name;

    if (priceStart.length == 0 || priceEnd.length == 0 || name.length == 0) {
      that.setData({
        tip: '提示：价格范围、描述不能为空！'
      })
      return;
    }
    if (parseInt(priceStart) >= parseInt(priceEnd) || parseInt(priceStart) < 1 || parseInt(priceEnd)>1000000){
      that.setData({
        tip: '提示：价格范围应为1-100W！'
      })
      return;
    }
    that.setData({
      tip: '',
      formSubmit: '',
      formSubmitTxt: "发布中..."
    })
    common.POST({
      url: "/demand_service/insert_browse_service",
      params: {
        Name: name,
        TimeStart: that.data.timeStart,
        TimeEnd: that.data.timeEnd + " 23:59:59",
        PriceStart: priceStart,
        PriceEnd: priceEnd,
        Description: name,
        plannerId: that.data.checkPlannerId,
        ServiceId: that.data.services[that.data.pService].Id,
        ServiceAreaId: that.data.areas[that.data.pArea].Id
      },
      success: function (res, s, m) {
        if (s) {
          that.setData({
            formSubmit: 'formSubmit',
            formSubmitTxt: "确认发布"
          })

          var url ="/pages/demand/demandPublic/demandPublic";
          if (that.data.addType == 1){
            url ="/pages/demand/demandPublic/demandPublic"
          }
          wx.redirectTo({
            url: url,
          })
        } else {
          that.setData({
            tip: m,
            formSubmit: 'formSubmit',
            formSubmitTxt: "确认发布"
          })
        }
      },
      fail: function () {
        that.setData({
          tip: m,
          formSubmit: 'formSubmit',
          formSubmitTxt: "确认发布"
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