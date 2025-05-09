function login() {
    const username = document.getElementById("username-input").value;
    const password = document.getElementById("password-input").value;

    // Vulnerable code: directly inserting user input into the DOM
    document.getElementById("login-result").innerHTML = "Welcome, " + username + "!";

    // Hidden flag element, revealed only via XSS
    if (username.includes("<script>")) {
        window.location.href = "home.html"; // Redirect to the home page when XSS is successful
    }
}
