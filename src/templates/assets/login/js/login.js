function login(event) {
    event.preventDefault();

    const mail = $("#input_mail").val();
    const password = $("#input_password").val();

    if (!mail || !password) {
        createModal("Please insert valid credentials.").modal("show")
        return false;
    }

    const login_button = $("#btn_login");
    
    async function sendAuth() {
        login_button.append(createSpinner("text-light"));
        await axios.post(`${ENV["BASE_URL"]}/user/auth`, {
            mail,
            password
        }).then(async (response) => {
            $("#login_button_spinner").remove();
            if (response.data.token) {
                const token = response.data.token;
                localStorage.setItem("token", token);
                await axios.get(`${ENV["BASE_URL"]}/dash`, {
                    headers: { Authorization: `Bearer ${localStorage.getItem("token")}` }
                }).then(() => {
                    window.location.href = `${ENV["BASE_URL"]}/dash`;
                })
            }
        }).catch((error) => {
            $("#login_button_spinner").remove();
            if (error.response.data) {
                createModal(`Ops. <strong>${error.response.data.message}</strong>`).modal("show")
            } else {
                createModal(`Something went wrong.`).modal("show")
            }
        })
    }
        
    sendAuth();
}