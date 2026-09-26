# Gerador de Legendas e Cortes

[English](README.en.md) · [Español](README.es.md) · Português

Aplicativo open source para transcrever vídeos, editar legendas, encontrar cortes com IA e exportar MP4. A interface funciona em português, inglês e espanhol. Não há checkout, assinatura ou conta obrigatória na instalação local.

## Instale com uma IA

Abra **[Instalar com Codex, Claude ou outra IA](INSTALAR-COM-IA.md)**, copie o bloco de texto e cole no seu assistente com acesso ao terminal. Ele baixa, instala, inicia e verifica o aplicativo. Você só informa sua chave OpenAI diretamente na tela de Configurações.

Os vídeos e os projetos ficam no computador que executa o servidor. A transcrição e os recursos de IA usam a sua própria chave OpenAI e podem gerar custos na sua conta. FFmpeg faz a renderização localmente. iPhone e Android podem usar a interface pelo navegador quando o aplicativo estiver publicado em um servidor com HTTPS; o processamento acontece no servidor, não no telefone.

## Instalação rápida

Baixe o [ZIP do projeto](https://github.com/sellpayclub/gerador-legendas-e-cortes/archive/refs/heads/main.zip) ou clone:

```bash
git clone https://github.com/sellpayclub/gerador-legendas-e-cortes.git
cd gerador-legendas-e-cortes
```

**macOS:** instale o [Homebrew](https://brew.sh), coloque a pasta fora de Desktop/Documentos/Downloads e execute `bash install.sh` no Terminal. O instalador instala Python, Node e FFmpeg, compila a aplicação e cria serviços que sobem ao entrar no Mac. Abra <http://localhost:3000>.

**Windows 10/11:** extraia o ZIP, dê dois cliques em `Instalar-Windows.cmd` e siga os avisos. O script usa o Windows Package Manager (`winget`) para instalar Python, Node e FFmpeg quando faltarem, compila e abre o aplicativo. Ele também inicia o app automaticamente quando você entrar no Windows; use `Iniciar-Windows.cmd` para iniciar manualmente. Se o Windows pedir um novo terminal após instalar um programa, abra o instalador novamente.

**Ubuntu/VPS:** veja [o guia completo](GUIA-INSTALACAO.md). A instalação publicada com domínio exige um servidor e HTTPS; o uso local no Mac ou Windows dispensa ambos.

Depois de abrir o app, entre em **Configurações**, cole sua [chave de API OpenAI](https://platform.openai.com/api-keys), clique em **Testar conexão** e **Salvar**. A chave não é fornecida pelo projeto. Para transcrição local sem OpenAI, usuários de Mac Apple Silicon podem instalar o extra opcional `mlx` e selecioná-lo nas configurações; detecção de cortes e outras funções de IA continuam precisando de chave OpenAI.

## O que você pode fazer

- Enviar MP4, MOV, MKV, AVI ou WebM.
- Transcrever fala com tempo por palavra; corrigir texto e pontuação no editor.
- Aplicar estilos, destacar palavras e renderizar legendas no MP4.
- Detectar cortes com IA, ajustar trechos, compor formatos verticais e exportar.
- Selecionar português, inglês ou espanhol no menu de idioma.

O [manual de instalação e uso](GUIA-INSTALACAO.md) tem instruções passo a passo, atualização e solução de problemas. O [guia rápido](COMO-USAR.md) explica o fluxo de trabalho.

## Requisitos e armazenamento

Requer Python 3.11+ (instalador usa 3.13), Node.js 22+ e FFmpeg com filtro `ass`/libass. Recomendamos pelo menos 4 GB de RAM e espaço para os vídeos e MP4 exportados. Os trabalhos ficam em `data/jobs/`; a configuração local da chave fica em `data/app-settings.json` ou `backend/.env`. Esses dados não entram no Git.

No Mac, use `./legendas.sh status`, `./legendas.sh reiniciar` e `./legendas.sh logs`. No Windows, use `Iniciar-Windows.cmd` para abrir novamente.

## Código e licença

Frontend: Next.js. Backend: FastAPI, FFmpeg e OpenAI. O código do projeto é distribuído sob [licença MIT](LICENSE). Bibliotecas, fontes e outros recursos de terceiros mantêm suas próprias licenças.
