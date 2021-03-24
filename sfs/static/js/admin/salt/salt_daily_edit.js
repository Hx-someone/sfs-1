$(function () {
    let $btn = $("#btn-salt-daily-edit")
    let $CheckTime = $("input[name=check-time]");
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

    $btn.click(function () {
        let sCheckTime = $("#check-time").val();
        if (!sCheckTime) {
            message.showError("检测日期不能为空");
            return
        }

        let sNumber = $("#number").val();
        if (!sNumber) {
            message.showError("检测编码不能为空，请重新输入！");
            return
        }
        if (!(/\d{8}\w\d{2}\w{3}/).test(sNumber)) {
            message.showError("检测编码格式不正确，请重新输入！");
            return
        }

        let sStoveNumber = $("#stove-number option:selected").val();
        if (!sStoveNumber) {
            message.showError("炉号不存在");
            return
        }
        if (sStoveNumber === "0") {
            message.showError("请选择炉号");
            return
        }
        if (!(/\d/).test(sStoveNumber)) {
            message.showError("炉号格式不正确");
            return
        }

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

        //碳酸根
        let sCo3 = $("#co3").val();
        // "^([+-]?)\\d*\\.\\d+$"
        if (!sCo3) {
            sCo3 = 0
        }
        if ((/^\d*\\.\\d+$/).test(sCo3)) {
            message.showError("碳酸根格式不正确");
            return
        }

        //cn
        let sCn = $("#cn").val();
        if (!sCn) {
            sCn = 0
        }
        if ((/^\d*\\.\\d+$/).test(sCn)) {
            message.showError("氰根格式不正确");
            return
        }

        let sCno = $("#cno").val();
        if (!sCno) {
            sCno = 0
        }
        if ((/^\d*\\.\\d+$/).test(sCno)) {
            message.showError("氰酸根格式不正确");
            return
        }

        let sStatus = $("#status option:selected").val();
        if (!sStatus) {
            message.showError("状态不存在");
            return
        }
        if (sStatus === "0") {
            message.showError("请选择状态");
            return
        }
        if (!(/\d/).test(sStatus)) {
            message.showError("状态格式不正确");
            return
        }

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
            "check_time": sCheckTime,
            "number": sNumber,
            "stove_number": sStoveNumber,
            "salt_na": sSaltNa,
            "cn": sCn,
            "co3": sCo3,
            "cno": sCno,
            "status": sStatus,
            "inspector": sInspector,
            "remark": sRemark,
        };
        let sSaltDailyId = $(this).data("salt-daily-id");
        $.ajax({
            url: sSaltDailyId ? "/salt/daily/edit/" + sSaltDailyId + "/" : "/salt/daily/add/",
            type: sSaltDailyId ? "PUT" : "POST",
            data: JSON.stringify(sDataParams),
            contentType: "application/json;charset=utf8",
            dataType: "json",
        })
            .done(function (res) {
                if (res.errno === "200") {
                    if (sSaltDailyId) {
                        message.showSuccess("炉盐数据更新成功");
                        setTimeout(function () {
                            window.location.href = "/salt/daily/"
                        }, 800)
                    } else {
                        message.showSuccess("炉盐数据添加成功");
                        setTimeout(function () {
                            window.location.href = "/salt/daily/"
                        }, 800)
                    }
                } else {
                    if (sSaltDailyId) {
                        message.showSuccess("炉盐数据更新失败" + res.errmsg);
                    }
                    else {
                        message.showSuccess("炉盐数据添加失败" + res.errmsg);
                    }
                }
            })
            .fail(function () {
                message.showError("服务器超时，请重试！")
            })

    });
});


