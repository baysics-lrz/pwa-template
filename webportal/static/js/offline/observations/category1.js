import csrftoken from "../csrftoken.js";
import db from "../db_instance.js"
import {retrieveCurrentUser} from "../user.js"


/**
 * Stores all category1-instances from the Server to the IndexedDB
 * @returns {Promise<*>} A Promise with ID of the category1-instance last stored in the IDB
 */
export function storeAllCategory1FromServerInIDB() {
    return retrieveCurrentUser().then(function (userData) {
            return getAllCategory1FromAPI(userData.id).then(function (response) {
                if (!response.ok) {
                    throw response;
                }
                return response.json();
            }).then(function (category1list) {
                db.remote_category1.clear()
                return db.remote_category1.bulkPut(category1list);
            })
        }
    )
}

/**
 * Stores a new category1-instance in the IDB
 * @param category1data        A data-object
 * @returns {Promise<*>}    A Promise with the ID of the category1-instance which is stored in the IDB
 */
export function storeNewCategory1InIDB(category1data) {
    // setting the user-id to -1; the right user-id is set when category1-instance is uploaded
    category1data.user = -1;
    return db.local_category1.put(category1data);
}


/**
 * Uploads new and locally stored category1-instances to the Server
 * @param userID        The ID of the user, from whom the category1-observations are uploaded from
 * @returns {Promise}   A Promise waiting for the upload
 */
export function uploadNewCategory1ToServer(userID) {
    return db.local_category1.toArray().then(function (category1list) {
        for (let category1 of category1list) {
            console.log(category1, userID);
            let formData = new FormData();
            formData.append('Category1Subject', category1.Category1Subject);
            formData.append('Certainty', category1.Certainty);
            formData.append('Lon', category1.Lon);
            formData.append('Lat', category1.Lat);
            formData.append('Category1Feature2', category1.Category1Feature2);
            formData.append('Category1Feature3', category1.Category1Feature3);
            formData.append('Category1Feature1', category1.Category1Feature1);
            formData.append('ObservationTime', category1.ObservationTime);
            formData.append('ObservationDate', category1.ObservationDate);
            formData.append('AccuracyGPS', category1.AccuracyGPS);

            if (category1.Photo !== null) {
                formData.append('Photo', category1.Photo);
            }
            formData.append('user', userID);
            addCategory1ToAPI(formData).then(function (response) {
                if (!response.ok) {
                    throw new Error("Could not upload");
                }
                return response.json();
            }).then(function (json) {
                console.log("Added new category1 to server:", json);
                alert("Data successfully uploaded from offline interface!");
                return deleteLocalCategory1(category1.id);
            }).catch(function (error) {
                console.log("Error when uploading category1:", error);
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
 * Get the a category1-instance as object
 * @param category1_id      The ID of the category1-instance
 * @returns {Promise}   A Promise with the category1-object
 */
export function getLocalCategory1ByID(category1_id) {
    return db.local_category1.get(category1_id);
}


/**
 * Update a locally stored category1-instance
 * @param category1_id      The id of the updated category1
 * @param updated_data  The data which is updated
 * @returns {Promise}   Promise waiting for the update
 */
export function updateLocalCategory1(category1_id, updated_data) {
    return db.local_category1.update(category1_id, updated_data)
        .then(function (updated) {
            if (updated) {
                console.log("Entry was updated");
            } else {
                console.log("Not updated");
            }
        });
}

/**
 * Delete a category1-instance which is locally stored
 * @param category1_id      The ID of the deleted category1-instance
 * @returns {Promise}   Promise waiting for the deletion
 */
export function deleteLocalCategory1(category1_id) {
    return db.local_category1.delete(category1_id)
}


/**
 * Get all locally stored category1-instances as list of objects
 * @returns {Promise}   Promise with the list of the category1-instances
 */
export function getLocalCategory1AsList() {
    return db.local_category1.toArray();
}

/**
 * Get all category1-instances from the remote-database as list of objects
 * @returns {Promise}   Promise with the list of the category1-instances
 */
export function getRemoteCategory1AsList() {
    return db.remote_category1.toArray();
}


/**
 * Gets a list of all category1-instances
 * @returns {Promise<*>} A Promise with the Response of the API
 */
function getAllCategory1FromAPI(userID) {
    return fetch(`/api/observations/category1?user=${userID}`, {
        headers: {
            "X-CSRFToken": csrftoken
        }
    });
}

/**
 * Adds a category1-instance to the API
 * @param formData              Form data fo the new category1
 * @returns {Promise<Response>} A Promise with the Response of the API
 */
function addCategory1ToAPI(formData) {
    return fetch("/api/observations/category1/add", {
        method: "POST",
        headers: {
            "X-CSRFToken": csrftoken
        },
        body: formData
    });
}
