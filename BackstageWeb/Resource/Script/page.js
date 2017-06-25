
//初始化分页按钮
jQuery.InitPagin = function (pageindex, pagesize, totalcount) {

    //初始化值
    var _currentpage = pageindex; //当前页码
    if (_currentpage == undefined || _currentpage <= 0) {
        _currentpage = 1;
    }

    var _pagesize = pagesize; //每页显示数
    if (_pagesize == undefined || _pagesize <= 0) {
        _pagesize = 10;
    }

    var _totalcount = totalcount; //总记录数
    if (_totalcount == undefined || _totalcount < 0) {
        _totalcount = 0;
    }

    var _showpage = 9; //默认显示页码数
    var _totalpage = Math.ceil(_totalcount / _pagesize); //总的页码数
    if (_totalpage <= 0) {
        _totalpage = 1;
    }
    if (_currentpage > _totalpage) {
        _currentpage = _totalpage;
    }

    //当前页码区间内的最大页码和最小页码。
    //页码区间是指以默认显示页码数做为一个显示区间，例如：1-9,10-18,19-27...
    var _maxpage = _showpage * Math.ceil(_currentpage / _showpage); 
    if (_maxpage > _totalpage) {
        _maxpage = _totalpage;
    }
    var _minpage = _maxpage - _showpage + 1; ; 
    if (_minpage < 1) {
        _minpage = 1;
    }

    var _html = "<ul class='pagin text-right'>";

    //是否首页
    if (_currentpage == 1) {
        _html += "<li><a href='javascript:void(0)' ondragstart='return false'>上一页</a></li>";
    } else {
        _html += "<li><a href='javascript:void(0)' ondragstart='return false' onclick='indexPage(" + (_currentpage - 1) + ")'>上一页</a></li>";
    }

    //第一页和左边更多(...)的页码
    if (_maxpage > _showpage) {
        _html += "<li><a href='javascript:void(0)' ondragstart='return false' onclick='indexPage(1)'>1</a></li>";
        _html += "<li><a href='javascript:void(0)' ondragstart='return false' class='more' onclick='indexPage(" + (_minpage - 1) + ")'>...</a></li>";
    }

    //生成默认显示的页码数
    for (var i = _minpage; i <= _maxpage; i++) {
        if (i == _currentpage) {
            _html += "<li><a href='javascript:void(0)' ondragstart='return false' class='blue'>" + _currentpage + "</a></li>"; //当前页码
        } else {
            _html += "<li><a href='javascript:void(0)' ondragstart='return false' onclick='indexPage(" + i + ")'>" + i + "</a></li>";
        }
    }

    //最后一页和右边更多(...)的页码
    if (_maxpage < _totalpage) {
        _html += "<li><a href='javascript:void(0)' ondragstart='return false' class='more' onclick='indexPage(" + (_maxpage + 1) + ")'>...</a></li>";
        _html += "<li><a href='javascript:void(0)' ondragstart='return false' onclick='indexPage(" + _totalpage + ")'>" + _totalpage + "</a></li>";
    }

    //是否尾页
    if (_currentpage == _totalpage) {
        _html += "<li><a href='javascript:void(0)' ondragstart='return false'>下一页</a></li>";
    } else {
        _html += "<li><a href='javascript:void(0)' ondragstart='return false' onclick='indexPage(" + (_currentpage + 1) + ")'>下一页</a></li>";
    }
    _html += "</ul>";

    return _html;
}