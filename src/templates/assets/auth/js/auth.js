function auth(event) {

    const BASE_URL = "http://localhost:8080"

    event.preventDefault();

    const mail = $("#input_mail").val();
    const password = $("#input_password").val();

    if (!mail || !password) {
        return false;
    }

    sendAuth()

    async function sendAuth() {
        await axios.post(`${BASE_URL}/user/auth`, {
            mail,
            password
        }).then((response) => {
            console.log(response)
        }).catch((error) => {
            console.error(error)
            $("#auth_alert").remove()
            $("#form_container").prepend(
                $("<div>").addClass("alert alert-danger alert-dismissible fade show").attr("id", "auth_alert")
                .append("<strong>")
                .text(error.response.data.message)
            )
        })
    }

}