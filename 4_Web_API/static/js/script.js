// Fonction à exécuter après apui sur le bouton ok
$(function(){
	$('button').click(function(){
		var user = $('#inputUsername').val();
		var pass = $('#inputPassword').val();
		$.ajax({
			url: '/api/celestialObjetcs/results',
			data: $('form').serialize(),
			type: 'POST',
			dataType : 'json', // Le type de données à recevoir, ici, du HTML.
			success: function(response){
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
	console.log(objects)
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
   $(document).ready(function () {
	$('#dtHorizontalVerticalExample').DataTable({
	"scrollX": true,
	"scrollY": 500,
	});
	$('.dataTables_length').addClass('bs-select');
	});
  }


 