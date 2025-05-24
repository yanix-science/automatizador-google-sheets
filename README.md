# Automatizador Google Sheets

Este proyecto automatiza la marcación de usuarios contactados en una hoja de cálculo de Google Sheets, verificando si han respondido a un formulario de Google Forms.

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
