const formPage = document.getElementById("main-container");
const otpPage = document.getElementById("otp-container");

otpPage.style.display = "none";


function openCloseLock(lock1, lock2, inputField){
    const lockIcon = document.querySelector(lock1);
    const lockIcon2 = document.querySelector(lock2);
    const passwordInput = document.querySelector(inputField);

    
    if (lockIcon){
        let open = false;
        function lockFunction() {
            lockIcon.classList.toggle('active');
            lockIcon2.classList.toggle('active');

            open = !open;
            if(open){
                passwordInput.type = 'text';
            }
            else{
                passwordInput.type = 'password';
            }
        }
        lockIcon.addEventListener('click', lockFunction);
        lockIcon2.addEventListener('click', lockFunction);
    }
}

openCloseLock('.lock', '.lock-2', '.password-a');
openCloseLock('.lock-b', '.lock-2-b', '.password-b');


document.getElementById('register').addEventListener('click', async function(event){
    const pattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    const nameInput = document.getElementById('name').value.trim();
    const surnameInput = document.getElementById('surname').value.trim();
    const emailInput = document.getElementById('email').value.trim();
    const password2Input = document.getElementById('password-input').value;
    const retypePasswordInput = document.getElementById('retype-password').value;
    
    let nameErrorMessage = document.getElementById('invalid-name');  
    let surnameErrorMessage = document.getElementById('invalid-surname');  
    let emailErrorMessage = document.getElementById('invalid-email');  
    let passwordErrorMessage = document.getElementById('invalid-password');
    let retypePasswordErrorMessage = document.getElementById('invalid-retype-password');  

    nameErrorMessage.textContent = "";
    surnameErrorMessage.textContent = "";
    emailErrorMessage.textContent = "";
    passwordErrorMessage.textContent = "";
    retypePasswordErrorMessage.textContent = "";

    let validEmail = true;
    let validPassword = true;
    let validName = true;
    let validSurname = true;
    let validRetypePassword = true;

    if(nameInput == ""){
        nameErrorMessage.textContent = "Invalid name. Name can't be empty";
        validName = false;
        event.preventDefault();
    }

    if(surnameInput == ""){
        surnameErrorMessage.textContent = "Invalid surname. Surname can't be empty";
        validSurname = false;
        event.preventDefault();
    }

    if(emailInput == ""){
        emailErrorMessage.textContent = "Invalid email. Email can't be empty";
        validEmail = false;
        event.preventDefault();
    }
    else{
        if(!pattern.test(emailInput)){
            emailErrorMessage.textContent = "Please enter a valid email address.";
            validEmail = false;
            event.preventDefault();
        }
    }

    if(password2Input == ""){
        passwordErrorMessage.textContent = "Invalid password. Password can't be empty";
        validPassword = false;
        event.preventDefault();
    }
    else{
        if(String(password2Input).length < 8){
            passwordErrorMessage.textContent = "Invalid password. Password should be 8 characters long";
            validPassword = false;
            event.preventDefault();
        }
    }

    if(retypePasswordInput == ""){
        retypePasswordErrorMessage.textContent = "Invalid password. Password can't be empty";
        validRetypePassword = false;
        event.preventDefault();
    }
    else{
        if(retypePasswordInput != password2Input){
            retypePasswordErrorMessage.textContent = "Password doesn't match";
            validRetypePassword = false;
            event.preventDefault();
        }
    } 
    

    if((validPassword && validEmail && validSurname && validName && validRetypePassword) || true){
        await fetch('http://127.0.0.1:5000/registration-form', {
            method: 'POST',
            body:JSON.stringify({
                name: nameInput,
                surname: surnameInput,
                email: emailInput,
                password: password2Input,
            }),
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then((data)=>{
            formPage.style.display = 'none'; 
            otpPage.style.display = "flex";
            
            document.getElementById("otp").addEventListener("click", async function(event){
                const codeInput = document.getElementById('text').value.trim();
                const invalidOtpMessage = document.getElementById("invalid-otp");
                invalidOtpMessage.textContent = "";
                let validOtp = true;

                if(codeInput == ""){
                    invalidOtpMessage.textContent = "Invalid OTP. OTP can't not be empty.";
                    validOtp = false;
                    event.preventDefault();
                }
                else{
                    if(codeInput != data.code){
                        invalidOtpMessage.textContent = "Invalid OTP. Please check the code.";
                        validOtp = false;
                        event.preventDefault();
                    }
                }

                if(validOtp){
                    await fetch("http://127.0.0.1:5000/otp-form", {
                        method: 'POST',
                        body:JSON.stringify({
                            email: emailInput,
                            code: codeInput
                        }),
                        headers: {
                            'Accept': 'application/json',
                            'Content-Type': 'application/json'
                        }
                    })
                    .then(response => response.json())
                    .then(data_json=>{
                        if(data_json.status == "200"){
                            window.location.href = ("home");
                        }
                    });
                }
            });
        });  
    }
});