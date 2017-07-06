#DS_Order 订单表状态
class OrderStatus:
    #通知后台
    notice_back=1
    #客服回访
    customer_review=2
    #拟定合同
    draw_contract=3
    #线下签约
    offline_contract=4
    #平台审查
    platform_review=5
    #付款确认
    payment_confirmation=6
    #服务完成
    finish=7

#DS_DemandUndertake 需求承接的状态
class DemandUndertakeStatus:
    #申请中
    applying=1
    #申请通过
    applyed=2
    #申请不通过
    disapply=3

#DS_DemandUndertake 是否用户发起
class IsUser:
    #用户发布需求的时候发起
    yes=1
    #规划师发起承接
    no=0