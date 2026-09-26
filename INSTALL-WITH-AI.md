# Install with an AI assistant

Copy the prompt below into Codex, Claude, or another assistant that can run terminal commands on your computer. By default, the app runs locally at <http://localhost:3000>.

```text
Install and start the open source Subtitle and Clip Generator on my computer.
Official repository: https://github.com/sellpayclub/gerador-legendas-e-cortes
Installation guide: https://github.com/sellpayclub/gerador-legendas-e-cortes/blob/main/GUIA-INSTALACAO.md

You may download the repository, install its required dependencies, run its installer, start the local services, and verify them. Complete the steps you can perform with terminal access.

Detect my OS and architecture. Keep the project in a permanent folder in my home directory; on macOS, avoid Desktop/Documents/Downloads. If it already exists, preserve projects, settings, secrets, and local edits. Never reset or delete the existing copy. Read the README and guide first. If Git is unavailable, use the official GitHub ZIP.

On macOS run `bash install.sh`. On Windows 10/11 run `Instalar-Windows.cmd` or `scripts/install-windows.ps1` in PowerShell. On Ubuntu with a domain, follow the guide and run `sudo bash install.sh`. Do not try to install the backend natively on an iPhone; iPhone access uses a browser when the server is published with HTTPS.

Verify `http://127.0.0.1:8000/api/health` reports `ok: true` and `ffmpeg_ok: true`, the page at `http://localhost:3000` opens, and `/checkout` is absent. Fix any startup failure using the logs. Check automatic startup on macOS/Windows.

Open `http://localhost:3000/configuracoes` so I can enter my own OpenAI key directly in the app, test it, and save it. Do not ask me to paste the key into chat or commit it to Git. OpenAI API usage may incur charges.

Finish by reporting the app URL, install folder, checks performed, and anything I must still do. Do not claim to have tested an OS/device you could not access. If you have no terminal access, say so and provide exact commands for my OS. Keep the server on localhost unless I provide a domain and choose access protection for public hosting.
```
