$(document).ready(() => {

    const token = localStorage.getItem("token");

    // Books

    
    // axios.post(`${ROUTES["BOOK"]["BOOK"]}`, {
        //     headers: { Authorization: `Bearer ${token}` }
        // }).then((response) => {
            
            // })
            
        });
            function addBook() {
                createFormModal("Add Book", 3, ["text", "number", "text"], ["Title", "Price", "Category"]).modal("show");
            }