var signupmodal = document.getElementById("SignUpModal");
var loginmodal = document.getElementById("LogInModal")
var signup = document.getElementById("SignUp");
var login = document.getElementById("LogIn");
var closesignup = document.getElementsByClassName("Close")[0];
var closelogin =document.getElementsByClassName("Close")[1];

// signing up 
signup.onclick=function(){
    signupmodal.style.display="block";
    loginmodal.style.display="none";
}
// closing signup form modal
closesignup.onclick=function(){
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
