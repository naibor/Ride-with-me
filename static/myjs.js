// var menu =document.getElementById("menu");
// var closesidenav = document.getElementsByClassName("Close");


// signing up 
var signup = document.getElementById("SignUp");
var signupmodal = document.getElementById("SignUpModal");
signup.onclick = function(){
    signupmodal.style.display="block";
    loginmodal.style.display="none";
}
// closing signup form modal
var closesignup = document.getElementsByClassName("Close")[0];
closesignup.onclick = function(){
    signupmodal.style.display="none";
}

// when user clicks anywhere outside modal
window.onclick = function(event){
    if(event.target == signupmodal){
        signupmodal.style.display="none";
    }
}

// login modal form
var login = document.getElementById("LogIn");
var loginmodal = document.getElementById("LogInModal");
login.onclick=function(){
    loginmodal.style.display="block";
    signupmodal.style.display="none";
}
// closing login form modal
var closelogin =document.getElementsByClassName("Close")[1];
closelogin.onclick=function(){
    loginmodal.style.display="none";
}

// menu button
var sidenav = document.getElementById("sidemodal");
function Open(){
    sidenav.style.display="block";
}

// close side nav
function Close(){
    sidenav.style.display="none";
}

// request details
var request = document.getElementById("requestDetails");
function Open(){
    request.style.display="block";
}
// close request details
function Close(){
    request.style.display="none";
}

// request table
var table =document.getElementsByClassName("requestTable");
function Open(){
    table.style.display="block";
}

// close table
