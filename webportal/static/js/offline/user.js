import csrftoken from "./csrftoken.js";


export function retrieveCurrentUser() {
    return fetch("/api/accounts/user", {
        headers: {
            "X-CSRFToken": csrftoken
        }
    }).then(function (response) {
       if (!response.ok) {
            throw new Error("User not authenticated");
        }
        return response.json();
    })
}