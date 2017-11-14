/**
 * Created by smart on 10/11/2017.
 */

// function submit() {
//     var input_email = $("#input-email").val();
//     $.post(
//         "",         //name of request
//         {input: input_email},
//         function (response) {
//             $("#result").html(response);
//         }
//     );
//     $("#result").html("spam");
// }
// $.ajax({
//   type: "POST",
//   url: url,  // url server của thắng
//   data: data,  // data input
//   success: success,  //  hàm callback khi success
//   dataType: dataType  // type data trả về
// });

$("#submit").click(function (event) {
    // Stop form from submitting normally
    // event.preventDefault();

    // Get some values from elements on the page:
    var $form = $("#submit-form"),
        term = $form.find("input[id='input-email']").val(),
        url = $form.attr("action");

    //send data using post
    // var posting = $.post(url, {input: term});
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

    //Put result in a div
    // posting.done(function (data) {
    //    var content = $(data).find("#content");
    //     $("#result").empty().append(content);
    // });
});