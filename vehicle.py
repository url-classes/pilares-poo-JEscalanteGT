class Vehicle:
    def __init__(self,
                 model: int,
                 engine: str,
                 oil_type: str):
        self.model = model
        self.engine = engine
        self.oil_type = oil_type

    @staticmethod
    def change_oil():
        print('Estoy cambiando el aceite')

