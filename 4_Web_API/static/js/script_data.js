// Fonction à exécuter après apui sur le bouton ok
$(function(){
	$('#submit').click(function(){
		var user = $('#inputUsername').val();
        var pass = $('#inputPassword').val();

        $.pony.load('/api/celestialObjetcs/results', {
            data: {"user": user, "pass":pass},
            success: function (response) {
				if (response.length != 0){
					drawTable(response)
				}
				else {
					$('#data_display').append('<p class="h2">No Data found !</p>');
				}
            },
            error: function(error){
				alert("Sorry, there was a problem!");		
			}
        });
	});
});


// fonction appelée après le renvoi des données depuis le serveur à fin d'insérer la table des données
function drawTable(data) {
	var keys = data[0]
	var objects = data[1]
	var col_name = []
	for(var key in data[0]){
		col_name.push(key)
	}

	var html = '<thead>';

	keys.forEach (elm => html += '<th>' + elm + '</th>')

	html += '</thead><tbody>';

	$.each(objects, function(k, v){
		html += '<tr>';
		keys.forEach (elm => html += '<td>' + v[elm] + '</td>');
		html += '</tr>';
   }); 
   html += '</tbody>'; 

   $('#dtHorizontalVerticalExample').append(html);

// ajout de style DataTable
$(document).ready(function() {
    $('#dtHorizontalVerticalExample').DataTable( {
		retrieve: true,
		paging: false,
        dom: 'Bfrtip',
        buttons: [
            {
                text: 'Download CSV',
                action: function ( e, dt, node, config ) {
					exportCSVFile(keys, objects, 'objects'); // call the exportCSVFile() function to process the JSON and trigger the download
                }
            }
        ],
		"scrollX": true,
		"scrollY": 500,	
	} );
	$('.dataTables_length').addClass('bs-select');
} );

}

// Ref:  https://medium.com/@danny.pule/export-json-to-csv-file-using-javascript-a0b7bc5b00d2
function convertToCSV(objArray) {
    var array = typeof objArray != 'object' ? JSON.parse(objArray) : objArray;
    var str = '';

    for (var i = 0; i < array.length; i++) {
        var line = '';
        for (var index in array[i]) {
            if (line != '') line += ','

            line += array[i][index];
        }

        str += line + '\r\n';
    }

    return str;
}

function exportCSVFile(headers, items, fileTitle) {
	console.log(items)
    if (headers) {
        items.unshift(headers);
    }

    // Convert Object to JSON
    var jsonObject = JSON.stringify(items);

    var csv = this.convertToCSV(jsonObject);

    var exportedFilenmae = fileTitle + '.csv' || 'export.csv';

    var blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
    if (navigator.msSaveBlob) { // IE 10+
        navigator.msSaveBlob(blob, exportedFilenmae);
    } else {
        var link = document.createElement("a");
        if (link.download !== undefined) { // feature detection
            // Browsers that support HTML5 download attribute
            var url = URL.createObjectURL(blob);
            link.setAttribute("href", url);
            link.setAttribute("download", exportedFilenmae);
            link.style.visibility = 'hidden';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        }
    }
}

var headers = {
    model: 'Phone Model'.replace(/,/g, ''), // remove commas to avoid errors
    chargers: "Chargers",
    cases: "Cases",
    earphones: "Earphones"
};

itemsNotFormatted = [
    {
        model: 'Samsung S7',
        chargers: '55',
        cases: '56',
        earphones: '57',
        scratched: '2'
    },
    {
        model: 'Pixel XL',
        chargers: '77',
        cases: '78',
        earphones: '79',
        scratched: '4'
    },
    {
        model: 'iPhone 7',
        chargers: '88',
        cases: '89',
        earphones: '90',
        scratched: '6'
    }
];

var itemsFormatted = [];

// format the data
itemsNotFormatted.forEach((item) => {
    itemsFormatted.push({
        model: item.model.replace(/,/g, ''), // remove commas to avoid errors,
        chargers: item.chargers,
        cases: item.cases,
        earphones: item.earphones
    });
})
	

itemsNotFormatted.forEach((item) => {
	i = {

	}
	itemsFormatted.push(i);

})