import csrftoken from "../csrftoken.js";
import db from "../db_instance.js"
import {retrieveCurrentUser} from "../user.js"

/**
 * Stores all category4-instances from the Server to the IndexedDB
 * @returns {Promise<*>} A Promise with ID of the category4-instance last stored in the IDB
 */
export function storeAllCategory4FromServerInIDB() {
    return retrieveCurrentUser().then(function (userData) {
            return getAllCategory4FromAPI(userData.id).then(function (response) {
                if (!response.ok) {
                    throw response;
                }
                return response.json();
            }).then(function (category4list) {
                db.remote_category4.clear()
                return db.remote_category4.bulkPut(category4list);
            })
        }
    )
}

/**
 * Stores a new category4-instance in the IDB
 * @param category4data
 * @returns {Promise<*>}    A Promise with the ID of the category4-instance which is stored in the IDB
 */
export function storeNewCategory4InIDB(category4data) {
    // setting the user-id to -1; the right user-id is set when category4-instance is uploaded
    category4data.user = -1;
    return db.local_category4.put(category4data);
}

/**
 * Uploads new and locally stored category4-instances to the Server
 * @param userID        The ID of the user, from whom the category4-observations are uploaded from
 * @returns {Promise}   A Promise waiting for the upload
 */
export function uploadNewCategory4ToServer(userID) {
    return db.local_category4.toArray().then(function (category4list) {
        for (let category4 of category4list) {
            let formData = new FormData();
            formData.append('Category4Subject', category4.Category4Subject);
            formData.append('Certainty', category4.Certainty);
            formData.append('Lon', category4.Lon);
            formData.append('Lat', category4.Lat);
            formData.append('Category4Feature1', category4.Category4Feature1);
            formData.append('Category4Feature3', category4.Category4Feature3);
            formData.append('Category4Feature2', category4.Category4Feature2);
            formData.append('ObservationDate', category4.ObservationDate);
            formData.append('AccuracyGPS', category4.AccuracyGPS);
            console.log(category4.Photo);
            if (category4.Photo !== null) {
                formData.append('Photo', category4.Photo);
            }
            formData.append('Position', category4.Position);
            formData.append('user', userID);
            addCategory4ToAPI(formData).then(function (response) {
                if (!response.ok) {
                    throw new Error("Could not upload");
                }
                return response.json();
            }).then(function (json) {
                console.log("Added new category4 to server:", json);
                alert("Data successfully uploaded from offline interface!");
                return deleteLocalCategory4(category4.id);
            }).catch(function (error) {
                console.log("Error when uploading category4:", error);
                var alerted = localStorage.getItem('alerted') || '';
                if (alerted != 'yes') {
                    alert("Problem uploading (some) data from offline interface, please check the data again!");
                    localStorage.setItem('alerted','yes');
                }
            });
        }
    });
}

/**
 * Get the a category4-instance as object
 * @param category4_id      The ID of the category4-instance
 * @returns {Promise}   A Promise with the category4-object
 */
export function getLocalCategory4ByID(category4_id) {
    return db.local_category4.get(category4_id);
}

/**
 * Update a locally stored category4-instance
 * @param category4_id      The id of the updated category4
 * @param updated_data  The data which is updated
 * @returns {Promise}   Promise waiting for the update
 */
export function updateLocalCategory4(category4_id, updated_data) {
    return db.local_category4.update(category4_id, updated_data)
        .then(function (updated) {
            if (updated) {
                console.log("Entry was updated");
            } else {
                console.log("Not updated");
            }
        });
}

/**
 * Delete a category4-instance which is locally stored
 * @param category4_id      The ID of the deleted category4-instance
 * @returns {Promise}   Promise waiting for the deletion
 */
export function deleteLocalCategory4(category4_id) {
    return db.local_category4.delete(category4_id)
}

/**
 * Get all locally stored category4-instances as list of objects
 * @returns {Promise}   Promise with the list of the category4-instances
 */
export function getLocalCategory4AsList() {
    return db.local_category4.toArray();
}

/**
 * Get all category4-instances from the remote-database as list of objects
 * @returns {Promise}   Promise with the list of the category4-instances
 */
export function getRemoteCategory4AsList() {
    return db.remote_category4.toArray();
}

// -------------- Category4-API-Functions --------------------

/**
 * Gets a list of all category4-instances
 * @returns {Promise<*>} A Promise with the Response of the API
 */
function getAllCategory4FromAPI(userID) {
    return fetch(`/api/observations/category4?user=${userID}`, {
        headers: {
            "X-CSRFToken": csrftoken
        }
    });
}

/**
 * Adds a category4-instance to the API
 * @param formData              Form data fo the new category4
 * @returns {Promise<Response>} A Promise with the Response of the API
 */
function addCategory4ToAPI(formData) {
    return fetch("/api/observations/category4/add", {
        method: "POST",
        headers: {
            "X-CSRFToken": csrftoken
        },
        body: formData
    });
}
