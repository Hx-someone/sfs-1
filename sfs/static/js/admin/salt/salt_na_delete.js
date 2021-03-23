$(function () {
    let $editBtn = $(".btn-edit");
    let $delBtn = $(".btn-del");

    $delBtn.click(function () {
        let _this = this;
        let sNewId = $(this).data("salt-na-id");

        fAlert.alertConfirm({
            title:"确定删除基盐数据吗？",
            type:"error",
            confirmButtonText:"确认删除",
            cancelButtonText:"取消删除",
            confirmCallback:function confirmCallback () {
                $.ajax({
                    url:'/salt/na/edit/'+sNewId+'/',
                    type:"DELETE",
                    dataType:"json",
                })
                    .done(function (res) {
                        if(res.errno === "200"){
                            message.showSuccess("成功删除基盐数据");
                            $(_this).parents("tr").remove();
                        }else{
                            message.showError("删除失败"+res.errmsg);
                        }
                    })
                    .fail(function () {
                        message.showError("服务器超时，请重试！")
                    })
            }
        })
    })
});