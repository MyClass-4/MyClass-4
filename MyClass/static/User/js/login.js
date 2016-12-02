(function() {
	$(function() {
		$("form").submit(login);
		$("input[type='submit']").blur(removeHint);
	})

	var login = function() {
		if($("#number").val() == "" || $("#password").val() == "") {
			$("#hint").show().text("echo '用户名和密码不能为空'");
			return false;
		}
		$.ajax({
			method:"POST",
			url:"/User/login",
            data:$("form").serialize(),
			dataType:"json",
			success: function(data) {
				if(data["state"]) {
					window.location.href = data["url"];
				}
				else {
					$("#hint").show().text("echo '学号或密码错误'");
				}
			}
		});
		return false;
	}
	var removeHint = function() {
		$("#hint").hide();
	}
})();
