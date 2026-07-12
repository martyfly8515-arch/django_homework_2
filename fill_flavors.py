from django.core.management.base import BaseCommand

from bboard.models import IceCreamSelection


class Command(BaseCommand):
    help = 'Заполняет поле-список сначала одной записью, затем циклом'

    def handle(self, *args, **options):
        selection, created = IceCreamSelection.objects.get_or_create(
            title='Набор мороженого'
        )

        selection.flavors = ['Пломбир']
        selection.save(update_fields=['flavors'])

        self.stdout.write(
            f'Добавлена одиночная запись: {selection.flavors}'
        )

        flavors = [
            'Эскимо',
            'Шоколадное',
            'Клубничное',
        ]

        for flavor in flavors:
            selection.flavors.append(flavor)

        selection.save(update_fields=['flavors'])

        self.stdout.write(
            self.style.SUCCESS(
                f'Итоговый список: {selection.flavors}'
            )
        )