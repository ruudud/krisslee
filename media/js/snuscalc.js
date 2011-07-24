$(function() {
    $("#snusvssmoke").slider({
        value: 50,
        min: 0,
        max: 100,
        slide: function(event, ui){
                $('#distribution').val(ui.value);
                $('#current').html(ui.value + '% snus, ' + (100 - ui.value) + '% røyk');
            }
    });
    var start_value = $("#snusvssmoke").slider("value");
    $('#distribution').val(start_value);
    $('#current').html(start_value + '% snus, ' + (100 - start_value) + '% røyk');
});
