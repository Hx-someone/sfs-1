$(function () {
    let $btn = $("#btn-edit-salt-na");


    $btn.click(function () {
        let sName = $("input[name=name]").val();
        let sType = $("input[name=type]").val();
        let sNewSalThawCraft = $("input[name=new_salt_thaw_craft]").val();
        let sUsingSaltThawCraft = $("input[name=using_salt_thaw_craft]").val();
        let sApplyAlloy = $("input[name=apply_alloy]").val();
        let sTrait = $("input[name=trait]").val();
        let sRemark = $("input[name=remark]").val();

        // name
        if (!sName) {
            message.showError("基盐名字不能为空");
            return
        }
        if (sName.length > 16) {
            message.showError("基盐名字长度太长");
            return
        }

        //type
        if (!sType) {
            message.showError("基盐类型不能为空");
            return
        }
        if (sType.length > 16) {
            message.showError("基盐类型长度太长");
            return
        }

        //new_salt_thaw_craft
        if (!sNewSalThawCraft) {
            message.showError("基盐化盐工艺不能为空");
            return
        }
        if (sNewSalThawCraft.length > 128) {
            message.showError("基盐化盐工艺长度太长");
            return
        }

        //using_salt_thaw_craft
        if (!sUsingSaltThawCraft) {
            message.showError("基盐使用工艺不能为空");
            return
        }
        if (sUsingSaltThawCraft.length > 64) {
            message.showError("基盐使用工艺长度太长");
            return
        }

        //apply_alloy
        if (!sApplyAlloy) {
            message.showError("基盐实用合金不能为空");
            return
        }
        if (sApplyAlloy.length > 64) {
            message.showError("基盐实用合金长度太长");
            return
        }

        //trait
        if (!sTrait) {
            message.showError("基盐特性不能为空");
            return
        }
        if (sTrait.length > 128) {
            message.showError("基盐特性长度太长");
            return
        }

        //remark
        if (sRemark.length > 256) {
            message.showError("备注长度太长");
            return
        }


        let sDataParams = {
            "name": sName,
            "type": sType,
            "new_salt_thaw_craft": sNewSalThawCraft,
            "using_salt_thaw_craft": sUsingSaltThawCraft,
            "apply_alloy": sApplyAlloy,
            "trait": sTrait,
            "remark": sRemark,
        };
        let sSaltNaId = $(this).data("salt-na-id");

        $.ajax({
            url: sSaltNaId ? "/salt/na/edit/" + sSaltNaId + "/" : "/salt/na/add/",
            type: sSaltNaId ? "PUT" : "POST",
            data: JSON.stringify(sDataParams),
            contentType: "application/json;charset=utf8",
            dataType: "json",
        })
            .done(function (res) {
                if (res.errno === "200") {
                    if (sSaltNaId) {
                        message.showSuccess(sName + "基盐数据更新成功!");
                        setTimeout(function () {
                            window.location.href = "/salt/na/";
                        }, 800)
                    } else {
                        message.showSuccess(sName + "基盐数据发布成功!");
                        setTimeout(function () {
                            window.location.href = "/salt/na/";
                        }, 800)
                    }
                }else{
                    fAlert.alertError(res.errmsg);
                }

            })
            .fail(function () {
                message.showError("服务器超时，请重试！")
            })
    })
});