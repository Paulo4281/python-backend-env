const ENV = {
    "BASE_URL": "http://localhost:8080"
}

function loader(color="text-primary", remove=false) {

    if (remove) {
        console.log("NEED TO REMOVE THE SPINNER.")
    } else {
        const loader = $("<div>").addClass(`spinner-border spinner-border-sm ${color}`)
        
        return loader;
    }

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

    modal.modal("show");

};