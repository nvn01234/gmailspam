// function get data from server through request

$("#submit").click(function (event) {

    var $form = $("#submit-form");

    $("#result").html("Đang chờ xử lý ... ");
    $.ajax({
        url: '/result',
        method: 'post',
        data: $form.serialize(),    //send input data
        success: function (res) {
            $("#result").html("KẾT QUẢ: " + res);
        },
        error: function (e) {
            console.log(e);
        }
    });
});