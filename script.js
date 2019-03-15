

$(document).ready(function () {
    $(document).on('click', '#StartGame', function () {
        $(".TheGallows").css("visibility", "visible");
        $("#CharIn").css("visibility", "visible");
        $("#StartGame").css("visibility", "hidden");
        $("input").keypress(function(){
            var input = this.value;
            if(input != ""){

            }
        });
    });
});


