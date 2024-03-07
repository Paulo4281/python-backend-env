function auth(event) {
    event.preventDefault();

    const mail = $("#input_mail").val();
    const password = $("#input_password").val();

    if (!mail || !password) {
        createModal("Please insert valid credentials.")
        return false;
    }

    const login_button = $("#btn_login");
    
    async function sendAuth() {
        login_button.append(loader("text-light"))
        await axios.post(`${ENV["BASE_URL"]}/user/auth`, {
            mail,
            password
        }).then((response) => {
            loader(null, true)
        }).catch((error) => {
            loader(null, true)
            createModal(`Ops. <strong>${error.response.data.message}</strong>`)
        })
    }
        
    sendAuth();
}