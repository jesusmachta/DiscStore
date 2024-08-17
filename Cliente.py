class Cliente():
    def __init__(self, cedula, discos_comprados):

        self.cedula = cedula
        self.discos_comprados = discos_comprados
    
    def show_attr(self):
        print(f"""
                Cedula: {self.cedula}
                discos_comprados: {self.discos_comprados}
                """)