<!-- : Скрип для управления полем ввода даты-->

    document.addEventListener('DOMContentLoaded', function() {
      var today = new Date();
      var elems = document.querySelectorAll('.datepicker');
      var options = {
        format: 'dd.mm.yyyy', // Формат даты
        i18n: {
          cancel: 'Отмена', // Текст кнопки отмены на русском
          clear: 'Очистить', // Текст кнопки очистки на русском
          done: 'Готово', // Текст кнопки подтверждения на русском
          months:
          [
            'Январь',
            'Февраль',
            'Март',
            'Апрель',
            'Май',
            'Июнь',
            'Июль',
            'Август',
            'Сентябрь',
            'Октябрь',
            'Ноябрь',
            'Декабрь'
          ],
          monthsShort:
          [
            'Янв',
            'Фев',
            'Мар',
            'Апр',
            'Май',
            'Июн',
            'Июл',
            'Авг',
            'Сен',
            'Окт',
            'Ноя',
            'Дек'
          ],
          weekdays:
          [
            'Воскресенье',
            'Понедельник',
            'Вторник',
            'Среда',
            'Четверг',
            'Пятница',
            'Суббота'
          ],
          weekdaysAbbrev:
          [
            'Вс',
            'Пн',
            'Вт',
            'Ср',
            'Чт',
            'Пт',
            'Сб'
          ],
          weekdaysShort:
          [
            'Вс',
            'Пн',
            'Вт',
            'Ср',
            'Чт',
            'Пт',
            'Суб'
          ]
        },
        firstDay: 1, // Неделя начинается с понедельника
        maxDate: today
        // Другие настройки Date Picker здесь
      };
      var instances = M.Datepicker.init(elems, options);
    });