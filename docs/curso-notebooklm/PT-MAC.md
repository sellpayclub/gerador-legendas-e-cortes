# Instalar e usar do início ao fim — Mac

Documento-fonte para aula narrada. Público: iniciante absoluto. Ritmo: calmo, uma ação por vez. Duração desejada: 10–15 minutos, sem garantia de duração pelo NotebookLM. As cenas são instruções de produção, não capturas já realizadas. Resultados descritos são critérios esperados, não provas de testes novos.

## 1. O que vamos fazer

Visual sugerido: Título com o sistema operacional desta aula e três marcos: instalar, configurar, exportar.

Narração:

Você vai instalar o Gerador de Legendas e Cortes no seu computador e produzir seu primeiro vídeo legendado. Não precisa saber programar. Primeiro vamos instalar, depois conectar a inteligência artificial e, por último, baixar um vídeo pronto. Pause sempre que precisar. O programa é open source e não exige compra ou cadastro no modo local. Os recursos da API de inteligência artificial têm cobrança separada na sua conta OpenAI. O endereço local só funciona no computador onde o aplicativo está rodando; ele não é um site público.

Pausa / conferência: Separe um vídeo de 20 a 30 segundos com voz clara e mantenha o computador ligado e conectado à internet.

## 2. Escolha o caminho de instalação

Visual sugerido: Dois cartões: com assistente de IA; sem assistente, usando o instalador.

Narração:

Se você já usa um assistente de IA que executa comandos no seu computador, pode pedir que ele faça a instalação. Uma conversa comum no navegador pode apenas explicar comandos; ela não necessariamente consegue instalar programas. Abra uma tarefa local no seu assistente e pergunte: você consegue executar comandos nesta máquina? Se não conseguir, siga a alternativa manual desta aula. Não é necessário contratar um assistente para usar o instalador do projeto.

Pausa / conferência: Escolha um caminho. Não execute a instalação manual ao mesmo tempo que a IA.

## 3. Encontre o projeto e copie o prompt

Visual sugerido: Endereço do GitHub em letras grandes. Destaque INSTALAR-COM-IA.md e o bloco de texto.

Narração:

Abra o navegador e acesse o link do repositório fornecido junto desta aula. Confira o proprietário sellpayclub e o nome gerador-legendas-e-cortes. Na lista de arquivos, abra INSTALAR-COM-IA.md. Selecione todo o conteúdo do bloco de prompt, copie e cole em uma nova tarefa local do seu assistente. O prompt autoriza baixar o projeto, instalar dependências e conferir o funcionamento. Se já existe uma instalação, avise a IA para preservar seus vídeos e configurações. Não envie senhas nem sua chave de API na conversa.

Pausa / conferência: Envie o prompt e acompanhe as solicitações. Se o assistente não tiver acesso ao terminal, use os passos manuais seguintes.

## 4. Acompanhe a instalação

Visual sugerido: Cartões Python: serviço do app; Node.js: interface; FFmpeg: processamento de vídeo.

Narração:

Durante a instalação aparecem mensagens e downloads. Python executa o serviço que trabalha nos vídeos. Node.js prepara a interface. FFmpeg é o programa que monta o vídeo final com as legendas. Você não precisa configurar cada um por conta própria: o instalador cuida das dependências, desde que os pré-requisitos desta aula estejam disponíveis. A primeira instalação pode levar vários minutos. Aguarde a conclusão, sem fechar a janela ou suspender o computador. Se aparecer erro, guarde a mensagem; não fique repetindo comandos desconhecidos.

Pausa / conferência: Espere a confirmação de conclusão. As próximas duas cenas detalham o caminho manual do seu sistema.

## 5. Instalação manual no Mac: baixar e preparar

Visual sugerido: Finder e navegador; pasta pessoal permanente, fora de Downloads.

Narração:

Se a sua IA já concluiu a instalação, pule estas duas cenas manuais. Caso contrário, no GitHub clique em Code e Download ZIP. Abra o ZIP para extrair a pasta. No Finder, use Ir e Início para abrir sua pasta pessoal e mova a pasta extraída para lá. Não deixe a instalação definitiva em Downloads, Mesa ou Documentos. Agora abra brew.sh e siga as instruções oficiais para instalar o Homebrew, caso ainda não tenha. Homebrew instala as dependências do aplicativo. Se houver solicitação de senha do Mac, digite-a apenas no Terminal; os caracteres podem não aparecer enquanto você digita.

Pausa / conferência: Aguarde o Homebrew terminar e siga as instruções finais exibidas por ele para disponibilizar o comando brew.

## 6. Instalação manual no Mac: executar e reabrir

Visual sugerido: Terminal: cd seguido da pasta arrastada; bash install.sh; ./legendas.sh status.

Narração:

Abra o Terminal pela busca do Mac. Digite cd seguido de um espaço, arraste a pasta do projeto do Finder para a janela do Terminal e pressione Enter. Isso coloca o Terminal dentro da pasta correta, mesmo se o nome tiver espaços. Digite bash install.sh e pressione Enter. Aguarde os downloads e a compilação. Quando terminar, abra o endereço local. Para conferir o serviço, execute ./legendas.sh status dentro da pasta. Se precisar reiniciar, use ./legendas.sh reiniciar. Para ver mensagens de diagnóstico, use ./legendas.sh logs. Os serviços são registrados para iniciar ao entrar na sua sessão do Mac; o computador precisa estar ligado.

Pausa / conferência: Confirme o resultado antes de prosseguir. Esta aula descreve o caminho padrão; erros dependem da mensagem exibida.

## 7. Abrir o aplicativo e conferir a instalação

Visual sugerido: Barra de endereço: http://127.0.0.1:3000. Depois: http://127.0.0.1:8000/api/health.

Narração:

Quando o instalador terminar, abra o endereço local indicado na tela. Por padrão, ele é http://127.0.0.1:3000. Cole na barra de endereço do navegador, não no campo de pesquisa. Você deve ver a página inicial do gerador. Abra também o endereço de verificação terminado em /api/health. Essa página mostra texto técnico. Procure ok com valor true e ffmpeg_ok com valor true. Esses resultados confirmam que o serviço responde e encontra o FFmpeg. Eles ainda não comprovam que a transcrição e a exportação funcionam: vamos testar isso com um vídeo.

Pausa / conferência: Se a página não abrir, vá à cena de diagnóstico. Se abrir, continue para a chave OpenAI.

## 8. Conectar sua conta OpenAI

Visual sugerido: Link platform.openai.com/api-keys. Usar apenas chave fictícia ocultada, nunca uma chave real.

Narração:

Abra platform.openai.com/api-keys e entre na sua conta da plataforma OpenAI. Se ainda não tem conta, conclua o cadastro apresentado. Na área de chaves, use a opção de criar uma nova chave secreta e dê um nome que você reconheça, como Legendas local. Copie a chave na própria plataforma. Ela funciona como uma senha para o aplicativo usar a API em sua conta. A configuração de faturamento e a disponibilidade de uso devem ser conferidas na plataforma antes do primeiro teste. Não presuma que sua assinatura do ChatGPT fornece saldo de API. Nunca publique a chave ou a inclua em um vídeo.

Pausa / conferência: Mantenha a chave privada. Volte ao aplicativo local para colocá-la diretamente no campo de configuração.

## 9. Testar e salvar a chave

Visual sugerido: Configurações → API Key → Testar conexão → Salvar. Mostrar sucesso somente como resultado esperado.

Narração:

No topo do aplicativo, clique em Configurações. Cole sua chave no campo API Key. Use Testar conexão e aguarde o resultado. Se o teste falhar, confirme a chave, o acesso à API e a mensagem recebida; não prossiga como se estivesse tudo certo. Se funcionar, clique em Salvar. Testar e salvar são ações diferentes. Depois de salvar, o campo pode ficar vazio e a tela mostrar apenas parte da chave já cadastrada. Isso é esperado. Para o primeiro uso, mantenha o motor OpenAI Whisper e deixe a URL alternativa em branco.

Pausa / conferência: Confirme a mensagem de configuração salva. Nunca mostre a chave completa nas capturas usadas no curso.

## 10. Enviar seu primeiro vídeo

Visual sugerido: Início → Legendas → idioma do áudio → escolher arquivo.

Narração:

Volte ao Início. Escolha Legendas. No campo de idioma do áudio, escolha o idioma falado no vídeo ou deixe a detecção automática. O idioma da interface, escolhido no menu superior, é uma preferência diferente: mudar o menu para inglês não traduz o vídeo. Clique na área de envio, escolha seu vídeo curto e aguarde o upload e a transcrição. Prefira MP4 com vídeo H.264 e áudio AAC no primeiro teste. O sistema aceita outros formatos, mas a reprodução no navegador pode variar.

Pausa / conferência: Aguarde o editor mostrar o vídeo e o texto transcrito. Se a transcrição falhar, consulte a cena de diagnóstico.

## 11. Revisar e editar

Visual sugerido: Editor com texto, estilo e posição da legenda. Usar exemplo neutro de frase.

Narração:

Reproduza o vídeo e acompanhe as palavras. A transcrição por IA pode errar nomes, palavras e pontuação, então revise antes de exportar. Corrija o texto necessário, escolha um estilo e ajuste a posição para não cobrir o rosto ou informações importantes. Para este primeiro teste, use poucas alterações. Confira se há imagem, áudio e legendas na prévia. Depois de validar o fluxo básico, você pode experimentar os demais estilos e efeitos.

Pausa / conferência: Prossiga quando o texto estiver revisado e a prévia estiver correta.

## 12. Renderizar e baixar o arquivo final

Visual sugerido: Renderizar → aguardar status de conclusão → Baixar MP4 → abrir arquivo baixado.

Narração:

Clique no botão de renderização do vídeo. Renderizar significa criar um arquivo novo com suas escolhas aplicadas. Aguarde a conclusão. O tempo depende do tamanho do vídeo e da capacidade do computador; não existe prazo único. Quando o aplicativo indicar que terminou, clique em Baixar MP4. Abra a lista de downloads do navegador e localize o arquivo. Dê dois cliques nele para assistir fora do aplicativo. Confira imagem, áudio, legendas e duração. O teste só está completo quando o MP4 baixado reproduz corretamente, e não apenas quando a página inicial abre.

Pausa / conferência: Guarde o MP4 final. Se faltar imagem, som ou legenda, pare e registre o problema antes de processar vídeos longos.

## 13. Conhecer o modo Cortes

Visual sugerido: Início → Cortes → detecção → revisão de trechos → exportação.

Narração:

Além de legendar um vídeo inteiro, você pode usar o modo Cortes para encontrar trechos em um conteúdo mais longo. Volte ao início, escolha Cortes e envie um vídeo com conteúdo suficiente para selecionar trechos. Use a detecção por IA, revise as sugestões e ajuste início, fim e composição antes de exportar. Um vídeo muito curto pode não gerar sugestões; isso por si só não significa falha. A seleção da IA é uma sugestão editorial: você decide o que publicar. Exporte um trecho e abra o arquivo baixado para conferir o resultado.

Pausa / conferência: Este é um teste separado. A aprovação do vídeo legendado não comprova automaticamente todas as funções de cortes.

## 14. Diagnóstico sem começar do zero

Visual sugerido: Três situações: página não abre; transcrição falha; exportação falha.

Narração:

Se a página não abrir, confira o endereço e use o procedimento de reinício do seu sistema, mostrado nesta aula. Se a transcrição falhar, teste a chave nas Configurações e consulte o acesso e o faturamento na plataforma OpenAI. Se o vídeo não aparecer na prévia, teste um MP4 H.264 com áudio AAC. Se a renderização falhar, peça à sua IA para verificar o FFmpeg, o filtro ass, o espaço livre e os logs. Uma porta ocupada precisa ser investigada; não encerre um programa desconhecido. Copie a mensagem de erro, ocultando qualquer chave. Você pode pedir: diagnostique minha instalação existente, preserve meus vídeos e corrija este erro.

Pausa / conferência: Não apague a pasta do projeto para tentar resolver um erro. Os seus trabalhos podem estar nela.

## 15. Reabrir e guardar seus trabalhos

Visual sugerido: Favorito do navegador e pasta data/jobs/.

Narração:

Salve o endereço local nos favoritos. O app precisa do computador ligado e dos serviços em execução; ele não continua processando com a máquina desligada. Seus projetos ficam na pasta data/jobs dentro da instalação. Guarde os MP4s exportados e faça backup dos trabalhos importantes. O arquivo data/app-settings.json contém configuração privada, então mantenha-o fora de compartilhamentos públicos. Para atualizar, preserve esses dados e siga o manual do repositório. A instalação estará validada para o seu uso quando abrir, transcrever, renderizar e permitir baixar um arquivo reproduzível.

Pausa / conferência: Ao terminar, confirme os quatro marcos: página abre; chave configurada; transcrição concluída; MP4 baixado e reproduzido.

## Links para acompanhar a aula

- https://github.com/sellpayclub/gerador-legendas-e-cortes
- https://github.com/sellpayclub/gerador-legendas-e-cortes/blob/main/INSTALAR-COM-IA.md
- https://github.com/sellpayclub/gerador-legendas-e-cortes/blob/main/GUIA-INSTALACAO.md
- http://127.0.0.1:3000
- http://127.0.0.1:8000/api/health
- https://platform.openai.com/api-keys
- https://developers.openai.com/api/docs/quickstart
- https://brew.sh
