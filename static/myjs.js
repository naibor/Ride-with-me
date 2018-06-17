// signup modal
var signupmodal = document.getElementById("SignUpModal");
// login modal
var loginmodal = document.getElementById("LogInModal");
// signup button
var signup = document.getElementById("SignUp");
// login button
var login = document.getElementById("LogIn");
// close signup icon
var closesignup = document.getElementById("CloseSignUp");
// close login icon
var closelogin =document.getElementById("CloseLogIn");
var sidenav = document.getElementById("sidemodal");
var details = document.getElementById("requestDetails");
var UserSideNav =document.getElementById("UsersideModal");
var ridedetails = document.getElementById("requestRide");
// tables
var tablerequests = document.getElementById("requestTable");
var availablerides = document.getElementById("RidesTable")
// Index page
// signing up 
signup.onclick = function() {
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
    sidenav.style.display="flex";
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
// close side nav driver  
function CloseMenu(){
    sidenav.style.display="none";
}

// user sidenav
// open side nav 
function Openside(){
    UserSideNav.style.display="flex";
    ridedetails.style.display="none";
}
// close user side nav
function Closeside(){
    UserSideNav.style.display="none";
}

// open ride request
function Openride(){
    ridedetails.style.display="block";
    UserSideNav.style.display="none";
}
// closing ride request
function Closeride(){
    ridedetails.style.display="none";
}

// open table requests
function Openrequests(){
    tablerequests.style.display="block"
}

// close table requests
function Closetable(){
    tablerequests.style.display="none";
    ridedetails.style.display="none";
}
// open available rides
function OpenRides(){
    availablerides.style.display="block";
    ridedetails.style.display="none";  

}
// close available rides
function CloseRides(){
    availablerides.style.display="none"
    
}
