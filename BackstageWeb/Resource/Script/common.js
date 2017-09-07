var APIHost = '/backweb';
//localhost:8083';

jQuery.loginAjax = function (url, param, successCallBack, failCallBack) {
    var UToken = sessionStorage["UToken"];
    url = url.indexOf("?") > 0 ? url + "&UToken=" + UToken : url + "?UToken=" + UToken;
    url = APIHost + url;
    $.ajax({
        async: true, dataType: "json", type: 'post', url: url, timeout: 600000, data: param ? param : null,
        success: function (jsonData) {
            successCallBack(jsonData);
        },
        error: function () {
            if (failCallBack) failCallBack();
        }
    });
}

//异步ajax操作,返回json结果集
jQuery.ajaxJson = function (url, param, successCallBack, failCallBack) {
    var UToken = sessionStorage["UToken"];
    url = url.indexOf("?") > 0 ? url + "&UToken=" + UToken : url + "?UToken=" + UToken;
    url = APIHost + url;
    $.ajax({
        async: true, dataType: "json", type: 'post', url: url, timeout: 600000, data: param ? param : null,
        success: function (jsonData) {
            if (jsonData.status == "600") {
                window.top.gotoLogin();
            } else if (jsonData.NoPermission) {
                $.alert("您没有权限执行该操作，请与管理员联系！");
            } else if (jsonData.status != "200") {
                $.alert("该操作出现异常，请与管理员联系！错误信息：" + jsonData.message);
            } else {
                if (successCallBack) successCallBack(jsonData);
                $.filterPermission(); //过滤权限
            }
            if ((self.frameElement && self.frameElement.tagName == "IFRAME") || (window.frames.length != parent.frames.length) || (self != top)) {
                window.parent.autoHeight();
            }
            if (jsonData.NoDataPermission) {
                $.alert(jsonData.Message);
            }
        },
        error: function () {
            if (failCallBack) failCallBack();
        }
    });
}
//异步提交表单,返回json结果集
jQuery.ajaxForm = function (url, formId, successCallBack, failCallBack) {
    var UToken = sessionStorage["UToken"];
    url = url.indexOf("?") > 0 ? url + "&UToken=" + UToken : url + "?UToken=" + UToken;
    url = APIHost + url;
    $.ajax({
        async: true, dataType: "json", type: 'post', url: url, timeout: 60000, data: $("#" + formId).serialize(),
        success: function (jsonData) {
            if (jsonData) {
                if (jsonData.status == "600") {
                    window.top.gotoLogin();
                } else if (jsonData.NoPermission) {
                    $.alert("您没有权限执行该操作，请与管理员联系！");
                } else if (jsonData.status != "200") {
                    $.alert("该操作出现异常，请与管理员联系！错误信息：" + jsonData.message);
                } else {
                    if (successCallBack) successCallBack(jsonData);
                }
            } else {
                if (failCallBack) failCallBack(jsonData);
            }
            if ((self.frameElement && self.frameElement.tagName == "IFRAME") || (window.frames.length != parent.frames.length) || (self != top)) {
                window.parent.autoHeight();
            }
        },
        error: function () {
            if (failCallBack) failCallBack();
        }
    });
}

// 时间字符格式化
Date.prototype.format = function (format) {
    var o = {
        "M+": this.getMonth() + 1,
        "d+": this.getDate(),
        "h+": this.getHours(),
        "m+": this.getMinutes(),
        "s+": this.getSeconds(),
        "q+": Math.floor((this.getMonth() + 3) / 3),
        "S": this.getMilliseconds()
    };
    if (/(y+)/.test(format)) format = format.replace(RegExp.$1, (this.getFullYear() + "").substr(4 - RegExp.$1.length));
    for (var k in o) if (new RegExp("(" + k + ")").test(format)) format = format.replace(RegExp.$1, RegExp.$1.length == 1 ? o[k] : ("00" + o[k]).substr(("" + o[k]).length));
    return format;
}
// 将json格式的时间转换为时间字符
String.prototype.toDateTime = function () {
    jsonDate = this;
    if (jsonDate != null) {
        var rDate = new Date(parseInt(jsonDate.replace("/Date(", "").replace(")/", ""), 10));
        return rDate.format("yyyy-MM-dd hh:mm:ss").replace("1900-01-01 00:00:00", "").replace("9999-12-31 23:59:59", "");
    }
    return null;
}
// 将json格式的时间转换为日期字符
String.prototype.toDate = function () {
    jsonDate = this;
    if (jsonDate != null) {
        var rDate = new Date(parseInt(jsonDate.replace("/Date(", "").replace(")/", ""), 10));
        return rDate.format("yyyy-MM-dd").replace("1900-01-01", "").replace("9999-12-31", "");
    }
    return null;
}
String.prototype.replaceAll = function (s1, s2) {
    str = this;
    return (new String(str)).replace(new RegExp(s1, "gm"), s2);
}; //g=global, m=multiLine

//自定义提示框
jQuery.alert = function (message, yes, close) {
    top.layer.alert(message, {
            shift: -1,
            end: function () {
                if (yes) {
                    yes();
                }
                if (close) {
                    jQuery.layerClose();
                }
            }
        },
        function (index) {
            top.layer.close(index);
        });
};
//自定义确认框
jQuery.confirm = function (message, yes, cancel) {
    top.layer.confirm(message, {shift: -1}, function (index) {
        top.layer.close(index);
        if (yes) {
            yes();
        }
    }, function () {
        if (cancel) {
            cancel();
        }
    });
};
//自定义弹出框
jQuery.Dialog = function (url, title, width, height, complete) {
    var UToken = sessionStorage["UToken"];
    url = url.indexOf("?") > 0 ? url + "&UToken=" + UToken : url + "?UToken=" + UToken;
    var _width = width.toString().indexOf("px") > 0 ? width : width + "px";
    var _height = height.toString().indexOf("px") > 0 ? height : height + "px";
    top.layer.open({
        type: 2,
        title: title,
        area: [_width, _height],
        skin: 'layui-layer-rim',
        content: [url, 'auto'],
        scrollbar: true,
        shift: -1,
        end: function () {
            if (complete) complete();
        }
    });

};
//自定义弹出层关闭
jQuery.layerClose = function () {
    top.layer.closeAll();
};

//权限过滤
jQuery.filterPermission = function () {
    //IE8 数组不支持indexOf
    if (!Array.prototype.indexOf) {
        Array.prototype.indexOf = function (elt /*, from*/) {
            var len = this.length >>> 0;
            var from = Number(arguments[1]) || 0;
            from = (from < 0)
                ? Math.ceil(from)
                : Math.floor(from);
            if (from < 0)
                from += len;
            for (; from < len; from++) {
                if (from in this &&
                    this[from] === elt)
                    return from;
            }
            return -1;
        };
    }

    var hidden = $("#Permissions", window.top.document);
    if (hidden.length > 0 && hidden.val().length > 0) {
        var permissions = hidden.val().split(",");
        var items = $("body [filterPermission]");
        if (items.length > 0) {
            items.each(function () {
                var thisfilter = $(this).attr("filterPermission");
                if (thisfilter == "" || permissions.indexOf(thisfilter) == -1) {
                    $(this).remove();
                } else if (permissions.indexOf(thisfilter) > -1) {
                    $(this).show();
                }
            });
        }
    }

}
//展开隐藏的列,如果隐藏的是一个table，则不额外添加信息
var showDetailTable = function (e, isTable) {
    e = $(e);
    var parentTr = e.parent();
    if (parentTr.hasClass('detail')) {
        parentTr.removeClass('detail');
        parentTr.next().remove();
        e.find("i").removeClass('fa-minus');
        e.find("i").addClass('fa-plus');
        return;
    }
    var tableObj = parentTr.parent();
    if (tableObj.get(0).tagName != "TABLE") tableObj = tableObj.parent();
    var detailColumns = tableObj.find(".data-detail-th");
    var detailCells = parentTr.find('.data-detail-td');
    var showColumnCount = parentTr.find("td").length - detailCells.length;
    var html = '';
    html += '<tr>';
    html += '<td class="td-detail" colspan="' + showColumnCount + '">';
    if (isTable) {
        for (var i = 0; i < detailCells.length; i++) {
            //html += '<p class="p-detail">';
            html += detailCells[i].innerHTML;
            //html += '</p>';
        }
    } else {
        for (var i = 0; i < detailCells.length; i++) {
            html += '<p class="p-detail">';
            html += detailColumns[i].innerHTML + '：' + detailCells[i].innerHTML;
            html += '</p>';
        }
    }
    html += '</td>';
    html += '</tr>';
    parentTr.after(html);
    parentTr.addClass('detail');
    e.find("i").addClass('fa-minus');
    e.find("i").removeClass('fa-plus');
    window.parent.autoHeight();
}
//展开所有隐藏的列 detail
var showAllDetailTable = function (obj) {
    var tableObj = $(obj).parent().parent().parent().parent();
    if (tableObj != null && tableObj.length > 0) {
        tableObj.find("tbody tr").each(function () {
            if (!$(this).hasClass('detail')) {
                $(this).find("td:first").click();
            }
        });
    }
    $(obj).parent().html("<i class='fa fa-minus thead-th-fonticon' onclick='hideAllDetailTable(this)' title='全部隐藏'></i>");
}
//隐藏所有隐藏的列
var hideAllDetailTable = function (obj) {
    var tableObj = $(obj).parent().parent().parent().parent();
    if (tableObj != null && tableObj.length > 0) {
        tableObj.find("tbody tr").each(function () {
            if ($(this).hasClass('detail')) {
                $(this).find("td:first").click();
            }
        });
    }
    $(obj).parent().html("<i class='fa fa-plus thead-th-fonticon' onclick='showAllDetailTable(this)' title='全部展开'></i>");
}

//记录最近常用的SystemId
var setSystemIdForSort = function (systemId) {
    if (!Storage) return;
    if (!localStorage.getItem("SystemIdSort")) {
        localStorage.setItem("SystemIdSort", "");
    }
    var sortList = localStorage.getItem("SystemIdSort").split(",");
    var newSortList = [systemId];
    var len = sortList.length > 100 ? 100 : sortList.length;
    for (var i = 0; i < len; i++) {
        if (sortList[i] != systemId) {
            newSortList.push(sortList[i]);
        }
    }
    localStorage.setItem("SystemIdSort", newSortList);
}
//根据最近常用的SystemId排序系统列表
var resortSystemList = function (systemList) {
    if (!systemList || systemList == null || systemList.length == 0) return systemList;
    if (!Storage || !localStorage.getItem("SystemIdSort")) return systemList;
    var sortList = localStorage.getItem("SystemIdSort").split(",");
    if (!sortList || sortList.length == 0) return systemList;
    var newSystemList = [];
    try {
        for (var i = 0; i < sortList.length; i++) {
            for (var j = 0; j < systemList.length; j++) {
                if (sortList[i] == systemList[j].SystemId) {
                    newSystemList.push(systemList[j]);
                    systemList.splice(j, 1);
                    break;
                }
            }
        }
        newSystemList = newSystemList.concat(systemList);
    } catch (e) {
    }
    return newSystemList;
}
var ImportFile = function (uploadId, fileID, fileViewId) {
    //$("ImportBox i").attr("class", "fa fa-spinner fa-pulse ");
    $("#" + uploadId).upload("/upload?" + Math.random(), function (result) {
        //$("Import").removeAttr("disabled").val("");
        //$("ImportBox i").attr("class", "fa fa-upload");
        if (!!result.data) {
            if (!!fileID) {
                $("#" + fileID).val(result.data.file_path);
            }
            if (!!fileViewId) {
                $("#" + fileViewId).attr("src", "/" + result.data.file_path)
            }
        } else {
            $.alert(result.message);
        }
    }, 'json');
    window.setTimeout(function () { /*$("Import").attr("disabled", true);*/
    }, 1);
}

//获取url中的参数
var getUrlParam = function (name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)"); //构造一个含有目标参数的正则表达式对象
    var r = window.location.search.substr(1).match(reg);  //匹配目标参数
    if (r != null) return unescape(r[2]);
    return null; //返回参数值
}
//页面初始化时过滤权限
//有些页面按钮是异步生成的，所以也要在异步请求成功，执行成功函数后，再次过滤权限。
jQuery(document).ready(function () {
    //获取用户信息
    var test = window.location.pathname;
    if (test.toLowerCase() != "/Home/Login.html".toLowerCase()) {
        $.ajaxJson("/home/get_current_login_user", {},
            function (result) {
                console.log(result)
                if (result.status == "600") {
                    window.top.gotoLogin();
                }
                if (result && result.status == 200) {
                    //
                }
            },
            function () {
                $("#loginInfo").show().html("网络故障，请稍候重试!");
                showloginButton(false);
            }
        );
    }
    $.filterPermission();
});