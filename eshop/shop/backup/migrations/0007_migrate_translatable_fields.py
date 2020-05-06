from django.db import migrations
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist


def forwards_func(apps, schema_editor):
    MyModel = apps.get_model('shop', 'Category')
    MyModelTranslation = apps.get_model('shop', 'MyModelTranslation')

    for object in MyModel.objects.all():
        MyModelTranslation.objects.create(
            master_id=object.pk,
            language_code=settings.LANGUAGE_CODE,
            name=object.name
        )

def backwards_func(apps, schema_editor):
    MyModel = apps.get_model('shop', 'Category')
    MyModelTranslation = apps.get_model('shop', 'MyModelTranslation')

    for object in MyModel.objects.all():
        translation = _get_translation(object, MyModelTranslation)
        object.name = translation.name
        object.save()   # Note this only calls Model.save()

def _get_translation(object, MyModelTranslation):
    translations = MyModelTranslation.objects.filter(master_id=object.pk)
    try:
        # Try default translation
        return translations.get(language_code=settings.LANGUAGE_CODE)
    except ObjectDoesNotExist:
        try:
            # Try default language
            return translations.get(language_code=settings.PARLER_DEFAULT_LANGUAGE_CODE)
        except ObjectDoesNotExist:
            # Maybe the object was translated only in a specific language?
            # Hope there is a single translation
            return translations.get()


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_add_translation_model'),
    ]

    operations = [
        migrations.RunPython(forwards_func, backwards_func),
    ]