$(function() {
	$("form").submit(hand_in);
	$("input[type='submit']").blur(hindHint);
});

var hand_in = function(event) {
	if (! /^.+?\\[0-9]{8}\_.+?\.\w+$/.test($('#homework-file').val())) {
		$("#hint").show().text('请输入正确格式：学号_姓名.后缀');
		return　false;
	}
	return true;
	// 下面代码有问题
	var formdata = new FormData();
	$.ajax({
		method:"POST",
		url:"/Homework/hand_in",
        data: $("form").serialize(),
		dataType:"json",
		// processData: false,
		// contentType: false,
		success: function(data) {
			if(data["state"]) {
				$("#hint").show().text(data['message']);
			}
			else {
				$("#hint").show().text("文件上传失败");
			}
		}
	});
	return false;
}

var hindHint = function(event) {
	$("#hint").hide();
}

