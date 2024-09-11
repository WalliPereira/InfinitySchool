function login() {
    var usuario = document.getElementById("username").value 
    var senha = document.getElementById("password").value

    if(usuario == "Walli" && senha == "1234") {
        window.alert("Login efetuado com sucesso")
    } else {
        window.alert("Login negado")
    }

}