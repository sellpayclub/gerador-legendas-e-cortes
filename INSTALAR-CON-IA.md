# Instalar con una IA

Copia este texto en Codex, Claude u otro asistente que pueda ejecutar comandos en tu computadora. De forma predeterminada, la aplicación se abre localmente en <http://localhost:3000>.

```text
Instala e inicia en mi computadora el proyecto abierto Generador de Subtítulos y Clips.
Repositorio oficial: https://github.com/sellpayclub/gerador-legendas-e-cortes
Manual: https://github.com/sellpayclub/gerador-legendas-e-cortes/blob/main/GUIA-INSTALACAO.md

Puedes descargar el repositorio, instalar las dependencias, ejecutar el instalador, iniciar los servicios locales y verificar la instalación. Completa los pasos que puedes hacer desde el terminal.

Detecta mi sistema operativo y arquitectura. Guarda el proyecto en una carpeta permanente dentro de mi directorio personal; en macOS, evita Escritorio/Documentos/Descargas. Si ya existe una copia, conserva proyectos, ajustes, secretos y cambios locales. No borres ni restablezcas la copia existente. Lee primero el README y el manual. Si no hay Git, descarga el ZIP oficial de GitHub.

En macOS ejecuta `bash install.sh`. En Windows 10/11 ejecuta `Instalar-Windows.cmd` o `scripts/install-windows.ps1` en PowerShell. En Ubuntu con dominio, sigue el manual y ejecuta `sudo bash install.sh`. No intentes instalar el backend de forma nativa en un iPhone; en iPhone se usa el navegador cuando el servidor está publicado con HTTPS.

Verifica que `http://127.0.0.1:8000/api/health` devuelva `ok: true` y `ffmpeg_ok: true`, que `http://localhost:3000` abra y que `/checkout` no exista. Consulta los registros y corrige cualquier fallo. Comprueba el inicio automático en macOS/Windows.

Abre `http://localhost:3000/configuracoes` para que introduzca mi propia clave OpenAI directamente en la aplicación, la pruebe y la guarde. No me pidas la clave en el chat ni la subas a Git. El uso de la API de OpenAI puede tener costo.

Al terminar, indícame la URL, la carpeta de instalación, las verificaciones realizadas y cualquier paso que aún me corresponda. No afirmes haber probado sistemas o dispositivos a los que no tuviste acceso. Si no tienes acceso al terminal, dilo y proporciona los comandos exactos para mi sistema. Mantén el servidor en localhost a menos que te proporcione un dominio y elija protección de acceso.
```
