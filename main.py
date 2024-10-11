import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style, init

# Cabecera chula con ASCII
header = f"""
{Fore.CYAN}

  _______                                   ______ 
 |     __|.----..----..---.-..-----..-----.|__    |.----. 
 |__     ||  __||   _||  _  ||  _  ||  _  ||__    ||   _| 
 |_______||____||__|  |___._||   __||   __||______||__| 
                             |__|   |__|
                                            BY All3_s3c
"""
print(header)

# Inicializa colorama
init(autoreset=True)

def main():
    # Solicitar al usuario que introduzca la URL y la etiqueta a buscar
    url = input(Fore.YELLOW + "Introduce la URL de la página web: " + Style.RESET_ALL)
    tag = input(Fore.YELLOW + "Introduce la etiqueta a buscar (por ejemplo, 'span'): " + Style.RESET_ALL)

    # Realizar la solicitud HTTP GET
    response = requests.get(url)

    # Verificar que la solicitud fue exitosa
    if response.status_code == 200:
        # Analizar el contenido HTML de la página
        soup = BeautifulSoup(response.content, 'html.parser')

        # Obtener todos los textos que están dentro de la etiqueta especificada
        elements = soup.find_all(tag)

        print(Fore.CYAN + f"Buscando nombres....")
        # Verificar si se encontraron elementos
        if elements:
            # Extraer el texto de cada etiqueta y almacenarlo en una lista
            elements_list = [element.get_text().strip() for element in elements]

            # Imprimir los nombres encontrados
            for element_text in elements_list:
                print(Fore.GREEN + element_text + Style.RESET_ALL)
        else:
            print(Fore.RED + f"No se encontraron etiquetas '{tag}' en la página." + Style.RESET_ALL)
    else:
        print(Fore.RED + f"Error al acceder a la página: {response.status_code}" + Style.RESET_ALL)

if __name__ == "__main__":
    main()

