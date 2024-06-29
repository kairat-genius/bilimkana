document.addEventListener('DOMContentLoaded', function() {
    const translations = [
        { mainFieldId: 'id_answer_ru', targetFieldIds: ['id_answer_en', 'id_answer_ky'] },
        { mainFieldId: 'id_question_ru', targetFieldIds: ['id_question_en', 'id_question_ky'] },
        { mainFieldId: 'id_title_ru', targetFieldIds: ['id_title_en', 'id_title_ky'] },
        { mainFieldId: 'id_name_ru', targetFieldIds: ['id_name_en', 'id_name_ky'] },
        { mainFieldId: 'id_speciality_ru', targetFieldIds: ['id_speciality_en', 'id_speciality_ky'] },
        { mainFieldId: 'id_education_ru', targetFieldIds: ['id_education_en', 'id_education_ky'] },
        { mainFieldId: 'id_description_ru', targetFieldIds: ['id_description_en', 'id_description_ky'] },

    ];
    translations.forEach(translation => {
        setupTranslation(translation.mainFieldId, translation.targetFieldIds, '/translate/');
    });
});


function setupTranslation(mainFieldId, targetFieldIds, url) {
    const mainField = document.getElementById(mainFieldId);
    const targetFields = targetFieldIds.map(id => document.getElementById(id));
    let timer = null;

    if (mainField && targetFields.every(field => field !== null)) {
        mainField.addEventListener('input', function() {
            clearTimeout(timer);

            timer = setTimeout(() => {
                const textToTranslate = mainField.value.trim();

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
                            targetFields[0].value = data.translated_text[0];
                            targetFields[1].value = data.translated_text[1];
                        }
                    })
                    .catch(error => {
                        console.error('Error:', error);
                    });
                }
            }, 500);
        });
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