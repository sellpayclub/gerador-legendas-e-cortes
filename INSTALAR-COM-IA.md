# Instalar com uma IA

Use este caminho se seu Codex, Claude ou outro assistente consegue executar comandos no seu computador. Copie **todo o texto abaixo** e cole em uma tarefa nova do assistente. A instalação padrão abre o aplicativo **somente neste computador**, em <http://localhost:3000>. Publicar na internet é outra configuração.

```text
Quero instalar e deixar funcionando o aplicativo open source Gerador de Legendas e Cortes no meu computador.
Repositório oficial: https://github.com/sellpayclub/gerador-legendas-e-cortes
Manual: https://github.com/sellpayclub/gerador-legendas-e-cortes/blob/main/GUIA-INSTALACAO.md

Você tem minha autorização para baixar o repositório, instalar as dependências necessárias, executar o instalador do projeto, iniciar os serviços locais e verificar a instalação. Trabalhe até o aplicativo abrir e responder. Não me peça para executar os passos que você consegue executar no terminal.

1. Detecte meu sistema operacional e arquitetura. Use uma pasta permanente na minha pasta pessoal. No macOS, não coloque o projeto em Desktop, Documentos ou Downloads. Se já houver uma cópia do projeto, preserve trabalhos, configurações e mudanças locais; não apague, sobrescreva ou faça reset. Verifique a origem Git antes de atualizar. Se Git não estiver disponível, baixe o ZIP oficial do GitHub.
2. Leia o README e o manual do repositório. No macOS, execute `bash install.sh`. No Windows 10/11, execute `Instalar-Windows.cmd` ou `scripts/install-windows.ps1` pelo PowerShell. Para Ubuntu com domínio próprio, siga o manual e use `sudo bash install.sh`. O instalador deve instalar/configurar Python, Node.js e FFmpeg com libass, compilar o frontend e deixar o backend e o frontend iniciados. Não tente instalar a aplicação nativamente no iPhone; nele a interface funciona pelo navegador quando o servidor estiver publicado com HTTPS.
3. Verifique que `http://127.0.0.1:8000/api/health` retorna `ok: true` e `ffmpeg_ok: true`, que `http://localhost:3000` abre, e que `/checkout` não existe. Se algo falhar, leia os logs, corrija a causa e teste novamente. No Mac, confirme que os serviços iniciam ao entrar na sessão. No Windows, confirme o atalho de inicialização automática e que `Iniciar-Windows.cmd` funciona.
4. Abra `http://localhost:3000/configuracoes` para eu colocar minha própria chave OpenAI diretamente no app, testar e salvar. Não peça para eu colar a chave na conversa e não a grave no Git. Sem a chave, a instalação ainda pode estar correta, mas transcrição e IA não vão funcionar. A OpenAI pode cobrar o uso da API.
5. No final, me diga o endereço para abrir, onde a pasta foi instalada, o resultado das verificações e o que ainda depende de mim. Não diga que testou Windows ou iPhone se você não executou nesses dispositivos. Se você não tiver acesso ao terminal, explique isso e me dê o comando exato para o meu sistema.

Não configure acesso público à internet sem eu fornecer domínio e escolher proteção de acesso. Para uso local, mantenha o servidor em localhost.
```

O projeto não inclui chave OpenAI. Depois de salvar a sua na tela de Configurações, faça um primeiro teste com vídeo curto. Se quiser instalar sem IA, siga o [manual de instalação](GUIA-INSTALACAO.md).
