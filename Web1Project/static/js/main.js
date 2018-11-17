$(document).ready(function () {
    $.uploadPreview({
        input_field: "#image-upload",   // По умолчанию: .image-upload
        preview_box: "#image-preview",  // По умолчанию: .image-preview
        label_field: "#image-label",    // По умолчанию: .image-label
        label_default: "Выберите файл",   // По умолчанию: Choose File
        label_selected: "Заменить файл",  // По умолчанию: Change File
        no_label: false,                // По умолчанию: false
        success_callback: null          // По умолчанию: null
    });
})

$('.shot img').click(function () {

})

function upload_file(method_id) {
    var $input = $("#image-upload");
    var fd = new FormData;

    fd.append('file', $input.prop('files')[0]);
    fd.append('method_id', method_id);

    showOverlay();
    $.ajax({
        type: 'POST',
        data: fd,
        processData: false,
        contentType: false,
        url: '/upload/',
        success: function (data) {
            data = JSON.parse(data);
            console.log(data[0]);
            showResult(data);
            hideOverlay();
        },
        error: function () {
            console.log('error uploading file');
            hideOverlay();
        }
    });
}

function choose_file(name, method_id) {
    var fd = new FormData;

    fd.append('name', name);
    fd.append('method_id', method_id);

    showOverlay();
    $.ajax({
        type: 'POST',
        data: fd,
        processData: false,
        contentType: false,
        url: '/choose/',
        success: function (data) {
            data = JSON.parse(data);
            console.log(data);
            showResult(data);
            var img_preview = $('#image-preview');
            img_preview.css('background-image', 'url(/static/images/' + name + ')');
            img_preview.css('background-repeat', 'no-repeat');
            img_preview.css('background-size', 'cover');
            img_preview.css('background-position', 'center center');
            hideOverlay();
        },
        error: function () {
            console.log('error choosing file');
            hideOverlay();
        }
    });
}

function showResult(data) {
    var result_block = $('#result_block');
    var result_image_block = $('#result_image_block');
    var result_description = $('#result_description');
    $('.result_value, #result_image').remove();
    var image_index = 0;
    for (var index in data) {
        if (data.hasOwnProperty(index)) {
            var fields = data[index].fields;
            if(fields.name === 'image')
            {
                result_image_block.append('<img id="result_image" src="/static/images/' + fields.value + '">');
                image_index = index;
                break;
            }
        }
    }
    for (var key in data) {
        if (data.hasOwnProperty(key) && key != image_index) {
            fields = data[key].fields;
            result_description.append('<p class="result_value">' + fields.name + ' : <strong> ' + fields.value + '</strong></p>')
        }
    }
    result_block.show();
    $('HTML, BODY').animate({scrollTop: 850}, 'slow');
}

function showOverlay() {
    $('.spinner, #gray_disable').show();
}

function hideOverlay() {
    $('.spinner, #gray_disable').hide();
}
