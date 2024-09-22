
const eyeIcon = document.querySelector('.lock');
const eyeIcon2 = document.querySelector('.lock-2');
const password = document.getElementById('password-input');

if (eyeIcon){
    let open = false;

    function eyeFunction(){
        eyeIcon.classList.toggle('active');
        eyeIcon2.classList.toggle('activate');

        open = !open;
        
        if(open){
            password.type = 'text';
        }
        else{
            password.type = 'password';
        }
    }

    eyeIcon.addEventListener('click', eyeFunction);
    eyeIcon2.addEventListener('click', eyeFunction);
}


document.getElementById("login").addEventListener("click", async function(event){
    const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/; 
    const emailInput = document.getElementById('email').value.trim();
    const passwordInput = password.value.trim();
    const checkbox = document.querySelector(".checkbox").checked;
    let emailErrorMessage = document.getElementById("invalid-email");
    let passwordErrorMessage = document.getElementById('invalid-password');
    
    emailErrorMessage.textContent = "";
    passwordErrorMessage.textContent = "";
    
    let validEmail = true;
    let validPassword = true;
   
    if(emailInput == ""){
        emailErrorMessage.textContent = "Invalid email. Email can't be empty";
        validEmail = false;
        event.preventDefault();
    }
    else{
        if(!emailPattern.test(emailInput)){
            emailErrorMessage.textContent = "Invalid email. Please enter a valid email address.";
            validEmail = false;
            event.preventDefault();
        }
    }

    if(passwordInput == ""){
        passwordErrorMessage.textContent = "Invalid password. Password can't be empty.";
        validPassword = false;
        event.preventDefault();
    }
    else{
        if(String(passwordInput).length < 8){
            passwordErrorMessage.textContent = "Invalid password. Password should be 8 characters long";
            validPassword = false;
            event.preventDefault();
        }
    }
    
    // if(validEmail & validPassword){
    //     let response = await fetch("http://127.0.0.1:5000/login-form", {
    //         method: "POST",
    //         body: JSON.stringify({
    //             email: emailInput,
    //             password: passwordInput
    //         }),
    //         headers: {
    //             'Accept': 'application/json',
    //             'Content-Type': 'application/json'
    //         }
    //     })
    //     .then(response => response.json())
    //     .then(jsonData => {});
    // }

});