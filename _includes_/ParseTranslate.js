function ParseTranslate(translateData) {
    // Create an empty object to store the mapping
    let translateMapping = {};

    // Initialize ordinal
    let ordinal = 0;

    // Loop over each row
    for(let i=0; i<translateData.length; i++) {
        // Create an empty object to store the translations
        let translations = {};

        // Loop over each property (column) in the row
        for(let prop in translateData[i]) {
            // If the property is not 'en' and not 'type', add it to the translations
            if(prop !== 'en' && prop !== 'type') {
                translations[prop] = translateData[i][prop];
            }
        }

        // If 'type' is not empty, reset ordinal to 0
        if(translateData[i]['type'] !== "") {
            ordinal = 0;
        }

        // Add the mapping
        translateMapping[translateData[i]['en']] = {
            'type': translateData[i]['type'],
            'ordinal': ordinal,
            'translations': translations,
        };

        // If 'type' is empty, increment ordinal
        if(translateData[i]['type'] === "") {
            ordinal++;
        }
    }

    return translateMapping;
}

module.exports = ParseTranslate;