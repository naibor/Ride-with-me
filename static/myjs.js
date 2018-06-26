// signup modal
var signUpModal = document.getElementById("signupmodal");
// login modal
var logInModal = document.getElementById("loginmodal");
// signup button
var signup = document.getElementById("SignUp");
// login button
var login = document.getElementById("LogIn");
// close signup icon
var closesignup = document.getElementById("closesignUp");
// close login icon
var closelogin =document.getElementById("closeLogIn");
var sidenav = document.getElementById("sidemodal");
var details = document.getElementById("requestdetails");
var UserSideNav =document.getElementById("UsersideModal");
var ridedetails = document.getElementById("requestride");
// tables
var tablerequests = document.getElementById("requesttable");
var availablerides = document.getElementById("ridestable");
var Historytable = document.getElementById("driverhistory");
var Userhistory = document.getElementById("userhistory");
// Index page
// signing up 
signup.onclick = function() {
    signUpModal.style.display="block";
    logInModal.style.display="none";
}

// closing signup form modal
closesignup.onclick = function(){
    signUpModal.style.display="none";
}

// when user clicks anywhere outside modal
window.onclick = function(event){
    if(event.target == signUpModal){
        signUpModal.style.display="none";
    }
}

// login modal form
login.onclick=function(){
    logInModal.style.display="block";
    signUpModal.style.display="none";
}


// closing login form modal
closelogin.onclick=function(){
    logInModal.style.display="none";
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
function close(){
    details.style.display="none";
    
} 
// close side nav driver  
function closeMenu(){
    sidenav.style.display="none";
}

// user sidenav
// open side nav 
function Openside(){
    UserSideNav.style.display="flex";
    ridedetails.style.display="none";
}
// close user side nav
function closeside(){
    UserSideNav.style.display="none";
}

// open ride request
function Openride(){
    ridedetails.style.display="block";
    UserSideNav.style.display="none";
}
// closing ride request
function closeride(){
    ridedetails.style.display="none";
}

// open table requests
function Openrequests(){
    tablerequests.style.display="block"
}

// close table requests
function closetable(){
    tablerequests.style.display="none";
    ridedetails.style.display="none";
}
// open available rides
function OpenRides(){
    availablerides.style.display="block";
    ridedetails.style.display="none";  

}
// close available rides
function closeRides(){
    availablerides.style.display="none";
    
}

// open history driver
function openhistory(){
    Historytable.style.display = "block";
}

// close history driver
function closehistory(){
    Historytable.style.display = "none"; 
}

// open user history
function openHistory(){
    Userhistory.style.display = "block";
}

// close user history
function closeHistory(){
    Userhistory.style.display = "none";
}