# Automatizador Google Sheets

Este proyecto me ayuda a automatizar la actualización de una hoja de Google Sheets que uso para llevar el control de quién ha respondido un formulario de Google Forms.  
Así, no tengo que estar marcando manualmente cada contacto que respondió, el script lo hace por mí.

---

##  ¿Qué necesito antes de empezar?

- Tener Python 3 instalado (recomiendo 3.8 o superior)  
- Una cuenta de Google con acceso para crear proyectos en Google Cloud  
- Crear un proyecto en Google Cloud y activar estas APIs:  
  - Google Sheets API  
  - Google Drive API  
- Crear una **cuenta de servicio** en Google Cloud y descargar el archivo `service_account.json` con las credenciales  
- Darle permisos de editor a esa cuenta de servicio en la hoja de cálculo que usarás

---

## ⚙ Cómo configurar todo localmente

### 1. Guardar las credenciales

Guarda el archivo `service_account.json` en la raíz del proyecto.  
**Importante:** no subir este archivo a GitHub ni compartirlo.

### 2. Definir la variable de entorno para la credencial

Esto es para que el script lea el JSON de forma segura sin tener el archivo directamente.

Si usas **Windows PowerShell**, ejecuta:

```powershell
$env:GOOGLE_CREDENTIALS = Get-Content -Raw .\service_account.json
[Environment]::SetEnvironmentVariable("GOOGLE_CREDENTIALS", (Get-Content -Raw .\service_account.json), "User")



