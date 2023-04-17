 // Получаем ссылки на элементы input по их id
  passwordInput.addEventListener('input', function() {

  var passwordInput = document.getElementById("password");

  var passwordValue = passwordInput.value;
  passwordInput.classList.remove('error');
  if (passwordValue.length >= 6) {
  console.log('Пароль валиден');
  } else {
  console.log('Длинна пароля должна быть больше 6 символов');
  passwordInput.classList.add('error');
  }
  }
  );