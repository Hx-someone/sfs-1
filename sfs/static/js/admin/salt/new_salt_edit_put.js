$(function () {
    let $btn = $("#btn-edit-new-salt");

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
        let sStoveNumber = $("#stove-number").val();
        if (!sStoveNumber) {
            message.showError("炉号不存在");
            return
        } else if (!(/\d/).test(sStoveNumber)) {
            message.showError("炉号格式不正确");
            return
        }


        //编号
        let sNumber = $("#number").val();
        if (!sNumber) {
            message.showError("编号不存在");
            return
        } else if (!(/\d{8}\w\d{2}\w{3}/).test(sNumber)) {
            message.showError("编号格式不正确");
            return
        }

        //碳酸根
        let sCo3 = $("#co3").val();
        // "^([+-]?)\\d*\\.\\d+$"
        if ((/^\d*\\.\\d+$/).test(sCo3)) {
            message.showError("碳酸根格式不正确");
            return
        }
        //cn
        let sCn = $("#cn").val();
        if ((/^\d*\\.\\d+$/).test(sCn)) {
            message.showError("氰根格式不正确");
            return
        }

        //cno
        let sCno = $("#cno").val();
        if ((/^\d*\\.\\d+$/).test(sCno)) {
            message.showError("氰酸根格式不正确");
            return
        }

        //salt-na-id
        let sSaltNa = $("#salt-na-name").val();
        if (!sSaltNa) {
            message.showError("盐类不存在");
            return
        } else if (![1, 2, 3, 4, 5, 6, 7].includes(parseInt(sSaltNa))) {
            message.showError("盐类不存在");
            return
        }

        //batch
        let sBatch = $("#batch").val();
        if (sBatch) {
            if (!(/\w{8}/).test(sBatch)) {
                message.showError("批号格式不正确");
                return
            }
        }

        //team
        let sTeam = $("#team").val();
        if (!sTeam) {
            message.showError("班组不存在");
            return
        }
        else if (!["X", "L"].includes(sTeam)) {
            message.showError("班组不存在");
            return
        }
        //thaw-date
        let sThawDate = $("#thaw-date").val();
        if (!sThawDate) {
            message.showError("日期不存在");
            return
        }

        //inspector
        let sInspector = $("#inspector").val();
        if (!sInspector) {
            message.showError("检测人不存在");
            return
        }
        else if (!["H", "T"].includes(sInspector)) {
            message.showError("检测人不存在");
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
            "team": sTeam,
            "thaw_date": sThawDate,
            "inspector": sInspector,
            "remark": sRemark,
        };

        let sNewSaltId = $(this).data("new-salt-id");
        $.ajax({
            url: sNewSaltId ? "/salt/new/edit/" + sNewSaltId + "/" : "/salt/new/pub/",
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
                            window.location.reload()

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
