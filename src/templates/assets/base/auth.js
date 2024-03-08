$(document).ready(async () => {

    if (localStorage.getItem("token")) {
        token = localStorage.getItem("token");
        
        await axios.post(`${ENV["BASE_URL"]}/verify`, {
            headers: { authorization: `Bearer ${token}` }
        }).then((response) => {
            if (response.data.status !== "authorized") {
                window.location.href = `${ENV["BASE_URL"]}/`
            }
        })
    } else {
        window.location.href = `${ENV["BASE_URL"]}/`
    }

});