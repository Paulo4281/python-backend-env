async function addBook() {
    const data = await router("GET", ROUTES["BOOK"]["CATEGORY"])
    const categories = data.map((element) => { return element.name })
    const categoryIds = data.map((element) => { return element.id_ })
            createFormModal(
                "Add Book",
                ["text", "number", "select"],
                ["Title. Eg: The Lord of the Rings", "Price. Eg: 45.90"],
                [categories],
                [categoryIds],
                ["title", "price", "category_id"],
                "addBookFinish(this)",
                "addBook_btn"
                ).modal("show");
    
            }
async function addBookFinish(button) {
    const formData = $(button).parent().parent().find("input, select")
    const data = {}

    formData.each(function() {
        const id_ = $(this).attr("id")
        let value
        if (id_ === "price") {
            value = Number($(this).val())
        } else {
            value = $(this).val()
        }
        data[id_] = value
    })

    data["owner_id"] = getUserId()
    $("#addBook_btn").append(createSpinner("text-light"))
        await router("POST", ROUTES["BOOK"]["BOOK"], data).then((response) => {
            console.log(response.data)
            $("#button_spinner").remove()
        }).catch((error) => {
            $("#button_spinner").remove()
            if (error.response.data) {
                createModal(`Ops. <strong>${error.response.data.message}</strong>`).modal("show")
            } else {
                createModal(`Something went wrong.`).modal("show")
            }
        })
}