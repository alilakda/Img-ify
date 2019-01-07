

$(document).ready(function(){
	function verifyPass(pass) {
		var fail = [];
		if (pass.length < 8) {
			fail.push(1);
		}
		var noUpper = true;
		var noNumber = true;
		for (var i = 0; i < pass.length; ++i) {
			if (!isNaN(parseInt(pass[i]))) {
				//numeric
				noNumber = false;
			} else {
				if (pass[i].toLowerCase() != pass[i].toUpperCase()) {
					if (pass[i] == pass[i].toUpperCase()) {
						//uppercase
						noUpper = false;
					}
				}
			}
		}
		if (noUpper) {
			fail.push(2);
		}
		if (noNumber) {
			fail.push(3);
		}
		return fail;
	}

	function statusMessage(message) {
		if($("#p1").length) {
			$("#p1").text(message);
		} else {
			$('#main').append("<p id='p1' style='text-align: center'>" + message + "</p>");
		}
	}

	$('#btnId').click(function(){
		var user = $('#inputUsername').val();
		var pass = $('#inputPassword').val();

		badPass = verifyPass(pass);
		var status;
		if (badPass.length == 0) {
			statusMessage("Congratulations on registering for CSE6242, " + user + "! Redirecting you to the course homepage...")
			status = 'OK';
		} else {
			status = 'BAD';

			var message = user + ', the password is invalid because it, ';
			for(var i = 0; i < badPass.length; ++i) {
				if (badPass[i] == 1) {
					message = message + '1. Should be at least 8 characters in length... ';
				} else if (badPass[i] == 2) {
					message = message + '2. Should have at least 1 uppercase character... ';
				} else if (badPass[i] == 3) {
					message = message + '3. Should have at least 1 number... ';
				}
			}
			message = message + 'Please Try Again!';
			statusMessage(message);

		}

		var jsonData = $('form').serialize() + '&status=' + status + '&fail=[' + badPass + ']';

		$.ajax({
			url: '/signUpUser',
			data: jsonData,
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});

		if (status == 'OK') {
			$("#form1").trigger("reset");
			setTimeout(function() {
				document.location = 'http://poloclub.gatech.edu/cse6242/';
			}, 3000);
		} else if (status == 'BAD') {
			$('#inputPassword').val('');
		}
	});
});
