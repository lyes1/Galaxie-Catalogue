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
			   //$('#showresults').replaceWith($('#showresults',response));
				console.log(response);
				drawTable(response)
				//$("#result").html(response); 
				//$('page').html(response)
			},
			error: function(error){
				alert("Sorry, there was a problem!");
				console.log(error);
		
			}
		});
	});
});

function drawTable(data) {
	var col_name = []
	for(var key in data[0]){
		col_name.push(key)
	}

	var html = '<thead>';

	col_name.forEach (elm => html += '<th>' + elm + '</th>')

	html += '</thead><tbody>';

	$.each(data, function(k, v){
        html += '<tr><td>' + v.user + '</td><td>' + v.pass + '</td><td>' + v.status + '</td></tr>';
   }); 
   html += '</tbody>'; 
   console.log(html);
   $('#tableau').append(html);
  }
