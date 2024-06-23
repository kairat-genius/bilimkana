from django.db import models
from parler.models import TranslatableModel, TranslatedFields

class FAQ(TranslatableModel):
    """F.A.Q. — «Frequently Asked Questions», «часто задаваемые вопросы»."""
    translations = TranslatedFields(
        question=models.TextField(),
        answer=models.TextField(),
    )

    def __str__(self):
        return self.safe_translation_getter('question', any_language=True)