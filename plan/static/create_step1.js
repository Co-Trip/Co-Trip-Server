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

(function ($) {
    function updateCityPickerList(provinceID) {
        debugger;
        var $cityPickerBody = $('#city-picker-body');
        $cityPickerBody.empty();
        $.getJSON('/api/v1/province/' + provinceID,
            {format: 'json'},
            function (json, textStatus) {
                var cityList = json['city'];
                for (var cityID in cityList) {
                    var $pickerItem = $('<div class="col-sm-3 CT-picker-item city-item"></div>');
                    var $pickerItemBody = $('<div class="thumbnail CT-picker-item-body"><div class="CT-item-check-icon"><span class="glyphicon glyphicon-ok-circle"></span></div></div>');
                    var $pickerItemImg = $('<img src="" alt="..." class="img-rounded CT-picker-item-img">');
                    var $pickerItemDetail = $('<div class="caption CT-picker-item-detail"></div>');

                    $pickerItemDetail.append('<h6>' + cityList[cityID] + '</h6><input name="destination_city" type="checkbox" class="CT-item-checkbox" form="plan-form" value="' + cityID + '">');
                    $pickerItemBody.append($pickerItemImg);
                    $pickerItemBody.append($pickerItemDetail);
                    $pickerItem.append($pickerItemBody);
                    $pickerItem.hide();
                    $pickerItem.click(function (event) {
                        $(this).toggleClass('item-selected');
                        $(this).find('.CT-item-checkbox').attr('checked', true);
                    });

                    $cityPickerBody.append($pickerItem);
                    $pickerItem.fadeIn();
                }
            }
        );
    }
    $(document).ready(function() {
        $('.CT-picker-item.friend-item').click(function (event) {
            debugger;
            $(this).toggleClass('item-selected');
            $(this).find('.CT-item-checkbox').attr('checked', true);
        });
        $('.CT-picker-item.city-item').click(function (event) {
            $(this).toggleClass('item-selected');
            $(this).find('.CT-item-checkbox').attr('checked', true);
        });

        updateCityPickerList(1);

        $('#id-destination-city').change(function (event) {
            var provinceID = $(this).val();
            updateCityPickerList(provinceID);
        });
    });
})(jQuery)