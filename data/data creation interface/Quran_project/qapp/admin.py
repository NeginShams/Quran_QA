from django.contrib import admin

# Register your models here.
from .models import QuestionData, FactoidQuestion, NonFactoidQuestion, FactoidDone, AutomaticQuestion, MultipleAutomatic, QUQAComplete, QUQA, QaraatiFirst, QaraatiSecond, QaraatiThird, RuleBased

admin.site.register(QuestionData)
admin.site.register(FactoidQuestion)
admin.site.register(NonFactoidQuestion)
admin.site.register(FactoidDone)
admin.site.register(AutomaticQuestion)
admin.site.register(MultipleAutomatic)
admin.site.register(QUQAComplete)
admin.site.register(QUQA)
admin.site.register(QaraatiFirst)
admin.site.register(QaraatiSecond)
admin.site.register(QaraatiThird)
admin.site.register(RuleBased)