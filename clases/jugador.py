
import random


class Jugador:
    def __init__(self,nombre):
        self.nombre = nombre
        self.salud = 50
        self.nivel = 1
        self.experiencia = 0


    def atacar(self):
       return  random.randint(10,20) * self.nivel
    


    def recibirDano(self,dano):

        self.salud -= dano

        if(self.salud <= 0):
            print(f"{self.nombre} ha muerto")
        else:
            print(f"Te quedan {self.salud} de vida")
        
    def ganarExperiencia(self, experiencia):
        print(f"{self.nombre} a ganado {experiencia} de experiencia")
        self.experiencia = self.experiencia + experiencia

        if self.experiencia > 100:
            self.nivel += 1
            self.experiencia = 0
            print(f"{self.nombre} subio de nivel a {self.nivel}")