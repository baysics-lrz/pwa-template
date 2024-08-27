import csrftoken from "../csrftoken.js";
import db from "../db_instance.js"
import {retrieveCurrentUser} from "../user.js";

/**
 * Stores all category3-instances from the Server to the IndexedDB
 * @returns {Promise<*>} A Promise with ID of the category3-instance last stored in the IDB
 */
export function storeAllCategory3FromServerInIDB() {
    return retrieveCurrentUser().then(function (userData) {
            return getAllCategory3FromAPI(userData.id).then(function (response) {
                if (!response.ok) {
                    throw response;
                }
                return response.json();
            }).then(function (category3list) {
                db.remote_category3.clear()
                return db.remote_category3.bulkPut(category3list);
            })
        }
    )
}

/**
 * Stores a new category3-instance in the IDB
 * @param category3data
 * @returns {Promise<*>}    A Promise with the ID of the category3-instance which is stored in the IDB
 */
export function storeNewCategory3InIDB(category3data) {
    // setting the user-id to -1; the right user-id is set when category3-instance is uploaded
    category3data.user = -1;
    return db.local_category3.put(category3data);
}

/**
 * Uploads new and locally stored category3-instances to the Server
 * @param userID        The ID of the user, from whom the category3-observations are uploaded from
 * @returns {Promise}   A Promise waiting for the upload
 */

export function uploadNewCategory3ToServer(userID) {
    return db.local_category3.toArray().then(function (category3list) {
        for (let category3 of category3list) {
            let formData = new FormData();
            formData.append('Category3Subject', category3.Category3Subject);
            formData.append('Certainty', category3.Certainty);
            formData.append('Lon', category3.Lon);
            formData.append('Lat', category3.Lat);
            formData.append('Category3Feature2', category3.Category3Feature2);
            formData.append('Category3Feature1', category3.Category3Feature1);
            formData.append('ObservationDate', category3.ObservationDate);
            formData.append('AccuracyGPS', category3.AccuracyGPS);
            console.log(category3.Photo);

            if (category3.Photo !== null) {
                formData.append('Photo', category3.Photo);
            }
            formData.append('Position', category3.Position);
            formData.append('user', userID);
            addCategory3ToAPI(formData).then(function (response) {
                if (!response.ok) {
                    throw new Error("Could not upload");
                }
                return response.json();
            }).then(function (json) {
                console.log("Added new category3 to server:", json);
                alert("Data successfully uploaded from offline interface!");
                return deleteLocalCategory3(category3.id);
            }).catch(function (error) {
                console.log("Error when uploading Category3:", error);
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
 * Get the a category3-instance as object
 * @param category3_id      The ID of the category3-instance
 * @returns {Promise}   A Promise with the category3-object
 */
export function getLocalCategory3ByID(category3_id) {
    return db.local_category3.get(category3_id);
}

/**
 * Update a locally stored category3-instance
 * @param category3_id      The id of the updated category3
 * @param updated_data  The data which is updated
 * @returns {Promise}   Promise waiting for the update
 */
export function updateLocalCategory3(category3_id, updated_data) {
    return db.local_category3.update(category3_id, updated_data)
        .then(function (updated) {
            if (updated) {
                console.log("Entry was updated");
            } else {
                console.log("Not updated");
            }
        });
}

/**
 * Delete a category3-instance which is locally stored
 * @param category3_id      The ID of the deleted category3-instance
 * @returns {Promise}   Promise waiting for the deletion
 */
export function deleteLocalCategory3(category3_id) {
    return db.local_category3.delete(category3_id)
}

/**
 * Get all locally stored category3-instances as list of objects
 * @returns {Promise}   Promise with the list of the category3-instances
 */
export function getLocalCategory3AsList() {
    return db.local_category3.toArray();
}

/**
 * Get all category3-instances from the remote-database as list of objects
 * @returns {Promise}   Promise with the list of the category3-instances
 */
export function getRemoteCategory3AsList() {
    return db.remote_category3.toArray();
}

/**
 * Gets a list of all category3-instances
 * @returns {Promise<*>} A Promise with the Response of the API
 */
function getAllCategory3FromAPI(userID) {
    return fetch(`/api/observations/category3?user=${userID}`, {
        headers: {
            "X-CSRFToken": csrftoken
        }
    });
}

/**
 * Adds a category3-instance to the API
 * @param formData              Form data fo the new category3
 * @returns {Promise<Response>} A Promise with the Response of the API
 */
function addCategory3ToAPI(formData) {
    return fetch("/api/observations/category3/add", {
        method: "POST",
        headers: {
            "X-CSRFToken": csrftoken
        },
        body: formData
    }).catch(err => console.log(err))
}
