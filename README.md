# Automatizador de Google Sheets

Este proyecto automatiza la actualización de una hoja de Google Sheets para llevar un control automático de quién ha respondido un formulario de Google Forms. Evita marcar manualmente los contactos, mejorando la productividad y precisión.


---

## Requisitos previos

Para empezar, asegúrate de tener lo siguiente:

- **Python 3** (versión 3.8 o superior recomendada).  
- Una **cuenta de Google** con permisos para crear proyectos en Google Cloud.  
- Un **proyecto en Google Cloud** con las siguientes APIs activadas:  
  - Google Sheets API  
  - Google Drive API  
- Una **cuenta de servicio de Google Cloud** con el archivo de credenciales `service_account.json` descargado.  
- La hoja de cálculo de Google compartida con el correo electrónico de tu cuenta de servicio, otorgándole permisos de **editor**.

---

## Configuración local

Tienes dos opciones para configurar tus credenciales:

### Opción 1 (Básica): Usar `service_account.json` directamente

Esta es la forma más rápida de empezar.

1. Coloca el archivo `service_account.json` en la raíz de tu proyecto.  
2. **Importante:** No subas este archivo a GitHub ni lo compartas públicamente.
3. > **Recomendación:** Para evitar conflictos con otras librerías, se recomienda usar un entorno virtual de Python:

```bash
python -m venv venv
source venv/Scripts/activate   # Windows
source venv/bin/activate       # Linux/macOS
pip install -r requirements.txt
```
5. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

6. Ejecuta el script:

    ```bash
    python main.py
    ```

### Opción 2 (Recomendada): Usar una variable de entorno para las credenciales

Esta opción es más segura, ya que evita que el archivo JSON esté directamente en tu proyecto, reduciendo el riesgo de filtraciones accidentales de credenciales. Cada desarrollador debería configurarlo en su propia máquina.

#### En Windows PowerShell:

Desde la carpeta donde se encuentra tu archivo `service_account.json`, ejecuta:

```powershell
# Temporal para la sesión actual
$env:GOOGLE_CREDENTIALS = Get-Content -Raw .\service_account.json

# Para hacer la variable permanente (solo una vez)
[Environment]::SetEnvironmentVariable("GOOGLE_CREDENTIALS", (Get-Content -Raw .\service_account.json), "User")

```
### Seguridad y buenas prácticas:
No subas nunca el archivo service_account.json a repositorios públicos.

1. Usa la variable de entorno para proteger tus credenciales y evitar filtraciones.

2. Cada colaborador debe configurar sus propias credenciales y variables de entorno localmente.

3. En tu .gitignore debes asegurarte de ignorar el archivo service_account.json para evitar subirlo accidentalmente.

## Preguntas frecuentes

**¿Qué hago si obtengo error de autorización?**

- Verifica que la hoja esté compartida con el correo de la cuenta de servicio.
- Asegúrate de que la variable de entorno `GOOGLE_CREDENTIALS` esté correctamente configurada.
- Revisa que las APIs estén activadas en Google Cloud Console.

**¿Puedo usar este script sin variable de entorno?**

Sí, pero solo en entornos locales y temporales. La variable de entorno es más segura para producción y colaboración.
