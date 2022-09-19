function buttonClick() {
    fetch("http://localhost:5000/usersjson")
    .then((response) => response.json())
    .then((data) => showResults(data));
}

function showResults(data) {
    console.log(data);
    let results = "";
    let table = "<table><tr><th>#</th><th>Username</th><th>Email</th></tr>";

    data.forEach((datum, index) => {
        console.log(datum);
        table += "<tr id='" + datum.username + "'>";
        table += "<td>" + index + "</td>";
        table += "<td>" + datum.username + "</td>";
        table += "<td>" + datum.email + "</td>";
        table += "</tr>";
    });

    table += "</table>";

    console.log(table);

    document.getElementById("result").innerHTML = table;
}

function showResult(dato) {
    console.log(dato);
    if (!dato.success) {
        document.getElementById("registerResult").innerHTML = "Server error!";
        return;
    }

    let results = document.getElementById("result").innerHTML

    results+="</div id='" + dato.username  + "'>Username: " + dato.username + " Email: " + dato.email + "<br></div>";

    document.getElementById("registerResult").innerHTML = "Success!"
    document.getElementById("result").innerHTML = results;
}

function hideUsers() {
    document.getElementById("result").innerHTML = "";
}

function hideUser(data) {
    if (!data.success) {
        document.getElementById("deleteResult").innerHTML = "Server error!";
        return;
    }

    const username = data.username;

    const element = document.getElementById(username);
    document.getElementById("deleteResult").innerHTML = "Success!"
    element.remove();
}

function deleteUser() {
    const deleteUser = document.getElementById("deleteUser").value;

    const body = {
        "username": deleteUser
    };

    const url = "http://localhost:5000/login/delete";

    fetch(url, {
        method: 'POST',
        body: JSON.stringify(body),
        headers: {
            "Content-Type":"application/json"
        }
    })
    .then((response) => response.json())
    .then((data) => hideUser(data));
}

function registerUser() {
    const newUsername = document.getElementById("newUsername").value;
    const newPassword = document.getElementById("newPassword").value;
    const newEmail = document.getElementById("newEmail").value;

    const body = {
        "newUsername": newUsername,
        "newPassword": newPassword,
        "newEmail": newEmail
    };

    const url = "http://localhost:5000/login/register";

    fetch(url, {
        method: 'POST',
        body: JSON.stringify(body),
        headers: {
            "Content-Type":"application/json"
        }
    })
    .then((response) => response.json())
    .then((data) => showResult(data));
}
/*
const registerUser = (param1, param2, param3) => {
    //codigo
}*/