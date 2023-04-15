
  // Получаем ссылки на элементы input по их id
  var passwordInput = document.getElementById("password");
  var twoPasswordInput = document.getElementById("two_password");

  // Добавляем обработчик события на ввод данных в поле "Повторите пароль"
  twoPasswordInput.addEventListener('input', function() {
    // Получаем значения из обоих полей
    var passwordValue = passwordInput.value;
    var twoPasswordValue = twoPasswordInput.value;

    // Удаляем класс с подсветкой ошибки с обоих полей (если был ранее установлен)
    passwordInput.classList.remove('error');
    twoPasswordInput.classList.remove('error');

    // Сравниваем значения и проверяем длину паролей
    if (passwordValue === twoPasswordValue && passwordValue.length >= 6) {
      // Если значения совпадают и длина паролей >= 6 символов, можно выполнить дополнительные действия
      console.log('Пароли валидны');
      // Например, можно разрешить отправку формы или выполнить другие действия
    } else {
      // Если значения не совпадают или длина паролей < 6 символов, добавляем класс с подсветкой ошибки на оба поля
      console.log('Пароли не валидны');
      passwordInput.classList.add('error');
      twoPasswordInput.classList.add('error');
    }
  });