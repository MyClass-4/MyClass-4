$(function() {
	$('input[type=submit]').click(changeSrcOfResult)
});

var changeSrcOfResult = function(event) {
	// alert('kkk')
	$('iframe').attr('src', '/CodeLib/coding');
}