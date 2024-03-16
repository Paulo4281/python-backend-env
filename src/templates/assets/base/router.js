async function router(method, route, data={}) {
    const token = ENV["TOKEN"]
    let response
    if (method === "GET") {
        response = await axios.get(route, {
            headers: { Authorization: `Bearer ${token}` }
        })
    } else if (method === "POST") {
        console.log(data)
        response = await axios.post(route, data, {
            headers: { Authorization: `Bearer ${token}` }
        })
    } else if(method === "PUT") {
        response = await axios.put(route, data, {
            headers: { Authorization: `Bearer ${token}` }
        })
    } else if (method === "DELETE") {
        response = await axios.delete(route, {
            headers: { Authorization: `Bearer ${token}` }
        })
    }
    return response.data
}