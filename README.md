
# AntiChristian Control Bot

Este proyecto es un bot de Telegram diseñado para controlar y notificar cuándo un usuario específico,en este caso  Christian, ha utilizado mi cuenta UCI. Está implementado en Python utilizando la librería `telebot` y tiene características de acceso restringido para ciertos comandos.

## Características

- **Comando `/start`**: Da la bienvenida al usuario y le proporciona información básica sobre el propósito del bot.
- **Comando `/status`**: Muestra la última vez que Christian usó tu cuenta. Este comando está restringido a usuarios autorizados.
- **Acceso restringido**: Solo los usuarios autorizados pueden ejecutar ciertos comandos, como el de estado.

## Cómo funciona

1. **Autenticación de usuarios**: El bot verifica que el usuario esté en la lista de usuarios autorizados antes de permitirles ejecutar comandos sensibles.
2. **Monitorización de actividad**: Utiliza una clase externa (`SRNI`) para obtener la última conexión de Christian y mostrarla al usuario autorizado.
3. **Notificaciones**: El bot responde a comandos con mensajes personalizados, incluyendo información sobre el usuario que interactúa con él.

## Requisitos

- Python 3.x
- Librería `python-telegram-bot`
- Archivo `.env` que contenga la variable `TOKEN_BOT` con el token de tu bot de Telegram.

## Ejecución

1. Clona el repositorio y navega hasta la carpeta del proyecto.
2. Instala las dependencias necesarias:
   ```
   pip install -r requirements.txt
   ```
3. Crea un archivo `.env` con la siguiente estructura:
   ```
   TOKEN_BOT=tu_token_aqui
   ```
4. Ejecuta el bot:
   ```
   python main.py
   ```

