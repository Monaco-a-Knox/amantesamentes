# Como utilizar a automação

Apesar de supostamente automático, o repositório ainda requer certa manutenção para gerar releases corretamente. Felizmente, essa manutenção é simples e pode ser feita tanto via linha de comando, quanto via interface web (pelo site).

## Liberando patches via linha de comando

Para começarmos a trabalhar via linha de comando, primeiramente precisamos clonar o repositório. Caso não tenha o comando ``git`` habilitado no seu terminal (seja Powershell ou CMD), instale a versão mais nova [aqui](https://git-scm.com/downloads).

Para clonar o repositório, abra o cmd no local onde você quer que ele seja baixado e rode o comando:
``git clone https://github.com/Monaco-a-Knox/Florescer.git``

Utilize o comando ``cd`` para entrar dentro do repositório baixado.

Agora vamos trabalhar com mudanças neste repositório local. É importante saber que as suas mudanças locais **não são automaticamente sincronizadas com as mudanças remotas (na web)**. Para atualizar seu repositório local, rode o comando ``git pull``. É bom lembrar que se você estiver fazendo mudanças em alguns arquivos que foram também alterados remotamente, você terá **um conflito**. Conflitos no geral são chatos de resolver via linha de comando, então recomendo utilizar o Github Desktop para lidar com eles. Conflitos também irão te impedir de atualizar seu repositório local a não ser que você descarte as mudanças locais dos arquivos afetados.

Agora que estamos com nosso repositório atualizado, é hora de começar o tracking das mudanças locais. Digamos que alterei este mesmo ``readme`` que você está lendo. Em git, arquivos são colocados "à postos" antes de serem enviados para o servidor remoto. Caso eu tenha feito alguma alteração local, rodarei o comando ``git add *`` (sendo ``*`` uma atualização para a pasta toda - caso queira ser mais específico, rode ``git add <nome do arquivo ou pasta>``, mas isto irá adicionar somente os arquivos explicitamente citados).

É normal que nada (aparentemente) aconteça depois de rodar ``git add``. Para colocarmos nossos arquivos "à postos", rodaremos o comando ``git commit -m "Mensagem de atualização"``. Essa é a mesma mensagem que aparece no seu repositório quando você modifica um arquivo pelo site do Github. Após rodar este comando, será apresentado um segmento com todos os arquivos modificados que serão enviados para o servidor remoto.

Para finalmente enviar os arquivos, rodaremos ``git push origin master``, sendo o ``master`` o nome da branch **padrão**. Leia mais sobre branches [aqui](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell). Em 99% das vezes este repositório irá trabalhar na branch ``master``, então não se preocupe com detalhes. Enfim, coloque seu login e senha e espere a sincronização. Após enviado, você poderá ver suas mudanças pelo seu repositório remoto, no site do Github.

**Espera, mas e o release automático?** Para criar uma tarefa de compilação, nós precisamos criar uma **tag**. Uma tag nada mais é que uma identificação de versão, como por exemplo ``1.0`` ou ``v1.0.0``. Estas tags são importantes porque elas marcam um ponto confortável no seu repositório, como uma cápsula do tempo. É importante que tags sejam **incrementais**, porque tags maiores são enviadas para o topo, enquanto tags menores são enviadas para o fundo, mesmo que seja a mais nova. Por exemplo: criar a tag ``v0.1`` quando a tag maior do repositório é ``v1.0`` irá colocar a tag nova **abaixo** de todas, mesmo que seja a versão mais nova. Isso não é uma boa prática, a não ser que você tenha uma boa razão para isso.

Enfim, para criar uma tag, rodaremos o comando ``git tag <versão da sua tag>``. Caso você corra para o Github logo após rodar este comando, verá que nada aconteceu. Isso é porque sua tag **ainda não foi publicada**. Para publicar sua tag, rode: ``git push --tags``. Com isso a tarefa de compilação será iniciada e um novo patch lançado. É importante que tags sejam criadas apenas quando você tenha certeza que um novo patch deve ser publicado. É uma prática ruim criar tags para pequenas modificações diversas vezes ao dia. Limite-se a criar tags apenas quando um novo release é explicitamente necessário.

Por último, vale também lembrar que criar uma tag sem fazer mudanças locais é totalmente possível e viável. Para isto, comece com um ``git pull``, ``git tag <sua tag>`` e finalmente ``git push --tags``.

Recapitulando, este são todos os comandos que utilizamos:

```
git clone https://github.com/Monaco-a-Knox/Florescer.git
git pull
git add *
git commit -m "Mensagem de atualização"
git push origin master
git tag <versão da sua tag>
git push --tags
```

Sendo o primeiro, ``git clone``, necessário apenas para clonar o repositório para o seu computador.

## Liberando releases pelo site

Caso você tenha feito mudanças pelo site e gostaria de criar um release por ele mesmo sem lidar com a linha de comando, é muito simples:

1. Abra a aba ``releases`` do seu repositório
2. Clique em ``draft a new release``
3. Em ``tag version``, adicione a versão do patch (leia sobre tags acima)
4. Opcionalmente, preencha o título e descrição
5. Clique em ``publish release``
6. Os patches serão compilados e adicionados ao release que você criou automaticamente
