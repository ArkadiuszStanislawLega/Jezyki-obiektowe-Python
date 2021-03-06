from models.mechanical_service import MechanicalService


class MechanicalWashWheels(MechanicalService):
    def __init__(self):
        super().__init__()
        self._is_paid = False
        self._name = f'{super().name} - czyszczenie kół'

    def clean(self):
        if self._is_paid:
            super().clean()
            print(f'Wykonuje {self._name}')
        else:
            print(f'Usługa {self._name} nie jest opłacona.')
