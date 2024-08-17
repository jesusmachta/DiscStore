class Staff():
    def __init__(self, cedula):
        
        self.cedula = cedula
    
    def show_attr(self):
        print(f"""
                Cedula: {self.cedula}
                """)