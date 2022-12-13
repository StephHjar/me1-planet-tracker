// Code adapted from a tutorial on JavaTPoint, credit in README
function verifyPassword() {
    var pw = document.getElementById("id_password1").value;
    //check empty password field  
    if (pw == "") {
        window.alert("**Fill in the password please!");
        return false;
    }

    //minimum password length validation  
    if (pw.length < 8) {
        window.alert("**Password length must be atleast 8 characters");
        return false;
    }

    //maximum length of password validation  
    if (pw.length > 15) {
        window.alert("**Password length must not exceed 15 characters");
        return false;
    } else {
        alert("Password is correct");
    }
}