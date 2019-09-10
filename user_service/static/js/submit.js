function submit(_username, _password){
	var data = {
            username: _username,
            password: _password,
        };

	fetch("/login", {
	  method: "POST", 
	  body: JSON.stringify(data)
	}).then(res => {
  		console.log("Request complete! response:", res);
	});
}
