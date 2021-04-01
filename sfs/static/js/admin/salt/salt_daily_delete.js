$(function () {
 let $editBtn = $(".btn-edit");
 let $delBtn = $(".btn-del");

 $delBtn.click(function () {
     let _this = this;

     let sDailyId = $(this).data("salt-daily-id");

     fAlert.alertConfirm({
         title:"确定删除该条炉盐数据吗？",
         type:"error",
         confirmButtonText:"确认删除",
         cancelButtonText:"取消删除",
         confirmCallback:function confirmCallback () {
             $.ajax({
                 url:'/salt/daily/edit/'+sDailyId +'/',
                 type:"DELETE",
                 dataType:"json"
             })
                 .done(function (res) {
                     if(res.errno === "200"){
                      message.showSuccess("成功删除炉盐数据");
                         $(_this).parents("tr").remove()
                     }else{
                      message.showError("删除失败:"+res.errmsg);
                     }
                 })
                 .fail(function () {
                     message.showError("服务器超时，请重试")
                 })
         }
     })
 })
});