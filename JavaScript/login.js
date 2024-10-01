/* Puxar a função no DOM para o codigo funcionar.*/

document.getElementById("loginForm").addEventListener("submit", function (event) {
    event.preventDefault();

    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    if (username.trim() === "" || password.trim() ==="") {
        alert("Please fill in all fields.");
        return;
    }

    if (username === "WspZero" && password === "9607") {
        alert("Successful login");

        /* Abaixo crie uma pagina e coloque a hef dela (page002.html) */
        window.location.href = "page002.html";
    } else {
        alert("Username or Password invalid");
    }
});
