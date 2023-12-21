import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'common.settings')

from django import setup
setup()
from django.forms.models import model_to_dict

from phones.models import base, phone, storages, colors

# phone.Phone.objects.get(pk=2).colors.add(colors.PhoneColor.objects.get(color="r"))
# print(phone.Phone.objects.get(pk=2).storages.all())
# a: base.PhonePosition = base.PhonePosition.objects.all().first()

# a.article_id = 4
#
# a.save()

# qs = phone.Phone.objects.raw("""
# SELECT * FROM phones_phone
# LEFT JOIN phones_phone_storages ON phones_phone.id = phones_phone_storages.phone_id
# LEFT JOIN phones_phone_colors ON phones_phone.id = phones_phone_colors.phone_id
# """)
#
# phone = colors.PhoneColor.objects.select_related("phone").values()
#
# for obj in phone:
#     obj: colors.PhoneColor
#     print(obj)

with open("dump2.json", 'r') as f:
    contents = f.read()

with open("dump.json", "w", encoding="utf-8") as f:
    f.write(contents)
