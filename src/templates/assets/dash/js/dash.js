// Book
async function addBook() {

    const categoriesData = await router("GET", ROUTES["BOOK"]["CATEGORY"])
    const categories = categoriesData.map((element) => { return element.name })
    const categoryIds = categoriesData.map((element) => { return element.id_ })

    const authorsData = await router("GET", ROUTES["BOOK"]["AUTHOR"])
    const authors = authorsData.map((element) => { return element.name })
    const authorsIds = authorsData.map((element) => { return element.id_ })

            createFormModal(
                "Add Book",
                ["text", "number", "select", "select"],
                ["Title. Eg: The Lord of the Rings", "Price. Eg: 45.90"],
                [categories, authors],
                [categoryIds, authorsIds],
                ["title", "price", "category_id", "author_id"],
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
            createModal(`Book successfully added!`).modal("show")
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
// End Book

// Author

function addAuthor() {

    createFormModal(
        "Add Author",
        ["text", "date", "date", "text"],
        ["Name", "", "", "Nationality"],
        [],
        [],
        ["name", "birth", "death", "nationality"],
        "addAuthorFinish(this)",
        "addAuthor_btn"
    ).modal("show")

}

async function addAuthorFinish(button) {

    const formData = $(button).parent().parent().find("input, select")
    const data = {}

    formData.each(function() {
        const id_ = $(this).attr("id")
        const value = $(this).val()
        data[id_] = value
    })

    $("#addAuthor_btn").append(createSpinner("text-light"))
    await router("POST", ROUTES["BOOK"]["AUTHOR"], data)
    .then((response) => {
        createModal(`Author Successfully added!`).modal("show")
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

// End Author