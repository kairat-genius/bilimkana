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



const translate = require('google-translate-free');

(function($) {
    $(document).ready(function() {
        // Функция для перевода текста через google-translate-free
        function translateText(text, targetLang, callback) {
            translate(text, { to: targetLang }).then(response => {
                callback(response.text);
            }).catch(error => {
                console.error('Error translating text:', error);
            });
        }

        // Остальной код остается таким же
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

        $('[data-source-lang]').each(function() {
            setupTranslation(this);
        });
    });
})(django.jQuery);