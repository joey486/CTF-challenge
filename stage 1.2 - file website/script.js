function checkPassword() {
    const correctPassword = "123456";
    const userPassword = document.getElementById("passwordInput").value;

    if (userPassword === correctPassword) {
        alert("Correct password! The file will now download.");
        document.getElementById("downloadLink").click();
    } else {
        alert("Incorrect password. Please try again.");
    }
}

console.log("Welcome to My Website!");
