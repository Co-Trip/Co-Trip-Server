/**
 * 
 * @authors Tom Hu (h1994st@gmail.com)
 * @date    2014-02-28 21:22:06
 * @version 1.0
 */

/**
 * Date Format Ex
 * --------------------------------------------------
 */
Date.prototype.format = function(format) //author: meizz 
{ 
    var o = { 
        "M+" : this.getMonth()+1, //month 
        "d+" : this.getDate(),    //day 
        "h+" : this.getHours(),   //hour 
        "m+" : this.getMinutes(), //minute 
        "s+" : this.getSeconds(), //second 
        "q+" : Math.floor((this.getMonth()+3)/3),  //quarter 
        "S" : this.getMilliseconds() //millisecond 
    } 
    if(/(y+)/.test(format)) format=format.replace(RegExp.$1, (this.getFullYear()+"").substr(4 - RegExp.$1.length)); 
    for(var k in o) if(new RegExp("("+ k +")").test(format)) format = format.replace(RegExp.$1, RegExp.$1.length==1 ? o[k] : ("00"+ o[k]).substr((""+ o[k]).length)); 
    return format; 
}

/**
 * Datetimepicker init
 * --------------------------------------------------
 */
$('.form_date').datetimepicker({
    language:  'zh-CN',
    weekStart: 1,
    todayBtn:  1,
    autoclose: 1,
    todayHighlight: 1,
    startView: 2,
    minView: 2,
    forceParse: 0,
    startDate: new Date().format('yyyy-MM-dd')
});

$(document).ready(function() {
    $('.CT-picker-item.friend-item').click(function(event) {
        $(this).toggleClass('item-selected');
        $(this).find('.CT-item-checkbox').attr('checked', true);
    });
});