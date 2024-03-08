function logout() {
    if (localStorage.getItem("token")) {
        localStorage.removeItem("token");
        window.location.href = `${ENV["BASE_URL"]}`
    }
}