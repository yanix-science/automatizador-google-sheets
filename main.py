import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
import json
import os 
from google.oauth2.service_account import Credentials

# Ruta del archivo JSON con credenciales para Google API
RUTA_CREDENCIALES = 'service_account.json'

# Nombres de la hoja de cálculo y pestañas en Google Sheets
NOMBRE_HOJA_GOOGLE = 'Automatizador'
NOMBRE_PESTAÑA_DATOS = 'Automatizador'
NOMBRE_PESTAÑA_RESPUESTAS = 'Form Responses 1'


def google_sheet_client():
    """
    Crea y retorna un cliente autorizado para manipular Google Sheets
    usando credenciales desde variable de entorno segura.

    Returns:
        gspread.Client: Cliente autorizado para Google Sheets.
    """
    credentials_info = json.loads(os.getenv('GOOGLE_CREDENTIALS'))

    # Crear credenciales con acceso completo a Google Sheets y Drive
    scopes = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
    credentials = Credentials.from_service_account_info(credentials_info, scopes=scopes)

    # Cliente de gspread
    cliente = gspread.authorize(credentials)
    print("✅ Conexión con Google Sheets establecida.")
    return cliente



def abrir_hoja_por_nombre(cliente, nombre_hoja):
    """
    Abre y retorna una hoja de cálculo de Google Sheets por su nombre.

    Args:
        cliente (gspread.Client): Cliente autorizado de Google Sheets.
        nombre_hoja (str): Nombre de la hoja de cálculo a abrir.

    Returns:
        gspread.Spreadsheet: Objeto hoja de cálculo abierta.
    """
    hoja = cliente.open(nombre_hoja)
    print(f"📄 Hoja abierta: {hoja.title}")
    return hoja


def marcar_contactados(hoja):
    """
    Actualiza la columna "Contactado" y registra la fecha en que
    fue marcado como contactado en la hoja de datos, según las respuestas
    recibidas en el formulario.

    En caso de que un contacto haya respondido, marca "Sí" y añade la fecha
    actual en la columna "Fecha Contactado". Si no respondió, marca "No" y
    limpia la fecha para evitar datos incorrectos.

    Args:
        hoja (gspread.Spreadsheet): Objeto hoja de cálculo abierta.
    """
    # Abrimos las pestañas de datos y respuestas
    pestaña_datos = hoja.worksheet(NOMBRE_PESTAÑA_DATOS)
    pestaña_respuestas = hoja.worksheet(NOMBRE_PESTAÑA_RESPUESTAS)

    # Obtenemos todos los registros como listas de diccionarios
    datos = pestaña_datos.get_all_records()
    respuestas = pestaña_respuestas.get_all_records()

    # Creamos un conjunto con correos electrónicos que respondieron el formulario
    correos_respondidos = {fila["Email"].strip().lower() for fila in respuestas}

    actualizados = 0
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d")  # Fecha en formato YYYY-MM-DD

    # Columnas que actualizaremos (1-based indexing)
    col_contactado = 4        # Columna "Contactado"
    col_fecha_contactado = 5  # Columna "Fecha Contactado" (debe existir en la hoja)

    # Iteramos sobre cada fila de los datos para actualizar su estado
    for i, fila in enumerate(datos):
        email = fila.get("Email", "").strip().lower()
        fila_num = i + 2  # Ajuste porque la fila 1 tiene encabezados

        if email in correos_respondidos:
            # Si respondió, marcar "Sí" y poner fecha actual
            pestaña_datos.update_cell(fila_num, col_contactado, "Sí")
            pestaña_datos.update_cell(fila_num, col_fecha_contactado, fecha_actual)
            print(f"✅ Respondió: {fila['Nombre']} ({email})")
            actualizados += 1
        else:
            # Si no respondió, marcar "No" y limpiar la fecha
            pestaña_datos.update_cell(fila_num, col_contactado, "No")
            pestaña_datos.update_cell(fila_num, col_fecha_contactado, "")
            print(f"❌ No ha respondido: {fila['Nombre']} ({email})")

    print(f"\n🔄 Proceso completado. {actualizados} contactos marcados como 'Sí'.")


def main():
    """
    Función principal que establece conexión con Google Sheets,
    abre la hoja y ejecuta la función para marcar contactos.
    """
    cliente = google_sheet_client()
    hoja = abrir_hoja_por_nombre(cliente, NOMBRE_HOJA_GOOGLE)
    marcar_contactados(hoja)


if __name__ == "__main__":
    main()
