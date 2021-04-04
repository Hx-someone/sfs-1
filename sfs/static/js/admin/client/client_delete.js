$(function () {
    let $delBtn = $(".btn-del");

    $delBtn.click(function () {
        let _this = this;
        let sClient = $(this).data("client-id");

        fAlert.alertConfirm({
            title:"确定客户数据吗？",
            type:"error",
            confirmButtonText:"确认删除",
            cancelButtonText:"取消删除",
            confirmCallback:function confirmCallback () {
                $.ajax({
                    url:'/client/edit/'+sClient+'/',
                    type:"DELETE",
                    dataType:"json",
                })
                    .done(function (res) {
                        if(res.errno === "200"){
                            message.showSuccess("成功删除客户数据");
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