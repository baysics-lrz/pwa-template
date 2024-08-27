import {retrieveCurrentUser} from "./user.js";
import {storeAllCategory1FromServerInIDB, uploadNewCategory1ToServer} from "./observations/category1.js";
import {storeAllCategory2FromServerInIDB, uploadNewCategory2ToServer} from "./observations/category2.js";
import {storeAllCategory3FromServerInIDB, uploadNewCategory3ToServer} from "./observations/category3.js";
import {storeAllCategory4FromServerInIDB, uploadNewCategory4ToServer} from "./observations/category4.js";


export function uploadAllLocalEntries() {
    return retrieveCurrentUser().then(function (userData) {
        return uploadNewCategory1ToServer(userData.id).then(function () {
            return uploadNewCategory2ToServer(userData.id);
        }).then(function () {
            return uploadNewCategory3ToServer(userData.id);
        }).then(function () {
            return uploadNewCategory4ToServer(userData.id);
        });
    }).then(function () {
        console.log("Uploaded stored observations to Server");
    });
}

// This function is not used in the template, please use depending on the need
export function downloadAllRemoteEntries() {
    return storeAllCategory1FromServerInIDB().then(function () {
        return storeAllCategory2FromServerInIDB();
    }).then(function () {
        return storeAllCategory3FromServerInIDB();
    }).then(function () {
        return storeAllCategory4FromServerInIDB();
    }).then(function () {
        console.log("Downloaded observations from Server");
    })
}