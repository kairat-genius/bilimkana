document.addEventListener('DOMContentLoaded', function() {
    const translations = [
        { mainFieldId: 'id_answer_ru', targetFieldIds: ['id_answer_en', 'id_answer_ky'] },
        { mainFieldId: 'id_question_ru', targetFieldIds: ['id_question_en', 'id_question_ky'] },
        { mainFieldId: 'id_title_ru', targetFieldIds: ['id_title_en', 'id_title_ky'] },
        { mainFieldId: 'id_full_name_ru', targetFieldIds: ['id_full_name_en', 'id_full_name_ky'] },
        { mainFieldId: 'id_speciality_ru', targetFieldIds: ['id_speciality_en', 'id_speciality_ky'] },
        { mainFieldId: 'id_education_ru', targetFieldIds: ['id_education_en', 'id_education_ky'], isCKEditor: true },
        { mainFieldId: 'id_description_ru', targetFieldIds: ['id_description_en', 'id_description_ky'], isCKEditor: true }
    ];

    translations.forEach(translation => {
        setupTranslation(translation.mainFieldId, translation.targetFieldIds, '/api/translate/', translation.isCKEditor);
    });
});

function setupTranslation(mainFieldId, targetFieldIds, url, isCKEditor = false) {
    if (isCKEditor) {
        CKEDITOR.on('instanceReady', function(event) {
            const mainField = CKEDITOR.instances[mainFieldId];
            const targetFields = targetFieldIds.map(id => CKEDITOR.instances[id]);
            addChangeListener(mainField, targetFields, url, isCKEditor);
        });
    } else {
        const mainField = document.getElementById(mainFieldId);
        const targetFields = targetFieldIds.map(id => document.getElementById(id));
        addChangeListener(mainField, targetFields, url, isCKEditor);
    }
}

function addChangeListener(mainField, targetFields, url, isCKEditor) {
    let timer = null;

    if (mainField && targetFields.every(field => field !== null)) {
        const eventListener = function() {
            clearTimeout(timer);

            timer = setTimeout(() => {
                const textToTranslate = isCKEditor ? mainField.getData().trim() : mainField.value.trim();

                if (textToTranslate) {
                    fetch(url, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': getCookie('csrftoken')
                        },
                        body: JSON.stringify({
                            text_to_translate: textToTranslate,
                            target_language: ['en', 'ky']
                        })
                    })
                    .then(response => response.json())
                    .then(data => {
                        if (data && data.translated_text) {
                            if (isCKEditor) {
                                targetFields[0].setData(data.translated_text[0]);
                                targetFields[1].setData(data.translated_text[1]);
                            } else {
                                targetFields[0].value = data.translated_text[0];
                                targetFields[1].value = data.translated_text[1];
                            }
                        }
                    })
                    .catch(error => {
                        console.error('Error:', error);
                    });
                }
            }, 500);
        };

        if (isCKEditor) {
            mainField.on('change', eventListener);
        } else {
            mainField.addEventListener('input', eventListener);
        }
    }
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}