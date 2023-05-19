from multiprocessing import Process

ruta_script = "main.py"

def ejecutar_script():
    exec(open(ruta_script).read())

if __name__ == "__main__":
    # Crea un nuevo proceso para ejecutar el script en segundo plano
    proceso = Process(target=ejecutar_script)
    proceso.start()