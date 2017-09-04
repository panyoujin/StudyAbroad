// pages/service/serviceDetails/serviceDetails.js
var common = require('../../../utils/common.js')
Page({

  /**
   * 页面的初始数据
   */
  data: {
    userType:1,
    demandId:"",
    isOK: true,
    service:[],
    isfllow:0
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this;
    var id = options.id;
    if (id == "" || id == null) {
      that.setData({ isOK: false })
      return;
    }
    that.setData({
      demandId:id
    })

    var loginInfo = wx.getStorageSync('userLoginInfo');
    if (loginInfo == "") {
      wx.redirectTo({
        url: "/pages/account/login/login"
      });
    } else {
      that.setData({
        userType: loginInfo.UserType
      })
    }

    var service = null;

    // var services = wx.getStorageSync("queryServices");
    // var i = 0
    // while (i< services.length){
    //   if (services[i].Id == id){
    //     service = services[i];
    //     break;
    //   }
    //   i++;
    // }
    // if (service == "" || service == null) {
    //   that.setData({ isOK: false })
    //   return;
    // }
    // service.HeadImage = common.apiUrl + "/" + service.HeadImage;
    // that.setData({
    //   service: service
    // })
    
    common.POST({
      url: "/demand_service/demand_service_info",
      params: {
        demandServiceId: id
      },
      success: function (res, s, m) {
        service = res;
        service.HeadImage = common.apiUrl + "/" + service.HeadImage;
        that.setData({
          service: service
        })
       },
      fail: function () { 
        that.setData({ isOK: false })
        return;
      }
    })

    //添加浏览历史
    common.POST({
      url: "/demand_service/browse",
      params: {
        demandServiceId: id
      },
      success: function (res, s, m) {},
      fail: function () { }
    })
  },

  /**
   * 关注
   */
  btnFollow: function () {
    var that = this;
    var title = '收藏';
    var content = '确定收藏该需求/服务';
    var msg = "";
    var url = '/demand_service/collection';
    var isfllow = 1;
    if (that.data.service.isfllow == 1) {
      title = '取消收藏';
      content = '确定取消收藏该需求/服务？';
      url = '/demand_service/uncollection';
      isfllow = 0;
    }
    wx.showModal({
      title: title,
      content: content,
      success: function (res) {
        if (res.confirm) {
          common.POST({
            url: url,
            params: {
              demandServiceId: that.data.service.Id
            },
            success: function (res, s, m) {
              if (s) {
                common.Alert("成功"+msg);
                that.setData({
                  isfllow: isfllow
                })
              } else {
                common.AlertError(msg+"失败");
              }
            },
            fail: function () {  }
          })
        }
      }
    })
  },

  btnSelect: function () {
    
    if (this.data.service.Type=="2"){
      //服务
      var url = "/pages/service/ContractDataAdd/ContractDataAdd?plannerId=" + this.data.service.UserId;
      wx.navigateTo({
        url: url
      })
    }else{
      //承接需求
      addDertake(this);
    }
    
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
    var desc = '分享需求/服务：' + this.data.planner.Name;
    var url = '/pages/service/serviceDetails/serviceDetails?id=' + this.data.service.Id;
    return {
      title: common.programName,
      desc: desc,
      path: url
    }
  }
})


function addDertake (that){
  if (that.data.demandId == "") {
    that.setData({
      tip: "申请的需求不存在！"
    })
    return;
  }
  common.POST({
    url: "/demand_undertake/insert_undertake",
    params: {
      DemandId: that.data.demandId,
      ContractId: "12345678"
    },
    success: function (res, s, m) {
      if (s) {
        wx.showToast({
          title: '承接需求成功',
          duration: 1500
        })
      } else {
        common.AlertError(m);
      }
    },
    fail: function () { }
  })
}