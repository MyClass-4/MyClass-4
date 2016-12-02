(function() {
	$(function() {
		$("form").submit(login);
		$("input[type='submit']").blur(removeHint);
	})

	var login = function() {
		if($("#number").html() == "" || $("#password").html() == "") {
			$("#password").after("<p id='hint'>用户名和密码不能为空</p>");
			return false;
		}
		$.ajax({
			method:"POST",
			url:"/login",
			dataType:"json",
			success: function(json) {
				if(json["state"]) {
					window.location.href = json["url"];
				}
				else {
					$("#password").after("<p id='hint'>学号或密码错误</p>");
				}
			}
		});

		return false;
	}

	var removeHint = function() {
		$("#hint").remove();
	}
})();