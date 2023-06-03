from django.forms import ModelForm, Textarea, TextInput, FileInput, EmailInput, PasswordInput, Select
# Напишите Form для приема данных для наших моделей 


# Создайте формы для каждой модели и добавите их в компоненты формы


# HTML                      forms.py                models.py
# -----------------------------------------------------------------------------
# input type="text"         = TextInput             = CharField
# input type="password"     = PasswordInput         = CharField
# input type="email"        = EmailInput            = EmailField
# input type="file"         = FileInput             = ImageField or FileField
# textarea                  = Textarea              = TextField
# select                    = Select                = ForeignKeyField
# input type="checkbox"    = CheckboxInput          = BooleanField