var signupmodal = document.getElementById("SignUpModal");
var loginmodal = document.getElementById("LogInModal");
var signup = document.getElementById("SignUp");
var login = document.getElementById("LogIn");
var closesignup = document.getElementById("CloseSignUp");
var closelogin =document.getElementById("CloseLogIn");
var menu =document.getElementById("menu");
var sidenav = document.getElementById("sidemodal");
// var closesidenav = document.getElementsByClassName("Closes")[2];
var details = document.getElementById("requestDetails")
// var closedetails = document.getElementsByClassName("Closes")[3];
// signing up 
signup.onclick = function(){
    signupmodal.style.display="block";
    loginmodal.style.display="none";
}
// closing signup form modal
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
login.onclick=function(){
    loginmodal.style.display="block";
    signupmodal.style.display="none";
}
// closing login form modal
closelogin.onclick=function(){
    loginmodal.style.display="none";
}

// menu button open side modal
function OpenMenu(){
    sidenav.style.display="block";
    details.style.display="none";
}
// request details
function Open(){
    details.style.display="block";
    sidenav.style.display="none";
    }
    // close request ride details
function Close(){
    details.style.display="none";
    
}   
function CloseMenu(){
    sidenav.style.display="none";
}
