
$("#submit").click(function (event) {

    // Get some values from elements on the page:
    var $form = $("#submit-form"),
        term = $form.find("input[id='input-email']").val(),
        url = $form.attr("action");

    console.log($form.serialize());
    $.ajax({
        url: '/result',
        method: 'post',
        data: $form.serialize(),
        success: function (res) {
            console.log(res);
            $("#result").html(res);
        },
        error: function (e) {
            console.log(e);
        }
    });
});