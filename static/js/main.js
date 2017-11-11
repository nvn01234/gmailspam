/**
 * Created by smart on 10/11/2017.
 */

$("#submit").click(function () {
    var input_email = $("#input-email").val();
    $.post(
        "/result",         //url của view mới
        {input: input_email},
        function (response) {
            $("#result").html(response);
        }
    );
});