const ENV = {
    "BASE_URL": "http://localhost:8080"
};

ROUTES = {
    "USER": {
        "USER": `${ENV.BASE_URL}/user`,
        "AUTH": `${ENV.BASE_URL}/user/auth`
    },
    "BOOK": {
        "BOOK": `${ENV.BASE_URL}/book`,
        "CATEGORY": `${ENV.BASE_URL}/book/category`,
        "AUTHOR": `${ENV.BASE_URL}/book/author`
    },
    "VIEWS": {
        "DASH": `${ENV.BASE_URL}/dash`
    }
};

function createSpinner(color="text-primary", id_="login_button_spinner") {

    const loader = $("<div>").addClass(`spinner-border spinner-border-sm ${color}`).attr("id", id_)
        
    return loader;

}

function createModal(message) {

    const modal = $("<div>").addClass("modal fade")
    const modalDialog = $("<div>").addClass("modal-dialog modal-md")
    modalDialog.appendTo(modal)

    const modalContent = $("<div>").addClass("modal-content");

    const modalBody = $("<div>").addClass("modal-body text-center fs-5");
    $("<span>").html(message).appendTo(modalBody);
    modalBody.appendTo(modalContent);

    const modalFooter = $("<div>").addClass("modal-footer");
    $("<button>").addClass("btn btn-primary").attr("data-bs-dismiss", "modal").text("Close").appendTo(modalFooter);
    modalFooter.appendTo(modalContent);

    modalContent.appendTo(modalDialog);

    return modal;

};