function send_mail(){
    var data = JSON.stringify({
    "email": document.getElementById('email').value,
    "message": document.getElementById('problem').value,
    "first_name": document.getElementById('firstname').value,
    "last_name": document.getElementById('lastname').value
    });

    var config = {
    method: 'post',
    url: 'http://127.0.0.1:8000',
    headers: { 
        'Content-Type': 'application/json'
    },
    data : data
    };

    axios(config)
    .then(function (response) {
    console.log(JSON.stringify(response.data));
    })
    .catch(function (error) {
    console.log(error);
    });
    alert("Your problem has been heard. Thank you")
    location.href = "http://127.0.0.1:5500/";
}