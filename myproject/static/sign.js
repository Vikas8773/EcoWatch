// JavaScript to toggle between Login and Signup
function showLogin() {
  document.getElementById("login-form").classList.add("active");
  document.getElementById("signup-form").classList.remove("active");
  document.getElementById("login-toggle").classList.add("active");
  document.getElementById("signup-toggle").classList.remove("active");
}

function showSignup() {
  document.getElementById("signup-form").classList.add("active");
  document.getElementById("login-form").classList.remove("active");
  document.getElementById("signup-toggle").classList.add("active");
  document.getElementById("login-toggle").classList.remove("active");
}
