# Automatizador Google Sheets

Este proyecto automatiza la actualización de estados de contacto en una hoja de Google Sheets, basándose en respuestas recibidas en un formulario de Google Forms.  
Ideal para equipos que manejan listas de contactos y quieren ahorrar tiempo marcando automáticamente quién respondió o no.

---

## ✅ Configuración local

### 1. Obtener credenciales

- Ve a [Google Cloud Console](https://console.cloud.google.com/)
- Crea un proyecto y habilita las APIs:
  - Google Sheets API
  - Google Drive API
- Crea una **cuenta de servicio**
- Asigna permisos de editor al correo de la cuenta de servicio sobre la hoja de cálculo
- Descarga el archivo `service_account.json`
- Guarda el archivo en la raíz del proyecto (⚠️ **No subir a GitHub**)

### 2. Establecer variable de entorno

#### En PowerShell (Windows)

```powershell
$env:GOOGLE_CREDENTIALS = Get-Content -Raw .\service_account.json
[Environment]::SetEnvironmentVariable("GOOGLE_CREDENTIALS", (Get-Content -Raw .\service_account.json), "User")
