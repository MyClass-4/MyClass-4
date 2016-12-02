
var rotate = {
    deg: 0,
}

$(function() {
    $('#rotate_content').click(function(){
        rotate.deg -= 40;
        $(this).css("transform","rotateY("+rotate.deg+"deg)")
    });

});
