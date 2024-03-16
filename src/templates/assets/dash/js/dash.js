$(document).ready(async () => {

    // Load Books
    const books = await router("GET", ROUTES["BOOK"]["BOOK"])

    console.log(books)

    const books_tbody = $("#books_tbody")

    books.forEach((book) => {
        const tr = $("<tr>").addClass("text-center").appendTo(books_tbody)
        $("<td>").text(book.title).appendTo(tr)
        $("<td>").text(book.price).appendTo(tr)
    })

})

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

    data["user_id"] = getUserId()
    $(button).append(createSpinner("text-light"))
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

    $(button).append(createSpinner("text-light"))
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

// Category

function addCategory() {

    createFormModal(
        "Add Category",
        ["text"],
        ["Category"],
        [],
        [],
        ["name"],
        "addCategoryFinish(this)",
        "addCategory_btn"
    ).modal("show")

}

async function addCategoryFinish(button) {
    
    const formData = $(button).parent().parent().find("input")
    const data = {}

    formData.each(function() {
        const id_ = $(this).attr("id")
        const value = $(this).val()
        data[id_] = value
    })

    $(button).append(createSpinner("text-light"))
    await router("POST", ROUTES["BOOK"]["CATEGORY"], data)
    .then((response) => {
        createModal("Category Successfully added!").modal("show")
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

// End Category

// Review

async function addReview() {

    const booksData = await router("GET", ROUTES["BOOK"]["BOOK"])
    const books = booksData.map((element) => { return element.title })
    const booksIds = booksData.map((element) => { return element.id_ })

    createFormModal(
        "Add Review",
        ["number", "text", "select"],
        ["Rate", "Review Text"],
        [books],
        [booksIds],
        ["rate", "review", "book_id"],
        "addReviewFinish(this)",
        "addReview_btn"
    ).modal("show")

}

async function addReviewFinish(button) {

    const formData = $(button).parent().parent().find("input, select")
    const data = {}

    formData.each(function() {
        const id_ = $(this).attr("id")
        let value
        if (id_ === "rate") {
            value = Number($(this).val())
        } else {
            value = $(this).val()
        }
        data[id_] = value
    })

    data["user_id"] = getUserId()
    $(button).append(createSpinner("text-light"))
    await router("POST", ROUTES["BOOK"]["REVIEW"], data)
    .then((response) => {
        createModal("Review successfully added!").modal("show")
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

// End Review

// User

function addUser() {

    createFormModal(
        "Add User",
        ["text", "text", "password", "date"],
        ["Name", "E-mail", "Password"],
        [],
        [],
        ["name", "mail", "password", "birth"],
        "addUserFinish(this)",
        "addUser_btn"
    ).modal("show")

}

async function addUserFinish(button) {

    const formData = $(button).parent().parent().find("input, select")
    const data = {}

    formData.each(function() {
        const id_ = $(this).attr("id")
        const value = $(this).val()
        data[id_] = value
    })
    
    $(button).append(createSpinner("text-light"))
    await router("POST", ROUTES["USER"]["USER"], data)
    .then((response) => {
        createModal("User successfully added!").modal("show")
        $("#button_spinner").remove()
    }).catch((error) => {
        $("#button_spinner").remove()
        if (error.response.data) {
            createModal(`Ops. <strong>${error.respones.data.message}</strong>`).modal("show")
        } else {
            createModal("Something went wrong.").modal("show")
        }
    })
}

// End User