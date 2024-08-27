const db = new Dexie('Portal');

db.version(1).stores({

     // table for the category1 which are stored locally
    local_category1: "id++, Category1Subject, Certainty, Number, Category1Feature1, Category1Feature2, " +
        "Category1Feature3, ObservationDate, ObservationTime, Lat, Lon, Position, ClimateStation, Municipal, Cell, AccuracyGPS, user",
    // table for the category1 which are fetched from the server
    remote_category1: "id, Category1Subject, Certainty, Number, Category1Feature1, Category1Feature2, " +
        "Category1Feature3, ObservationDate, ObservationTime, Lat, Lon, Position, ClimateStation, Municipal, Cell, AccuracyGPS, user",
    local_category2: "id++, Category2Subject, Certainty, Category2Feature3, Category2Feature4, Category2Feature5, Category2Feature6, Category2Feature7, " +
        "Category2Feature8, Category2Feature1, Category2Feature2, Lat, Lon, Position" +
        "ObservationDate, AccuracyGPS, user",
    remote_category2: "id, Category2Subject, Certainty, Category2Feature3, Category2Feature4, Category2Feature5, Category2Feature6, Category2Feature7, " +
        "Category2Feature8, Category2Feature1, Category2Feature2, Lat, Lon, Position, ClimateStation" +
        "Municipal, Cell, ObservationDate, AccuracyGPS, user",
    local_category3: "id++, Category3Subject, Certainty, Category3Feature1, Category3Feature2, ObservationDate, " +
        "Lat, Lon, Position, " +
        "ClimateStation, Municipal, Cell, AccuracyGPS, user",
    remote_category3: "id, Category3Subject, Certainty, Category3Feature1, Category3Feature2, ObservationDate, " +
        "Lat, Lon, Position, " +
        "ClimateStation, Municipal, Cell, AccuracyGPS, user",
    local_category4: "id++, Category4Subject, Certainty, Category4Feature1, Category4Feature2, Category4Feature3, Lat, Lon, Position" +
        "ObservationDate, AccuracyGPS, user",
    remote_category4: "id, Category4Subject, Certainty, Category4Feature1, Category4Feature2, Category4Feature3, Lat, Lon, Position, " +"ClimateStation, Municipal, Cell, ObservationDate, AccuracyGPS, user",

});

export default db
