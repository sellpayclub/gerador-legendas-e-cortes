# Comece aqui — gerar suas quatro aulas no NotebookLM

Os quatro roteiros estão prontos. Este pacote contém fontes e prompts; os MP4s ainda precisam ser gerados na sua conta.

## Primeiro vídeo: Português — Mac

1. Abra https://notebooklm.google.com no computador e entre na sua conta.
2. Crie um novo notebook e dê o nome **Instalação do Gerador — Português — Mac**.
3. Adicione uma fonte. Escolha o envio de arquivo e selecione **PT-MAC.md** desta pasta. Se a interface não aceitar Markdown, abra o arquivo, copie o conteúdo inteiro e use a opção de colar texto como fonte.
4. Aguarde o processamento da fonte. Não envie toda a pasta nem os quatro idiomas juntos.
5. Abra **Studio / Estúdio → Video Overview / Resumo em vídeo** e a opção de personalizar.
6. Escolha o formato **Explainer / Explicativo**, idioma **Português (Brasil)** e visual clássico ou simples, conforme as opções disponíveis.
7. Abra **PROMPTS-NOTEBOOKLM.md**, copie o prompt **Português — Mac** e cole no campo de instruções da geração de vídeo. Esse prompt vai na personalização do vídeo, não apenas no chat do notebook.
8. Clique em gerar. O Google informa que a geração pode demorar mais de 30 minutos; limites dependem da sua conta.
9. Assista ao vídeo completo. Confira se ele ensina a instalar, salvar a chave, transcrever, renderizar e baixar. Verifique os comandos na tela; gráficos gerados podem conter erros.
10. Use a opção de download do vídeo e salve como **instalacao-pt-mac.mp4**.

## Repetir para as outras versões

| Notebook | Fonte única | Prompt | Idioma | Nome do MP4 |
| --- | --- | --- | --- | --- |
| Português — Mac | PT-MAC.md | Português — Mac | Português (Brasil) | instalacao-pt-mac.mp4 |
| Português — Windows | PT-WINDOWS.md | Português — Windows | Português (Brasil) | instalacao-pt-windows.mp4 |
| English — Mac | EN-MAC.md | English — Mac | English | installation-en-mac.mp4 |
| English — Windows | EN-WINDOWS.md | English — Windows | English | installation-en-windows.mp4 |

Crie um notebook separado para cada linha e repita os passos. Não é necessário me enviar senha, login ou chave Google.

## Se o vídeo ficar resumido demais

Não publique como aula completa se pular passos. Gere três partes por sistema/idioma, usando o mesmo notebook e estes focos na personalização:

- Parte 1: cenas 1 a 7 — preparar, instalar e abrir.
- Parte 2: cenas 8 a 12 — chave, primeiro vídeo, revisão, renderização e download.
- Parte 3: cenas 13 a 15 — cortes, diagnóstico e reabertura.

Acrescente ao prompt: “Explique detalhadamente somente as cenas indicadas. Termine com o ponto de partida da próxima parte. Não resuma as ações em frases genéricas.” A duração e a cobertura exatas precisam ser verificadas no resultado.

## Sobre a demonstração visual

O NotebookLM cria vídeo explicativo a partir das fontes, com voz e elementos visuais. Isso não executa o instalador nem equivale a gravar o mouse clicando no software real. Os roteiros incluem sugestões visuais; não incluem capturas de tela já produzidas.

Para uma demonstração fiel de cada clique, use capturas ou gravação real da instalação como material complementar e revise os visuais gerados. A geração pode reorganizar ou resumir o conteúdo. Não apresente imagens ilustrativas como evidência de instalação concluída.

## Revisão antes de disponibilizar para alunos

- Arquivo e prompt correspondem ao idioma e ao sistema corretos.
- O vídeo explica o caminho com IA e a alternativa manual.
- Mac inclui Homebrew e pasta permanente; Windows inclui extrair ZIP e os nomes exatos dos arquivos.
- Comandos e URLs estão legíveis e sem alterações inventadas.
- Chave de API aparece apenas fictícia ou ocultada; custo da API é mencionado.
- A aula distingue testar de salvar a chave.
- O teste final inclui abrir o MP4 baixado, não só abrir a página inicial.
- Windows permanece descrito como procedimento preparado até ser testado em uma máquina Windows real.
- Nenhuma promessa de funcionamento universal, computador desligado ou instalação nativa no iPhone.

## Base utilizada

Roteiros conferidos com os instaladores e o manual do repositório no commit aa3b845. Nenhuma nova instalação Windows foi executada na elaboração. A área de Aulas do aplicativo não foi alterada por este pacote.

Documentação Google consultada: https://support.google.com/notebooklm/answer/16454555?hl=en
Documentação OpenAI para a etapa de chave/API: https://developers.openai.com/api/docs/quickstart

O Google documenta seleção de formato, idioma, estilo, instruções e download. As vozes e visuais podem conter erros. Português (Brasil) e inglês estão disponíveis no formato explicativo. Estas instruções podem mudar com a interface do serviço.
