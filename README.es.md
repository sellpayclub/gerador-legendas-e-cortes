# Generador de Subtítulos y Clips

[Português](README.md) · [English](README.en.md) · Español

Aplicación de código abierto para transcribir videos, editar subtítulos, encontrar clips con IA y exportar archivos MP4. La interfaz admite portugués, inglés y español. El uso local no requiere cuenta, pago ni suscripción.

## Instalar con IA

Abre **[el prompt listo para Codex, Claude u otra IA](INSTALAR-CON-IA.md)** y cópialo en un asistente con acceso al terminal. Descargará, instalará, iniciará y comprobará la aplicación. Introduce tu clave OpenAI directamente en Configuración.

Los videos permanecen en la computadora donde se ejecuta la aplicación. La transcripción y otras funciones de IA usan tu propia clave de API de OpenAI, cuyo uso puede tener costo. FFmpeg renderiza los videos localmente.

## Instalación

Descarga el [ZIP del proyecto](https://github.com/sellpayclub/gerador-legendas-e-cortes/archive/refs/heads/main.zip) o clona el repositorio:

```bash
git clone https://github.com/sellpayclub/gerador-legendas-e-cortes.git
cd gerador-legendas-e-cortes
```

- **macOS:** instala [Homebrew](https://brew.sh), mueve la carpeta fuera de Escritorio/Documentos/Descargas y ejecuta `bash install.sh` en Terminal. Abre <http://localhost:3000>.
- **Windows 10/11:** extrae el ZIP y haz doble clic en `Instalar-Windows.cmd`. Utiliza `winget` para instalar Python, Node y FFmpeg si faltan. Después, abre la aplicación con `Iniciar-Windows.cmd`.
- **Ubuntu/VPS:** consulta el [manual de instalación en portugués](GUIA-INSTALACAO.md) para los detalles de publicación.

En **Configuración**, pega tu [clave de API OpenAI](https://platform.openai.com/api-keys), pulsa **Probar conexión** y guárdala. El proyecto no incluye una clave. En Mac con Apple Silicon, puedes instalar opcionalmente `mlx` para transcripción local; otras funciones de IA siguen requiriendo OpenAI.

Selecciona **Subtítulos** o **Clips**, sube un video, edita el resultado, renderiza y descarga el MP4. Cambia el idioma de la interfaz con el selector superior. El idioma de voz del video se selecciona por separado.

Se necesitan Python 3.11+, Node.js 22+ y FFmpeg con el filtro `ass`/libass. Los proyectos se guardan en `data/jobs/` y la clave local en `data/app-settings.json` o `backend/.env`; estos archivos no se suben al repositorio.

El instalador local solo usa `localhost`. Para acceder desde iPhone o Android, publica la aplicación en tu propio servidor HTTPS con protección de acceso adecuada. Consulta el [manual completo](GUIA-INSTALACAO.md) para uso, actualizaciones y solución de problemas.

El código del proyecto se distribuye bajo [MIT](LICENSE); los recursos y paquetes de terceros mantienen sus propias licencias.
