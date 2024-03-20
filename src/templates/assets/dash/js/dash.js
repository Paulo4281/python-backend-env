$(document).ready(async () => {

    // Load Books

    const books = await router("GET", ROUTES["BOOK"]["BOOK"])
    
    if (books) {
        const books_tbody = $("#books_tbody")
        books.forEach((book) => {
            const tr = $("<tr>").addClass("text-center").appendTo(books_tbody)
            $("<td>").text(book.title).appendTo(tr)
            $("<td>").text(`${parseFloat(book.price)}$`).appendTo(tr)
            $("<td>").text("").appendTo(tr)
            $("<td>").text(book.category.name).appendTo(tr)
            $("<td>").text(book.user.name).appendTo(tr)
            $("<td>").text(book.author.name).appendTo(tr)
            $("<td>").text(new Date(book.created_at).toLocaleDateString()).appendTo(tr)
        })
    }

    // Load Authors

    const authors = await router("GET", ROUTES["BOOK"]["AUTHOR"])

    if (authors) {
        const authors_tbody = $("#authors_tbody")
        authors.forEach((author) => {
            const tr = $("<tr>").addClass("text-center").appendTo(authors_tbody)
            $("<td>").text(author.name).appendTo(tr)
            $("<td>").text(new Date(author.birth).toLocaleDateString()).appendTo(tr)
            $("<td>").text(new Date(author.death).toLocaleDateString()).appendTo(tr)
            $("<td>").text(author.nationality).appendTo(tr)
            $("<td>").text(new Date(author.created_at).toLocaleDateString()).appendTo(tr)
        })
    }

    // Load Categories

    const categories = await router("GET", ROUTES["BOOK"]["CATEGORY"])
    
    if (categories) {
        const category_tbody = $("#category_tbody")
        categories.forEach((category) => {
            const tr = $("<tr>").addClass("text-center").appendTo(category_tbody)
            $("<td>").text(category.name).appendTo(tr)
            $("<td>").text(new Date(category.created_at).toLocaleDateString()).appendTo(tr)
        })
    }


    // Load Reviews

    const reviews = await router("GET", ROUTES["BOOK"]["REVIEW"])

    if (reviews) {
        const reviews_tbody = $("#reviews_tbody")
        reviews.forEach((review) => {
            const tr = $("<tr>").addClass("text-center").appendTo(reviews_tbody)
            $("<td>").text(review.rate).appendTo(tr)
            $("<td>").text(review.review).appendTo(tr)
            $("<td>").text(review.user.name).appendTo(tr)
            $("<td>").text(review.book.title).appendTo(tr)
            $("<td>").text(new Date(review.created_at).toLocaleDateString()).appendTo(tr)
        })
    }

    // Load Users

    const users = await router("GET", ROUTES["USER"]["USER"])

    if (users) {
        const users_tbody = $("#users_tbody")
        users.forEach((user) => {
            const tr = $("<tr>").addClass("text-center").appendTo(users_tbody)
            $("<td>").text(user.name).appendTo(tr)
            $("<td>").text(user.mail).appendTo(tr)
            $("<td>").text(user.birth).appendTo(tr)
            $("<td>").text(new Date(user.created_at).toLocaleDateString()).appendTo(tr)
        })
    }


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