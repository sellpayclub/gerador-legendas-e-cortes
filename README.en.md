# Subtitle and Clip Generator

[Português](README.md) · English · [Español](README.es.md)

Open source app to transcribe videos, edit captions, find clips with AI, and export MP4 files. The interface supports Portuguese, English, and Spanish. Local use requires no account, checkout, or subscription.

## Install with AI

Open **[the copy-ready prompt for Codex, Claude, or another AI](INSTALL-WITH-AI.md)** and paste it into an assistant with terminal access. It will download, install, start, and verify the app. You enter your OpenAI key directly in Settings.

Your video files stay on the computer running the app. Transcription and other AI features use your own OpenAI API key, which may incur OpenAI charges. FFmpeg renders videos locally.

## Install

Download the [project ZIP](https://github.com/sellpayclub/gerador-legendas-e-cortes/archive/refs/heads/main.zip) or clone the repository:

```bash
git clone https://github.com/sellpayclub/gerador-legendas-e-cortes.git
cd gerador-legendas-e-cortes
```

- **macOS:** install [Homebrew](https://brew.sh), move the folder outside Desktop/Documents/Downloads, and run `bash install.sh` in Terminal. Open <http://localhost:3000>.
- **Windows 10/11:** extract the ZIP and double-click `Instalar-Windows.cmd`. It uses `winget` to install missing Python, Node, and FFmpeg. Later, double-click `Iniciar-Windows.cmd` to start the app.
- **Ubuntu/VPS:** see the [Portuguese installation manual](GUIA-INSTALACAO.md) for deployment details.

In **Settings**, paste your [OpenAI API key](https://platform.openai.com/api-keys), click **Test connection**, and save it. The project does not include an API key. On Apple Silicon Macs, you can optionally install `mlx` for local transcription; other AI features still require OpenAI.

Choose **Subtitles** or **Clips**, upload a video, edit the result, render, then download the MP4. Use the language switcher at the top to change the interface. The spoken language of the uploaded video is a separate choice.

Python 3.11+, Node.js 22+, and FFmpeg with the `ass`/libass filter are required. Projects are saved under `data/jobs/` and the local key under `data/app-settings.json` or `backend/.env`; these files are not committed.

The local installer binds to `localhost`. For use from iPhone or Android, publish the app on your own HTTPS server with appropriate access protection. See the [full manual](GUIA-INSTALACAO.md) for usage, updates, and troubleshooting.

The project's code is licensed under [MIT](LICENSE); third-party assets and packages retain their own licenses.
