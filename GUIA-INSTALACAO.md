# Manual de instalação e uso

Este projeto roda no seu computador, sem checkout e sem cadastro obrigatório. A interface tem português, inglês e espanhol. Para transcrever e usar IA, você informa uma chave OpenAI sua; a cobrança do uso da API é feita pela OpenAI.

Se você usa Codex, Claude ou outro assistente com acesso ao terminal, pode copiar o prompt de [Instalar com IA](INSTALAR-COM-IA.md) para ele fazer as etapas de instalação e verificação.

## 1. Baixar

Na [página do projeto](https://github.com/sellpayclub/gerador-legendas-e-cortes), clique em **Code → Download ZIP**, extraia a pasta e mantenha-a em um local permanente. Se já usa Git, pode executar:

```bash
git clone https://github.com/sellpayclub/gerador-legendas-e-cortes.git
cd gerador-legendas-e-cortes
```

Não coloque a pasta do Mac em Desktop, Documentos ou Downloads para uso como serviço automático. Mova para uma pasta como `~/gerador-legendas-e-cortes`.

## 2. Instalar no Mac

Instale o [Homebrew](https://brew.sh) se ainda não estiver instalado. Abra o Terminal dentro da pasta extraída e execute:

```bash
bash install.sh
```

O instalador instala Python 3.13, Node.js 22 e FFmpeg com libass, cria o ambiente Python, baixa dependências do frontend e compila. Ele também registra dois serviços locais que iniciam quando você entra no Mac e reiniciam se pararem. O primeiro processo pode demorar vários minutos.

Abra <http://localhost:3000>. Para verificar ou reiniciar:

```bash
./legendas.sh status
./legendas.sh reiniciar
./legendas.sh logs
```

## 3. Instalar no Windows

Requer Windows 10 ou 11 com [Windows Package Manager](https://learn.microsoft.com/windows/package-manager/winget/) (`winget`, normalmente já instalado). Abra a pasta extraída e dê dois cliques em **Instalar-Windows.cmd**. O instalador tenta instalar Python 3.13, Node.js LTS e FFmpeg quando faltarem. Se um instalador do Windows pedir permissão, conclua-o. Se aparecer uma mensagem para abrir outro terminal, feche a janela e dê dois cliques novamente no instalador.

Depois da instalação, o navegador abre <http://localhost:3000>. O app inicia automaticamente quando você entra no Windows; também pode abrir **Iniciar-Windows.cmd** manualmente. O instalador verifica se o FFmpeg tem o filtro `ass`, necessário para gravar legendas no vídeo.

## 4. Configurar a IA

1. Crie uma chave em [OpenAI API Keys](https://platform.openai.com/api-keys). Uma conta do ChatGPT não inclui automaticamente créditos de API.
2. Abra **Configurações** em <http://localhost:3000/configuracoes>.
3. Cole a chave, clique em **Testar conexão** e depois em **Salvar**.

A chave fica apenas no computador servidor, em `data/app-settings.json`. Não publique esse arquivo. Se preferir, coloque `OPENAI_API_KEY=` no arquivo `backend/.env` e não salve a mesma chave na interface. A configuração da interface tem prioridade.

No Mac com Apple Silicon, a transcrição local MLX é opcional. Para instalar:

```bash
cd backend
.venv/bin/python -m pip install -e '.[mlx]'
```

Reinicie o app e selecione MLX nas Configurações. A detecção de cortes e outros recursos de IA ainda precisam da chave OpenAI.

## 5. Criar o primeiro vídeo

1. Na página inicial, escolha **Legendas** ou **Cortes** e envie um MP4, MOV, MKV, AVI ou WebM curto para testar.
2. Aguarde a transcrição. O editor mostra cada palavra com seu tempo. Corrija o texto se necessário.
3. Em Legendas, selecione estilo, destaque e posição. Clique em **Renderizar**. Ao concluir, clique em **Baixar MP4**.
4. Em Cortes, use a detecção por IA, escolha trechos, ajuste formato/composição, exporte e baixe cada MP4.
5. Use o seletor no topo para mudar a interface entre português, inglês e espanhol. O idioma da fala do vídeo é uma opção separada na tela de envio.

Os projetos e arquivos ficam em `data/jobs/`. Faça backup dessa pasta se quiser preservá-los. Ao apagar um projeto no app, os arquivos associados são removidos.

## Atualizar

Se baixou ZIP, baixe o ZIP novo e copie para ele `data/jobs/`, `data/app-settings.json` e `backend/.env` se existirem. Depois rode o instalador novamente. Se clonou com Git, execute `git pull` dentro da pasta e rode o instalador outra vez.

No Mac, também pode usar `./legendas.sh atualizar`. No Windows, execute novamente **Instalar-Windows.cmd**.

## Diagnóstico

- **A página não abre:** no Mac, execute `./legendas.sh status` e `./legendas.sh logs`; no Windows, tente **Iniciar-Windows.cmd** novamente.
- **Porta 3000 ou 8000 ocupada:** feche outro servidor que use essa porta e inicie o aplicativo novamente.
- **Transcrição falha:** confirme a chave e o saldo na OpenAI em Configurações. Teste um vídeo curto primeiro.
- **Render falha:** o FFmpeg precisa do filtro `ass`/libass. Rode `ffmpeg -filters` no Terminal/PowerShell e procure `ass`.
- **Vídeo não aparece no preview:** experimente MP4 H.264 com áudio AAC. Outros formatos podem ser aceitos no upload, mas alguns navegadores não os reproduzem diretamente.
- **Um botão parece parado:** recarregue a página, confirme que o backend está ativo e veja os logs. Trabalhos longos podem precisar de vários minutos para IA e renderização.

O backend responde em <http://127.0.0.1:8000/api/health>. O resultado deve incluir `"ok":true` e `"ffmpeg_ok":true`. Após configurar a chave, `"openai_configured":true`.

## Usar pelo telefone ou publicar

O instalador local atende apenas `localhost`, por segurança. No iPhone ou Android, abra o aplicativo no navegador **quando ele estiver publicado em um servidor seu com HTTPS**. O telefone serve de interface; o processamento continua no servidor. O projeto também contém scripts de deploy para VPS Ubuntu, mas publicar na internet exige configurar domínio, HTTPS, proteção de acesso e armazenamento adequados ao seu uso. Não exponha diretamente o modo local sem autenticação.

Em uma VPS Ubuntu 22.04/24.04, o fluxo básico é apontar o DNS do domínio para o IP do servidor, clonar o repositório e executar `sudo bash install.sh`. O instalador pede o domínio e configura os serviços e o proxy HTTPS. Antes de abrir o domínio para outras pessoas, configure uma camada de autenticação no proxy: a instalação local gratuita não exige conta e qualquer visitante que alcance a interface pode usar os recursos configurados nela. Para uso apenas pessoal, mantenha o acesso restrito pela rede privada ou VPN.

## Licença

O código do projeto está sob [MIT](LICENSE). Dependências e recursos de terceiros mantêm as próprias licenças.
