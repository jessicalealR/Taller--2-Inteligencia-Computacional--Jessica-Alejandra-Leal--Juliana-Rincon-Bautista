import tkinter as tk
from tkinter import ttk
import random

class Alimento(object):
    def __init__(self, nombre, caloria, proteina, hidratos, grasa, indiceglicemico, tipo):
        super(Alimento, self).__init__()
        self.nombre = nombre
        self.caloria = caloria
        self.proteina = proteina
        self.hidratos = hidratos
        self.grasa = grasa
        self.indiceglicemico = indiceglicemico
        self.tipo = tipo

    def mostrarAlimento(self):
        print("%s %s %s %s %s %s %s" % (self.nombre, self.caloria, self.proteina, self.hidratos, self.grasa, self.indiceglicemico, self.tipo))

Alimentos = []

class Perfil(object):
    def __init__(self, nombre, peso, altura, sexo):
        super(Perfil, self).__init__()
        self.nombre = nombre
        self.peso = peso
        self.altura = altura
        self.sexo = sexo
        self.alimentos = [] 

    def imc(self):
        return self.peso / pow(self.altura, 2)

perfiles = []

def cargaConocimientoAlimentos():
    try:
        with open('conocimiento', 'r') as file:
            for linea in file:
                alim = linea.strip().split('|')

                if not alim:
                    continue

                if len(alim) == 7:
                    Alimentos.append(Alimento(alim[0], alim[1], alim[2], alim[3], alim[4], alim[5], alim[6]))
                else:
                    print(f"Error: La línea '{linea}' no tiene la cantidad correcta de elementos.")

        print("Alimentos cargados:")
        for alimento in Alimentos:
            alimento.mostrarAlimento()

    except FileNotFoundError:
        print("Error: El archivo 'conocimiento' no se encuentra en el directorio actual.")

def cargaConocimientoPerfiles():
    try:
        with open('Perfiles', 'r') as file:
            for linea in file:
                per = linea.strip().split('|')

               
                if not per:
                    continue

                if len(per) == 4:
                    perfiles.append(Perfil(per[0], float(per[1]), float(per[2]), per[3]))
                else:
                    print(f"Error: La línea '{linea}' no tiene la cantidad correcta de elementos.")
    except FileNotFoundError:
        print("Error: El archivo 'Perfiles' no se encuentra en el directorio actual.")

def OAV():
    try:
        with open('OAV', 'w') as OAV, open('conocimiento', 'r') as file:
            OAV.write('Objeto               Atributo                        Valor\n')
            for linea in file:
                alim = linea.strip().split('|')
                OAV.write(f"Alimento   Nombre                  {alim[0]}\n")
                OAV.write(f"Alimento   Calorias                {alim[1]}\n")
                OAV.write(f"Alimento   Proteinas               {alim[2]}\n")
                OAV.write(f"Alimento   Carbohidratos           {alim[3]}\n")
                OAV.write(f"Alimento   Grasas                  {alim[4]}\n")
                OAV.write(f"Alimento   Indice Glicemico        {alim[5]}\n")
                OAV.write(f"Alimento   Tipo                    {alim[6]}\n")
                OAV.write('\n\n\n')
    except FileNotFoundError:
        print("Error: El archivo 'conocimiento' no se encuentra en el directorio actual.")

def Recordar(nombre, peso, altura, sexo):
    try:
        with open('Perfiles', 'a') as file:
            file.write('\n')
            file.write(f'{nombre}|{peso}|{altura}|{sexo}')
    except FileNotFoundError:
        print("Error: El archivo 'Perfiles' no se encuentra en el directorio actual.")

def pesoIdeal(sexo, altura):
    if 'hombre' in sexo:
        return (((altura * 100) - 150) * 0.75) + 50
    elif 'mujer' in sexo:
        return (((altura * 100) - 150) * 0.6) + 50

def Desconocido(nombre):
    for x in range(len(perfiles)):
        pass
        if nombre == perfiles[x].nombre:
            return perfiles[x]
        elif x == len(perfiles) and nombre != perfiles[x].nombre:
            return False

def alimento(dias, numerodia, semana, tipoalimento):
    diasl = int(dias) * 7
    reposteria = []
    pescados = []
    carnes_huevos = []
    frutas_verduras_cereales = []
    comidas_elaboradas = []
    frutas = []
    semillas = []
    for x in range(len(Alimentos)):
        pass
        if 'Dulces y Reposteria' in Alimentos[x].tipo:
            pass
            reposteria.append(Alimentos[x])
        if 'Pescados y Mariscos' in Alimentos[x].tipo:
            pass
            pescados.append(Alimentos[x])
        if 'Carnes y Derivados' in Alimentos[x].tipo or 'Huevos' in Alimentos[x].tipo:
            pass
            carnes_huevos.append(Alimentos[x])
        if ('Verduras y Legumbres' in Alimentos[x].tipo or 'Frutas' in Alimentos[x].tipo) or 'Cereales y Derivados' in Alimentos[x].tipo:
            pass
            frutas_verduras_cereales.append(Alimentos[x])
        if 'Comidas Elaboradas' in Alimentos[x].tipo:
            pass
            comidas_elaboradas.append(Alimentos[x])
        if 'Frutas' in Alimentos[x].tipo:
            pass
            frutas.append(Alimentos[x])
        if 'Semillas' in Alimentos[x].tipo:
            pass
            semillas.append(Alimentos[x])
    if tipoalimento == 'desayuno':
        pass
        return random.choice(frutas_verduras_cereales)
    elif tipoalimento == 'media mañana':
        return random.choice(semillas)
    elif tipoalimento == 'merienda':
        return random.choice(frutas)
    elif tipoalimento == 'cena':
        return random.choice(frutas_verduras_cereales)
    elif tipoalimento == 'comida':
        if numerodia <= (diasl / 2):
            return random.choice(carnes_huevos)
        else:
            return random.choice(pescados)

def actividad(caloriasdiarias):
    caloriasdiarias = caloriasdiarias * 1.55
    if caloriasdiarias < 1700:
        print("Nivel de actividad Bajo")
    elif caloriasdiarias > 1700 and caloriasdiarias < 2000:
        print("Nivel de actividad Moderado")
    elif caloriasdiarias > 2000:
        print("Nivel de actividad Alto")

def valoracion(perfil):
    resultados = "Valoración:"
    tipo_comida = {1: "Diario", 2: "Semanal", 3: "Mensual"}

    if perfil.alimentos is not None:
        for y in perfil.alimentos:
           
            if isinstance(y, Alimento):
                resultados += f"{tipo_comida[y.tipo]}: {y.nombre}\n"
            else:
            
                resultados += f"{tipo_comida[y.tipo]}: Nombre no disponible\n"
    else:
        resultados += "Error: No se encontraron alimentos en el perfil.\n"

    return resultados


def semana_interfaz(perfil):
    global ndia
    ndia = 0
    caloriasdiarias = 0
    resultados = ""

    resultados += f"{int(perfil.peso - pesoIdeal(perfil.sexo, perfil.altura))}\n"

    dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    tipo_comida = ['Desayuno', 'Media mañana', 'Comida', 'Merienda', 'Cena']

    if (perfil.imc() <= 18):
        for x in range(int(pesoIdeal(perfil.sexo, perfil.altura) - perfil.peso)):
            resultados += f"SEMANA {x + 1}\n"
            for z in range(len(dias)):
                resultados += f"{dias[z]}\n"
                for y in range(5):
                    ndia = ndia + 1
                    alim = alimento(pesoIdeal(perfil.sexo, perfil.altura) - perfil.peso, ndia, x, tipo_comida[y])
                    resultados += f"{tipo_comida[y]}: {alim.nombre}\n"
                resultados += "______________________________________________________________________________\n"
    else:
        for x in range(int(perfil.peso - pesoIdeal(perfil.sexo, perfil.altura))):
            resultados += f"SEMANA {x + 1}\n"
            
            for z in range(len(dias)):
                resultados += f"{dias[z]}\n"
                for y in range(5):
                    ndia = ndia + 1
                    alim = alimento(perfil.peso - pesoIdeal(perfil.sexo, perfil.altura), ndia, x, tipo_comida[y])
                    resultados += f"{tipo_comida[y]}: {alim.nombre}\n"
                    caloriasdiarias = caloriasdiarias + int(alim.caloria)
                actividad(caloriasdiarias)
                caloriasdiarias = 0

    return resultados

def dieta_interfaz(perfil):
    if perfil.imc() <= 18:
        resultados = f"""Tu peso es Bajo 
Ello quiere decir que tu peso {perfil.peso}kg es insuficiente del recomendado para tu estatura {perfil.altura}m debido a que tu índice de masa corporal es de {perfil.imc()}
por lo que deberías seguir un plan encaminado a obtener un peso apto para ti y una correcta nutrición.
Tu peso ideal debería ser {pesoIdeal(perfil.sexo, perfil.altura)}kg"""
    elif 18 < perfil.imc() <= 24.9:
        resultados = f"""En este momento te encuentras en una situacion de Peso Normal
Tu peso {perfil.peso}kg es adecuado u optimo para tu estatura {perfil.altura}m debido a que usted tiene un índice de masa corporal de {perfil.imc()}."""
    elif 25 <= perfil.imc() <= 26.9:
        resultados = f"""En este momento te encuentras en una situación de Sobrepeso I
Ello quiere decir que tu peso está por encima del recomendado para tu estatura {perfil.altura}m y debido a tu índice de masa corporal {perfil.imc()}. Accede cuanto antes a iniciar tu plan y verás qué sencillo te resulta.
Tu peso ideal debería ser {pesoIdeal(perfil.sexo, perfil.altura)}
por lo que estás pasado por {perfil.peso - pesoIdeal(perfil.sexo, perfil.altura)} kilos"""
    elif 27 <= perfil.imc() <= 29.9:
        resultados = f"""En este momento te encuentras en una situación de Sobrepeso II
Pre-obesidad. Ello quiere decir que tu peso {perfil.peso}kg está por encima del recomendado para tu estatura {perfil.altura}m tu índice de masa corporal es de {perfil.imc()}. Accede cuanto antes a iniciar tu plan y verás qué sencillo te resulta.
Tu peso ideal debería ser {pesoIdeal(perfil.sexo, perfil.altura)}kg por lo que estás pasado por {perfil.peso - pesoIdeal(perfil.sexo, perfil.altura)} kilos"""
    elif 30 <= perfil.imc() <= 34.9:
        resultados = f"""En este momento te encuentras en una situación de Obesidad Tipo I
Ello significa que tu peso {perfil.peso}kg está por encima del recomendado para tu estatura {perfil.altura}m debido a que usted tiene un índice de masa corporal de {perfil.imc()}, y que además tienes probabilidades de que vaya asociado todo ello a la aparición de patologías (colesterol, Triglicéridos, hipertensión, diabetes tipo II, etc). Por todo esto, accede a iniciar plan, y te ayudaremos a bajar de peso y mejorar tu salud.
Tu peso ideal debería ser {pesoIdeal(perfil.sexo, perfil.altura)}kg por lo que estás pasado por {perfil.peso - pesoIdeal(perfil.sexo, perfil.altura)} kilos"""
    elif 35 <= perfil.imc() <= 39.9:
        resultados = f"""En este momento te encuentras en una situación de Obesidad Tipo II
Ello significa que tu peso {perfil.peso}kg está por encima del recomendado para tu estatura {perfil.altura}m debido a que usted tiene un índice de masa corporal de {perfil.imc()}, y que además tienes probabilidades de que vaya asociado todo ello a la aparición de patologías (colesterol, Triglicéridos, hipertensión, diabetes tipo II, etc). Por todo esto, accede a iniciar plan, y te ayudaremos a bajar de peso y mejorar tu salud.
Tu peso ideal debería ser {pesoIdeal(perfil.sexo, perfil.altura)}kg por lo que estás pasado por {perfil.peso - pesoIdeal(perfil.sexo, perfil.altura)} kilos"""
    elif 40 <= perfil.imc() <= 49.9:
        resultados = f"""En este momento te encuentras en una situación de Obesidad Tipo III
Ello significa que tu peso {perfil.peso}kg está por encima del recomendado para tu estatura {perfil.altura}m debido a que usted tiene un índice de masa corporal de {perfil.imc()}, y que además tienes probabilidades de que vaya asociado todo ello a la aparición de patologías (colesterol, Triglicéridos, hipertensión, diabetes tipo II, etc). Por todo esto, accede a iniciar plan, y te ayudaremos a bajar de peso y mejorar tu salud.
Tu peso ideal debería ser {pesoIdeal(perfil.sexo, perfil.altura)}kg por lo que estás pasado por {perfil.peso - pesoIdeal(perfil.sexo, perfil.altura)} kilos"""
    elif perfil.imc() >= 50:
        resultados = f"""En este momento te encuentras en una situación de Obesidad Extrema
Ello significa que tu peso {perfil.peso}kg está por encima del recomendado para tu estatura {perfil.altura}m debido a que usted tiene un índice de masa corporal de {perfil.imc()}, y que además tienes probabilidades de que vaya asociado todo ello a la aparición de patologías (colesterol, Triglicéridos, hipertensión, diabetes tipo II, etc). Por todo esto, accede a iniciar plan, y te ayudaremos a bajar de peso y mejorar tu salud.
Tu peso ideal debería ser {pesoIdeal(perfil.sexo, perfil.altura)}kg por lo que estás pasado por {perfil.peso - pesoIdeal(perfil.sexo, perfil.altura)} kilos"""
    else:
        resultados = ""  
    return resultados


class NutriologApp:
    def __init__(self, root):
        self.root = root
        self.root.title("**Nutriologo**")

        self.nombre_var = tk.StringVar()
        self.peso_var = tk.DoubleVar()
        self.altura_var = tk.DoubleVar()
        self.sexo_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        
        style = ttk.Style()
        style.configure('TLabel', font=('Arial', 12))
        style.configure('TButton', font=('Arial', 12))

        ttk.Label(self.root, text="Nombre:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        ttk.Entry(self.root, textvariable=self.nombre_var).grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Peso (kg):").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        ttk.Entry(self.root, textvariable=self.peso_var).grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Altura (m):").grid(row=2, column=0, sticky="w", padx=10, pady=5)
        ttk.Entry(self.root, textvariable=self.altura_var).grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Sexo (hombre/mujer):").grid(row=3, column=0, sticky="w", padx=10, pady=5)
        ttk.Entry(self.root, textvariable=self.sexo_var).grid(row=3, column=1, padx=10, pady=5)

        ttk.Button(self.root, text="Calcular y Mostrar", command=self.mostrar_resultados).grid(row=4, column=0, columnspan=2, pady=10)

        self.resultados_label = ttk.Label(self.root, text="", wraplength=600, font=('Arial', 12))
        self.resultados_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def mostrar_resultados(self):
        nombre = self.nombre_var.get()
        peso = self.peso_var.get()
        altura = self.altura_var.get()
        sexo = self.sexo_var.get()
        perfil = Perfil(nombre, peso, altura, sexo)
        
        resultados_text = valoracion(perfil) + "\n\n" + dieta_interfaz(perfil)
        self.resultados_label.config(text=resultados_text)


if __name__ == "__main__":
    
    cargaConocimientoAlimentos()
    cargaConocimientoPerfiles()
    OAV()

    root = tk.Tk()
    app = NutriologApp(root)
    root.mainloop()
