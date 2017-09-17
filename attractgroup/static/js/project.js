'use strict';
$('.form-group').removeClass('row');

const serverAPI = 'http://127.0.0.1:8000';

function makeAjax(url, type, data, success, error) {
    $.ajax({
      type: type,
      url: url,
      contentType : "application/json",
      dataType: 'json',
      data: JSON.stringify(data),
      success: success,
      error: error
    });
}

class Manager {
    changeInvoice(id, data) {
       makeAjax(
           `${serverAPI}/api/invoices/${id}/`,
           "PUT",
           data,
           function (response) { location.reload();},
           function (response) { console.log(response)}
       );
    }

    createInvoice(data) {
        makeAjax(
            `${serverAPI}/api/invoices/`,
            "POST",
            data,
           function (response) { location.reload();},
           function (response) { console.log(response)}
        )
    }

    showSelect(selector) {
        $(selector).css("display", "inline");
    }
}



$(document).ready(function() {
    let manager = new Manager();
    // Show select and hide "Add dish button"
    $(".show-select").click(function() {
        let id = $(this).data("id");
        let btn = $(`button.show-btn-${id}`);
        let select = $(`.dishes-slct-${id}`);
        btn.css("display", "none");
        select.css("display", "inline");
    });
    // Add dish to invoice
    $(".dish").on("change", function () {
        let invoiceId = $(this).data("id");
        let productId = $(this).val();
        if (productId === "dich") {
            return;
        }
        manager.changeInvoice(invoiceId, {'product_id': productId});
    });
    // Create invoice
    $(".crt-invoice").change(function () {
        let userId = $(this).data("id");
        let productId = $(this).val();
        if (productId === "dich") {
            return;
        }
        manager.createInvoice({"user": userId, "product": productId});

    })
    // Change invoice status
    $(".invoice-chbx").change(function () {
        let status = $(this).is(":checked");
        let invoiceId = $(this).data("id");
        manager.changeInvoice(invoiceId, {'status': status});
    })
});
