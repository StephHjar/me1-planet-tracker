// Code adapted from a tutorial on JavaTPoint, credit in README
function verifyPassword() {
    let pw = document.getElementById("id_password1").value;
    //checks for empty password field  
    if (pw == "") {
        window.alert("**Fill in the password please!");
        return false;
    }

    //minimum password length validation  
    if (pw.length < 8) {
        window.alert("**Password length must be at least 8 characters");
        return false;
    }

    //maximum length of password validation  
    if (pw.length > 15) {
        window.alert("**Password length must not exceed 15 characters");
        return false;
    }
    return true;
}

var module = module || {};
module.exports = verifyPassword;