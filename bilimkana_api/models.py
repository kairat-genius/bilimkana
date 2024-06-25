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

class News(TranslatableModel):
    image = models.ImageField()
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        text=models.TextField(),
    )

    def __str__(self):
        return self.safe_translation_getter('title,text', any_language=True)
class Events(TranslatableModel):
    image = models.ImageField()
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        text=models.TextField(),
    )

    def __str__(self):
        return self.safe_translation_getter('title,text', any_language=True)