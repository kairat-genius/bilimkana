//(function($) {
//    $(document).ready(function() {
//        function translateText(text, targetLang, callback) {
//            const apiUrl = `https://translate.googleapis.com/translate_a/single?client=gtx&sl=ru&tl=${targetLang}&dt=t&q=${encodeURI(text)}`;
//            $.get(apiUrl, function(data) {
//                callback(data[0][0][0]);
//            });
//        }
//
//        function setupTranslation(field) {
//            const sourceLang = $(field).data('source-lang');
//            const targetFields = $(field).data('target-fields').split(',');
//
//            $(field).on('input', function() {
//                const text = $(this).val();
//                if (text) {
//                    targetFields.forEach(function(targetField) {
//                        const targetLang = $(targetField).data('target-lang');
//                        translateText(text, targetLang, function(translatedText) {
//                            $(targetField).val(translatedText);
//                        });
//                    });
//                }
//            });
//        }
//
//        $('[data-source-lang]').each(function() {
//            setupTranslation(this);
//        });
//    });
//})(django.jQuery);



(function($) {
    $(document).ready(function() {
        // Функция для перевода текста
        function translateText(text, targetLang, callback) {
            // Здесь должен быть ваш код отправки запроса на перевод
            // Пример:
            // const apiUrl = `https://translate.googleapis.com/translate_a/single?client=gtx&sl=ru&tl=${targetLang}&dt=t&q=${encodeURI(text)}`;
            // $.get(apiUrl, function(data) {
            //     callback(data[0][0][0]);
            // });

            // Примерный код для демонстрации
            // Вместо этого вызывайте ваш реальный API или сервис для перевода
            // и обновления значения поля targetField
            setTimeout(function() {
                // Возвращаем случайное значение в качестве перевода для демонстрации
                callback(text.toUpperCase()); // Замените на реальный результат перевода
            }, 500); // Имитация задержки запроса
        }

        // Функция для настройки автоматического перевода полей формы
        function setupTranslation(field) {
            const sourceLang = $(field).data('source-lang');
            const targetFields = $(field).data('target-fields').split(',');

            $(field).on('input', function() {
                const text = $(this).val();
                if (text) {
                    targetFields.forEach(function(targetField) {
                        const targetLang = $(targetField).data('target-lang');
                        translateText(text, targetLang, function(translatedText) {
                            $(targetField).val(translatedText);
                        });
                    });
                }
            });
        }

        // Настройка автоматического перевода для всех полей с атрибутом data-source-lang
        $('[data-source-lang]').each(function() {
            setupTranslation(this);
        });
    });
})(django.jQuery);