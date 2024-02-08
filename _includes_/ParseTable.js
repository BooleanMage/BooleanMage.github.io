function ParseTable(tableData, translateMapping, language) {
    // Loop over each row
    for(let i=0; i<tableData.length; i++) {
        // Get the question
        let question = tableData[i]['Question'];

        // If the question is in the translate mapping, assign the type and translation
        if(question in translateMapping) {
            tableData[i]['type'] = translateMapping[question]['type'];
            tableData[i]['translation'] = translateMapping[question]['translations'][language];

            // If the type is 'Checkbox', parse the answer into a JSON array
            if(translateMapping[question]['type'] === 'Checkbox') {
                // Assume the answers are in a column named 'Answer' and are comma-separated
                let answer = tableData[i]['Answer'];
                tableData[i]['Answer'] = answer.split(',').map(Number);
            }
        }
    }

    return tableData;
}

module.exports = ParseTable;