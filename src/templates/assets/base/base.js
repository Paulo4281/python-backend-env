const ENV = {
    "BASE_URL": "http://localhost:8080",
    "TOKEN": localStorage.getItem("token")
};

const ROUTES = {
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

function getUserId() {

    const token = localStorage.getItem("token")

    const [, payloadBase64] = token.split('.')
    const payloadDecoded = atob(payloadBase64)
    const payloadJSON = JSON.parse(payloadDecoded)
    return payloadJSON.userId

}

function createSpinner(color="text-primary", id_="button_spinner") {

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

}

function createFormModal(title, inputTypes=[], placeHolders=[], options=[], values=[], ids=[], buttonAction, buttonId) {

    const formModal = $("<div>").addClass("modal fade").attr("tabindex", "-1").attr("aria-hidden", "true")
    const modalDialog = $("<div>").addClass("modal-dialog")
    modalDialog.appendTo(formModal)

    const modalContent = $("<div>").addClass("modal-content p-2")
    
    const modalHeader = $("<div>").addClass("modal-header")
    const modalTitle = $("<div>").addClass("modal-title").append($("<h2>").text(title))
    modalTitle.appendTo(modalHeader)
    modalHeader.appendTo(modalContent)

    const form = $("<div>").addClass("form")
    const buttonDiv = $("<div>").addClass("d-flex justify-content-end")
    const button = $("<button>").addClass("btn btn-success").text(title).attr("onclick", buttonAction).attr("id", buttonId)
    button.appendTo(buttonDiv)
    form.appendTo(modalContent)
    modalContent.appendTo(modalDialog)

    inputsArray = []

    if (inputTypes.length) {
        selectIndex = 0
        for (let i = 0; i < inputTypes.length; i++) {
            if (inputTypes[i] === "select") {
                const select = $("<select>").addClass("form-select mb-2").attr("id", ids[i])
                options[selectIndex].forEach((option, index) => {
                    $("<option>").text(option).val(values[selectIndex][index]).appendTo(select)
                })
                inputsArray.push(
                    select
                )
            } else {
                inputsArray.push(
                    $("<input>").addClass("form-control mb-2").attr("id", ids[i]).attr("type", inputTypes[i]).attr("placeholder", placeHolders[i])
                )
            }
        }
    }

    for (const input of inputsArray) {
        input.appendTo(form)
    }

    buttonDiv.appendTo(form)

    return formModal

}