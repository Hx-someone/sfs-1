$(function () {
    let $btn = $("#btn-alloy-edit")
    $btn.click(function () {
        let sName = $("#name").val();
        if (!sName) {
            message.showError("合金名称不能为空");
            return
        }
         if (sName.length > 16) {
            message.showError("合金名称长度超长，请重新输入！");
            return
        }

        let sTackle = $("#tackle").val();
        if (sTackle.length > 256) {
            message.showError("合金攻关长度超长，请重新输入！");
            return
        }

        let sType = $("#type option:selected").val();
        if (!sType) {
            message.showError("所属类型不存在");
            return
        }
        if (sType === "0") {
            message.showError("请选择所属类型");
            return
        }
        if (!(/\d/).test(sType)) {
            message.showError("所属类型格式不正确");
            return
        }

       
        let sRemark = $("#remark").val();

        let sDataParams = {
            "number": sName,
            "type": sType,
            "tackle":sTackle ,
            "remark": sRemark,
        };
        let sAlloyId = $(this).data("alloy-id");
        $.ajax({
            url: sAlloyId ? "/alloy/edit/edit/" + sAlloyId + "/" : "/alloy/edit/add/",
            type: sAlloyId ? "PUT" : "POST",
            data: JSON.stringify(sDataParams),
            contentType: "application/json;charset=utf8",
            dataType: "json",
        })
            .done(function (res) {
                if (res.errno === "200") {
                    if (sAlloyId) {
                        message.showSuccess("合金数据更新成功");
                        setTimeout(function () {
                            window.location.href = "/alloy/"
                        }, 800)
                    } else {
                        message.showSuccess("合金添加成功");
                        setTimeout(function () {
                            window.location.href = "/alloy/"
                        }, 800)
                    }
                } else {
                    if (sAlloyId) {
                        message.showSuccess("合金数据更新失败" + res.errmsg);
                    }
                    else {
                        message.showSuccess("合金数据添加失败" + res.errmsg);
                    }
                }
            })
            .fail(function () {
                message.showError("服务器超时，请重试！")
            })

    });
});


