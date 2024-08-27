import csrftoken from "../csrftoken.js";
import db from "../db_instance.js"
import {retrieveCurrentUser} from "../user.js"


/**
 * Stores all category2-instances from the Server to the IndexedDB
 * @returns {Promise<*>} A Promise with ID of the category2-instance last stored in the IDB
 */
export function storeAllCategory2FromServerInIDB() {
    return retrieveCurrentUser().then(function (userData) {
        return getAllCategory2FromAPI(userData.id).then(function (response) {
        if (!response.ok) {
            throw response;
        }
        return response.json();
    }).then(function (category2list) {
        return db.remote_category2.bulkPut(category2list);
    })
    })


}

/**
 * Stores a new category2-instance in the IDB
 * @param category2data
 * @returns {Promise<*>}    A Promise with the ID of the category2-instance which is stored in the IDB
 */
export function storeNewCategory2InIDB(category2data) {
    // setting the user-id to -1; the right user-id is set when category2-instance is uploaded
    category2data.user = -1;
    return db.local_category2.put(category2data);
}


/**
 * Uploads new and locally stored category2-instances to the Server
 * @param userID        The ID of the user, from whom the category2-observations are uploaded from
 * @returns {Promise}   A Promise waiting for the upload
 */
export function uploadNewCategory2ToServer(userID) {
    return db.local_category2.toArray().then(function (category2list) {
        for (let category2 of category2list) {
            let formData = new FormData();
            formData.append('Category2Subject', category2.Category2Subject);
            formData.append('Certainty', category2.Certainty);
            formData.append('Lon', category2.Lon);
            formData.append('Lat', category2.Lat);
            formData.append('Category2Feature1', category2.Category2Feature1);
            formData.append('Category2Feature2', category2.Category2Feature2);
            formData.append('Category2Feature3', category2.Category2Feature3);
            formData.append('Category2Feature4', category2.Category2Feature4);
            formData.append('Category2Feature5', category2.Category2Feature5);
            formData.append('Category2Feature6', category2.Category2Feature6);
            formData.append('Category2Feature7', category2.Category2Feature7);
            formData.append('Category2Feature8', category2.Category2Feature8);
            formData.append('AccuracyGPS', category2.AccuracyGPS);

            formData.append('ObservationDate', category2.ObservationDate);
            console.log(category2.Photo);
            if (category2.Photo !== null) {
                formData.append('Photo', category2.Photo);
            }
            formData.append('Position', category2.Position);
            formData.append('user', userID);
            addCategory2ToAPI(formData).then(function (response) {
                if (!response.ok) {
                    throw new Error("Could not upload");
                }
                return response.json();
            }).then(function (json) {
                console.log("Added new category2 to server:", json);
                alert("Data successfully uploaded from offline interface!");
                return deleteLocalCategory2(category2.id);
            }).catch(function (error) {
                console.log("Error when uploading category2:", error);
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
 * Get the a category2-instance as object
 * @param category2_id      The ID of the category2-instance
 * @returns {Promise}   A Promise with the category2-object
 */
export function getLocalCategory2ByID(category2_id) {
    return db.local_category2.get(category2_id);
}

/**
 * Update a locally stored category2-instance
 * @param category2_id      The id of the updated category2-instance
 * @param updated_data  The data which is updated
 * @returns {Promise}   Promise waiting for the update
 */
export function updateLocalCategory2(category2_id, updated_data) {
    return db.local_category2.update(category2_id, updated_data)
        .then(function (updated) {
            if (updated) {
                console.log("Entry was updated");
            } else {
                console.log("Not updated");
            }
        });
}

/**
 * Delete a category2-instance which is locally stored
 * @param category2_id      The ID of the deleted category2-instance
 * @returns {Promise}   Promise waiting for the deletion
 */
export function deleteLocalCategory2(category2_id) {
    return db.local_category2.delete(category2_id)
}


/**
 * Get all locally stored category2-instances as list of objects
 * @returns {Promise}   Promise with the list of the category2-instances
 */
export function getLocalCategory2AsList() {
    return db.local_category2.toArray();
}

/**
 * Get all category2-instances from the remote-database as list of objects
 * @returns {Promise}   Promise with the list of the category2-instances
 */
export function getRemoteCategory2AsList() {
    return db.remote_category2.toArray();
}


// ------------- category2-API-Functions

/**
 * Gets a list of all category2-instances from th API
 * @returns {Promise<*>} A Promise with the Response of the API
 */
function getAllCategory2FromAPI(userID) {
    return fetch(`/api/observations/category2?user=${userID}`, {
        headers: {
            "X-CSRFToken": csrftoken
        }
    });
}

/**
 * Adds a category2-instance to the API
 * @param formData              Form data fo the new category2
 * @returns {Promise<Response>} A Promise with the Response of the API
 */
function addCategory2ToAPI(formData) {
    return fetch("/api/observations/category2/add", {
        method: "POST",
        headers: {
            "X-CSRFToken": csrftoken
        },
        body: formData
    });
}
