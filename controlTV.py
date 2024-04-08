import socket
import pyinputplus as pyip
import os

def start_client():
    while True:
        host = "192.168.1.240" 
        port = 1515  
        pyip.inputStr(prompt='Presione tecla para iniciar conexion:')
    
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            client_socket.connect((host, port))
            menu(client_socket)
        except ConnectionRefusedError:
            print(f'Error: No se puede conectar al servidor en {host}:{port}')
        finally:
            client_socket.close()
            print('Conexión cerrada')

def enviar_comando(client_socket, comando):
    client_socket.sendall(bytes.fromhex(comando))

def menu(client_socket):
    while True:
        print("Selecciona una opción:")
        print("1. Encender")
        print("2. Apagar")
        print("0. Finalizar")
        try:
            opcion = int(pyip.inputInt("Ingresa el número de la opción deseada: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if opcion == 1:
            enviar_comando(client_socket, "AA11FE010111") 
            os.system("cls")
        elif opcion == 2:
            enviar_comando(client_socket, "AA11FE010010")
            os.system("cls")
        elif opcion == 0:
            print("Saliendo del programa. ¡Hasta luego!") 
            break
        else:
            print("Opción no válida. Por favor, ingresa un número válido.")

if __name__ == "__main__":
    start_client()
    # pyinstaller --onefile controlTV.py

