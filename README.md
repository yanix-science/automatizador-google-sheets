# Automatizador Google Sheets

Este proyecto automatiza la actualización de una hoja de Google Sheets para controlar quién ha respondido un formulario de Google Forms.  
Así, no tienes que marcar manualmente cada contacto que respondió: el script lo hace automáticamente.

---

## Requisitos previos

- Python 3 instalado (recomiendo versión 3.8 o superior)  
- Cuenta de Google con permisos para crear proyectos en Google Cloud  
- Proyecto en Google Cloud con las APIs activadas:  
  - Google Sheets API  
  - Google Drive API  
- Crear una **cuenta de servicio** en Google Cloud y descargar el archivo `service_account.json` con las credenciales  
- Compartir la hoja de cálculo con el email de la cuenta de servicio, otorgándole permisos de editor

---

## Configuración local

### Opción 1 (básica): Usar archivo `service_account.json` directamente

1. Coloca el archivo `service_account.json` en la raíz del proyecto.  
2. **Importante:** No subir este archivo a GitHub ni compartirlo públicamente.  
3. Instala las dependencias:  
   ```bash
   pip install -r requirements.txt

### Opción 2 (recomendada): Usar variable de entorno para las credenciales (más segura)
Esta opción evita tener el archivo JSON en el proyecto, previniendo fugas accidentales de las credenciales.

Cada desarrollador debe hacer esto en su propia máquina para que el script pueda autenticarse correctamente sin el archivo físico.

En Windows PowerShell:
Desde la carpeta donde esté el archivo service_account.json, ejecuta:

$env:GOOGLE_CREDENTIALS = Get-Content -Raw .\service_account.json
[Environment]::SetEnvironmentVariable("GOOGLE_CREDENTIALS", (Get-Content -Raw .\service_account.json), "User")

