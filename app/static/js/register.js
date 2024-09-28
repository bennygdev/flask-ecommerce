const setError = (element, message) => {
  const errorDiv = document.getElementById(`${element.id}Error`);
  errorDiv.textContent = message;
};

const clearError = (element) => {
  const errorDiv = document.getElementById(`${element.id}Error`);
  errorDiv.textContent = '';
};

const validateStep1 = () => {
  let isValid = true;

  // get user inpout
  const firstName = document.getElementById('firstName');
  const lastName = document.getElementById('lastName');
  const email = document.getElementById('email');
  const password = document.getElementById('password');
  const confirmPassword = document.getElementById('confirmPassword');

  // first name
  if (firstName.value.trim() === '') {
    setError(firstName, 'First name is required');
    isValid = false;
  } else {
    clearError(firstName);
  }

  // last Name
  if (lastName.value.trim() === '') {
    setError(lastName, 'Last name is required');
    isValid = false;
  } else {
    clearError(lastName);
  }

  // email
  if (email.value.trim() === '') {
    setError(email, 'Email is required');
    isValid = false;
  } else if (!/\S+@\S+\.\S+/.test(email.value.trim())) {
    setError(email, 'Email is invalid');
    isValid = false;
  } else {
    clearError(email);
  }

  // passwrd
  if (password.value.trim() === '') {
    setError(password, 'Password is required');
    isValid = false;
  } else if (password.value.length < 6) {
    setError(password, 'Password must be at least 6 characters');
    isValid = false;
  } else {
    clearError(password);
  }

  // confirm password
  if (confirmPassword.value.trim() === '') {
    setError(confirmPassword, 'Confirm Password is required');
    isValid = false;
  } else if (confirmPassword.value !== password.value) {
    setError(confirmPassword, 'Passwords do not match');
    isValid = false;
  } else {
    clearError(confirmPassword);
  }

  return isValid;
};

const validateStep2 = () => {
  let isValid = true;

  const username = document.getElementById('username');

  // username
  if (username.value.trim() === '') {
    setError(username, 'Username is required');
    isValid = false;
  } else {
    clearError(username);
  }

  return isValid;
};

document.getElementById('register__next').addEventListener('click', () => {
  if(validateStep1()) {
    const step1 = document.getElementById('step1');
    const step2 = document.getElementById('step2');

    step1.classList.add('slide-out');
    step1.addEventListener('animationend', () => {
      step1.classList.add('hidden');
      step1.classList.remove('slide-out');
      step2.classList.remove('hidden');
      step2.classList.add('slide-in');
    }, { once: true });
  }

  document.getElementById('register__submit').addEventListener('click', function(event) {
    // prevent submission
    event.preventDefault();

    if (validateStep2()) {
      document.querySelector('.register__form').submit();
    }
  });
});