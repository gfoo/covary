import random
import string

from celery import shared_task


@shared_task
def random_text(text_length=100, letters=string.ascii_letters+' '):
    return ''.join(random.choices(letters, k=text_length))
