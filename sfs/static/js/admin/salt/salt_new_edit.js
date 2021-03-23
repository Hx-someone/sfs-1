$(function () {
    let $btn = $("#btn-salt-new-edit");

    let $CheckTime = $("input[name=check-time]");
    let $ThawDate = $("input[name=thaw-date]");
    const config = {

        autoclose: true,// 自动关闭

        format: 'yyyy-mm-dd',// 日期格式

        language: 'zh-CN',// 选择语言为中文

        showButtonPanel: true,// 优化样式

        todayHighlight: true, // 高亮今天

        // calendarWeeks: true,// 是否在周行的左侧显示周数

        clearBtn: true,// 清除

        startDate: new Date(1900, 10, 1),// 0 ~11  网站上线的时候

        endDate: new Date(), // 今天
    };

    $CheckTime.datepicker(config);
    $ThawDate.datepicker(config);
    $btn.click(function () {
        //检测日期
        let sCheckTime = $("#check-time").val();
        if (!sCheckTime) {
            message.showError("检测日期不存在");
            return
        }

        //炉号
        let sStoveNumber = $("#stove-number option:selected").val();
        if (!sStoveNumber) {
            message.showError("炉号不存在");
            return
        }
        if(sStoveNumber === "0"){
            message.showError("请选择炉号");
            return
        }
        if (!(/\d/).test(sStoveNumber)) {
            message.showError("炉号格式不正确");
            return
        }
        // sStoveNumber = parseInt(sStoveNumber); //将炉号的id转化为整数

        //编号
        let sNumber = $("#number").val();
        if (!sNumber) {
            message.showError("编号不存在");
            return
        }
        if (!(/\d{8}\w\d{2}\w{3}/).test(sNumber)) {
            message.showError("编号格式不正确");
            return
        }

        //碳酸根
        let sCo3 = $("#co3").val();
        // "^([+-]?)\\d*\\.\\d+$"
         if(!sCo3){
            sCo3 = 0
        }
        if ((/^\d*\\.\\d+$/).test(sCo3)) {
            message.showError("碳酸根格式不正确");
            return
        }
        //cn
        let sCn = $("#cn").val();
        if(!sCn){
            sCn = 0
        }
        if ((/^\d*\\.\\d+$/).test(sCn)) {
            message.showError("氰根格式不正确");
            return
        }

        //cno
        let sCno = $("#cno").val();
        if(!sCno){
            sCno = 0
        }
        if ((/^\d*\\.\\d+$/).test(sCno)) {
            message.showError("氰酸根格式不正确");
            return
        }



        //salt-na-id
        let sSaltNa = $("#salt-na-name option:selected").val();
        if (!sSaltNa) {
            message.showError("盐类不存在");
            return
        }
        if (sSaltNa === "0") {
            message.showError("请选择盐类");
            return
        }
        if (!(/\d/).test(sSaltNa)) {
            message.showError("盐类格式不正确");
            return
        }
        // sSaltNa = parseInt(sSaltNa);


        //batch
        let sBatch = $("#batch").val();
        if (sBatch) {
            if (!(/\w{8}/).test(sBatch)) {
                message.showError("批号格式不正确");
                return
            }
        }

        //team
        let sTeam = $("#team option:selected").val();
        if (!sTeam) {
            message.showError("班组不存在");
            return
        }

        if (sTeam == "0") {
            message.showError("请选择班组");
            return
        }
        if (!(/\d/).test(sSaltNa)) {
            message.showError("班组格式不正确");
            return
        }

        //thaw-date
        let sThawDate = $("#thaw-date").val();
        if (!sThawDate) {
            message.showError("日期不存在");
            return
        }

        //inspector
        let sInspector = $("#inspector option:selected").val();
        if (!sInspector) {
            message.showError("检测人不存在");
            return
        }

        if (sInspector == "0") {
            message.showError("请选择检测人");
            return
        }
        if (!(/\d/).test(sInspector)) {
            message.showError("检测人格式不正确");
            return
        }

        let sRemark = $("#remark").val();

        let sDataParams = {


            "check_time": sCheckTime ,
            "stove_number": parseInt(sStoveNumber),
            "number": sNumber,
            "co3": parseFloat(sCo3),
            "cn": parseFloat(sCn),
            "cno": parseFloat(sCno),
            "salt_na": parseInt(sSaltNa),
            "batch": sBatch,
            "team": parseInt(sTeam),
            "thaw_date": sThawDate,
            "inspector": parseInt(sInspector),
            "remark": sRemark,
        };

        let sNewSaltId = $(this).data("new-salt-id");
        $.ajax({
            url: sNewSaltId ? "/salt/new/edit/" + sNewSaltId + "/" : "/salt/new/add/",
            type: sNewSaltId ? "PUT" : "POST",
            data: JSON.stringify(sDataParams),
            contentType: "application/json;charset=utf8",
            dataType: "json",
        })
            .done(function (res) {
                if (res.errno === "200") {
                    if (sNewSaltId) {
                        message.showSuccess("新盐数据更新成功");
                        setTimeout(function () {
                            window.location.href = '/salt/new';

                        }, 800)

                    } else {
                        message.showSuccess("新盐数据发布成功");
                        setTimeout(function () {
                            window.location.href = '/salt/new';

                        }, 800)
                    }
                } else {
                    fAlert.alertError(res.errmsg)
                }

            })

            .fail(function () {
                message.showError("服务器超时，请重试！")
            })


    });
});
