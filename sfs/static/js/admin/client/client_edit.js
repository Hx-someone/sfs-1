$(function () {
    let $btn = $("#btn-client-edit")
    $btn.click(function () {
        let sName = $("#name").val();
        if (!sName) {
            message.showError("客户名称不能为空");
            return
        }

        let sNumber = $("#number").val();
        if (!sNumber) {
            message.showError("客户编号，请重新输入！");
            return
        }
        if (sNumber.length > 8) {
            message.showError("客户编号长度超长，请重新输入！");
            return
        }

        let sBelong = $("#belong option:selected").val();
        if (!sBelong) {
            message.showError("所属销售不存在");
            return
        }
        if (sBelong === "0") {
            message.showError("请选择所属销售");
            return
        }
        if (!(/\d/).test(sBelong)) {
            message.showError("所属销售格式不正确");
            return
        }

        let sIndustry= $("#industry option:selected").val();
        if (!sIndustry) {
            message.showError("客户性质不存在");
            return
        }
        if (sIndustry === "0") {
            message.showError("请选择客户性质");
            return
        }
        if (!(/\d/).test(sIndustry)) {
            message.showError("客户性质格式不正确");
            return
        }
        let sMark= $("#mark option:selected").val();
        if (!sMark) {
            message.showError("客户等级不存在");
            return
        }
        if (sMark === "0") {
            message.showError("请选择客户等级");
            return
        }
        if (!(/\d/).test(sMark)) {
            message.showError("客户等级格式不正确");
            return
        }

        let sProductType= $("#product_type option:selected").val();
        if (!sMark) {
            message.showError("客户产品类型不存在");
            return
        }
        if (sProductType === "0") {
            message.showError("请选择客户产品类型");
            return
        }
        if (!(/\d/).test(sProductType)) {
            message.showError("客户产品类型格式不正确");
            return
        }

        let sType= $("#type option:selected").val();
        if (!sType) {
            message.showError("客户类型不存在");
            return
        }
        if (sType === "0") {
            message.showError("请选择客户类型");
            return
        }
        if (!(/\d/).test(sType)) {
            message.showError("客户类型格式不正确");
            return
        }

        //碳酸根
        let sAbbr= $("#abbr").val();
        // "^([+-]?)\\d*\\.\\d+$"

        if (sAbbr.length > 64) {
            message.showError("客户简介太长，请重新输入");
            return
        }

        //cn
        let sAddress = $("#address").val();
        if (sAddress.length > 256) {
            message.showError("客户地址太长，请重新输入");
            return
        }

        let sRemark = $("#remark").val();

        let sDataParams = {
            "number": sName,
            "name": sNumber,
            "abbr":sAbbr ,
            "address": sAddress,
            "belong": sBelong,
            "industry": sIndustry,
            "product_type": sProductType,
            "mark": sMark,
            "type": sType,
            "remark": sRemark,
        };
        let sClientId = $(this).data("client-id");
        $.ajax({
            url: sClientId ? "/client/edit/edit/" + sClientId + "/" : "/client/edit/add/",
            type: sClientId ? "PUT" : "POST",
            data: JSON.stringify(sDataParams),
            contentType: "application/json;charset=utf8",
            dataType: "json",
        })
            .done(function (res) {
                if (res.errno === "200") {
                    if (sClientId) {
                        message.showSuccess("客户数据更新成功");
                        setTimeout(function () {
                            window.location.href = "/client/index/"
                        }, 800)
                    } else {
                        message.showSuccess("客户添加成功");
                        setTimeout(function () {
                            window.location.href = "/client/index/"
                        }, 800)
                    }
                } else {
                    if (sClientId) {
                        message.showSuccess("客户数据更新失败" + res.errmsg);
                    }
                    else {
                        message.showSuccess("客户数据添加失败" + res.errmsg);
                    }
                }
            })
            .fail(function () {
                message.showError("服务器超时，请重试！")
            })

    });
});


