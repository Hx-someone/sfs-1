$(function () {
    let $userName = $("#userName");
    let $password = $("#inputUserName");
    let $login = $(".form-signin");
    
    
   function check_userName() {
       let sUserName = $userName.val();

       if(sUserName ===""){
           message.showError("用户名不能为空");
           return

       }else if(!(/\w{5,18}/).test(sUserName)){
           message.showError("用户名格式不正确，请重新输入");
           return
       };
   }

   $login.submit(function (arg) {
       arg.preventDefault();//阻止表单自动提交

       let $userAccount = $("input[name=inputUserName]").val();
       let $password = $("input[name=inputPassword]").val();
       let $remember = $("input[type=checkbox]").is(":checked");

       if ($userAccount === ""){
           message.showError("用户名不能为空");
           return
       }else if(!(/\w{5,18}/).test($userAccount)){
           message.showError("用户名格式错误");
           return
       }

       let sDataParams = {
           "user_name":$userAccount,
           "password":$password,
           "remember":$remember
       };

       $.ajax({
           url:"/user/login",
           type:"POST",
           data:JSON.stringify(sDataParams),
           contentType:"application/json;charset=utf-8",
           success:function (res) {
               if(res.errno === "0"){
                   message.showSuccess("恭喜 "+res.userName+" 登录成功");
                   setInterval(function () {
                       window.location.href="/next/index/";
                   },800);
               }else{
                   message.showError("登录失败:"+res.errmsg)
               }

           },
           error:function () {
               message.showError("服务器超时，请稍后重试！")
           }
       })

   })

    
})