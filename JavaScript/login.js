document.getElementById("loginForm").addEventListener("submit", function (event) {
    event.preventDefault();

    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    if (username.trim() === "" || password.trim() ==="") {
        alert("Please fill in all fields.");
        return;
    }

    if (username === "Formiguinha" && password === "9898") {
        alert("Successful login");

        window.location.href = "page002.html";
    } else {
        alert("Username or Password invalid");
    }
});
