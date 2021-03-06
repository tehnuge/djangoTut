import React from 'react'

var SignUp = React.createClass({
	handleSubmit: function(){
		var password = document.getElementById('password').value;
		var password2 = document.getElementById('password2').value;
		if(password !== password2){
			console.log(password2)
			alert("Passwords didn't match man");
		}
		else{
			var username = document.getElementById('username').value;
			var data = {
				'username': username,
				'password': password
			}
/*			$.post('/signup/', data, function() {
				console.log('signup success')
			})*/
		}
	},
	render: function(){
		return(
				<div>
				<h2>Sign Up </h2>
					<form method="post" action="/signup/">
					<input type="hidden" name="csrfmiddlewaretoken" value={cookie} />
					<b>Account Name </b>
					<input id="username" name="username" type="text"
					       placeholder="Your account name"
					       autocomplete="off" />
					<br />
					<b>Password </b>
			       	<input id="password" name="password" type="password"
			              placeholder="Your password"
			              autocomplete="off" />
			        <br />
					<b>Password again </b>
	              	<input id="password2" name="password2" type="password"
	                     placeholder="Type your password again"
	                     autocomplete="off" />
			              <input type="submit" class="button" value="Submit" onClick = {this.handleSubmit} />
			       </form>
				</div>
			)
	}
})

module.exports = SignUp