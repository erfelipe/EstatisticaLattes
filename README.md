# EstatisticaLattes

Trabalho para a disciplina ZZZ na Universidade Federal de Minas Gerais 

Professor: Renato Rocha - FGV  [lattes] [github] 
Aluno: Eduardo R Felipe - UFMG [lattes] [github] 

# Considerações iniciais
<img src="https://github.com/erfelipe/EstatisticaLattes/blob/master/img/lattes.jpg" alt="Lattes Público?">
Embora o currículo lattes seja divulgado como uma base de dados pública, o acesso aos dados é protegido contra acessos de algoritmos de pesquisa e varredura de dados automatizadas, o que impede que mecanismos de busca seja utilizados para um levantamento estatístico especializado. 

O cnpq lattes divulga em sua página: <a href="http://memoria.cnpq.br/web/portal-lattes/extracoes-de-dados" target="_blank">http://memoria.cnpq.br/web/portal-lattes/extracoes-de-dados</a> que há uma possibilidade de acesso à base para extração por meio de uma ferramenta específica chamada Lattes Extrator. Mediante o envio de um cadastro com diversas informações da instituição de ensino e da assinatura de seu diretor, inicia-se um processo de liberação da ferramenta. Infelizmente neste projeto não foi possível aguardar a liberação do mesmo. Neste momento há mais de 30 dias de aguardo da liberação da ferramenta e não há nenhuma resposta ou previsão para o acesso.

Desta forma o projeto foi alterado a fim de utilizar alguns dados publicados em formato CSV no site da plataforma, contendo basicamente os IDs dos currículos, suas áreas de atuação e formação profissional dos participantes na plataforma.

Estranha-se o fato de uma empresa privada denominada: StelaExperta <a href="http://site.stelaexperta.com.br" target="_blank"> http://site.stelaexperta.com.br </a> possuir e COMERCIALIZAR dados da plataforma Lattes. Empresa que se descreve em seu site como: "A Stela Experta© foi criada pela equipe que desenvolveu a Plataforma Lattes." 

Portanto, como uma base de dados pública pode ter seu acesso para análise dificultado para instituições de ensino e/ou público em geral, mas ser comercializada pela "equipe que a desenvolveu"? 

# Introdução

A base de dados Lattes é uma referência aceita amplamente no meio acadêmico para registrar informações de formação profissional e acadêmico. A extensa maioria das instituições de ensino consideram o currículo Lattes como ferramenta oficial na busca por informações de alunos, professores e profissionais de diversas áreas. 

A intenção governamental de padronizar e centralizar o acesso obteve êxito neste processo. Seu acesso porém é limitado à ação humana por meio de mecanismo de validação (<a href="https://pt.wikipedia.org/wiki/CAPTCHA" target="_blank"> capcha</a>) impedindo que algoritmos automatizados possam extrair informações e gerar estatísticas. 

# Desenvolvimento

Este trabalho foi desenvolvido com base em algoritmo e bibliotecas Python. Foram utilizadas as seguintes ferramentas de desenvolvimento: 
- Python 3.6
- IDE PyCharm (versão educacional) 
- Jupyter Notebook 

A análise foi limitada a utilizar os arquivos em formato textual (CVS) divulgados na plataforma Lattes denominados: ID dos Currículos Lattes. 
No site da plataforma:  <a href="http://memoria.cnpq.br/web/portal-lattes/extracoes-de-dados" target="_blank">http://memoria.cnpq.br/web/portal-lattes/extracoes-de-dados</a> pode-se ter acesso a um arquivo compactado em formato <a href="https://pt.wikipedia.org/wiki/ZIP" target="_blank">ZIP</a> que por sua vez contém três arquivos textos ao ser descompactado: 
- numero_identificador_lattes_zzzzzzzz.cvs
- tab_area_conhecimento_zzzzzzzz.cvs 
- tab_nivel_formacao_zzzzzzzz.csv
onde zzzzzzzz possui informações sobre ano, mes e dia da geração do arquivo. 

Arquivos em formato CVS são arquivos texto sem formatação (negrito, itálico, etc...) com dados separados por alguma pontuação como ponto e vírgula ou somente vírgula. 

Cada arquivo possui a seguinte estrutura: 

numero_identificador_lattes_.cvs - este é o maior e principal arquivo da distribuição.  Possui o ID do currículo lattes e três outras informações usadas neste trabalho: nacionalidade, a área do conhecimento e o nível de formação. Que pode ser visto conforme o cabeçalho do arquivo abaixo. Importante notar que diversos registros (linhas) não possuem todas as informações, como na primeira linha de dados do exemplo abaixo. 
NUMERO_IDENTIFICADOR;PAIS_NACIONALIDADE_ISO3;DATA_ATUALIZACAO;COD_AREA_CONHEC;COD_NIVEL_FORMACAO
7739792697883557;BRA;29/09/2009 18:36:17;;2
8871954517195536;BRA;14/10/2015 20:17:54;60400005;C

tab_area_conhecimento_zzzzzzzz.cvs - neste arquivo há a tradução do código da área de conhecimento para três idiomas: Português, inglês e espanhol.
COD_AREA_CONHEC;NOME_AREA_CONHEC;NOME_AREA_CONHEC_EN;NOME_AREA_CONHEC_ES
60500000;Planejamento Urbano e Regional;Urban and Regional Planning;Planeamiento Urbano y Regional
10100008;Matemática;Mathematics;Matemática

tab_nivel_formacao_zzzzzzzz.csv - este arquivo apresenta a tradução do código do nível de formação para três idiomas: Português, inglês e espanhol. 
COD_NIVEL_FORM;DSC_NIVEL_FORM;DSC_NIVEL_FORM_EN;DSC_NIVEL_FORM_ES
Y;Outros;Others;Otro
3;Mestrado;Master's;Maestria
4;Doutorado;Doctorate;Doctorado

O processamento ocorre no algoritmo em Python, considerando o arquivo numero_identificador_lattes como referência principal para a contagem estatística. Na medida que este arquivo possui todos os identificadores de currículos cadastrados, a contagem e agrupamento de dados é feito por meio de um laço de repetição na estrutura de dados referente a este arquivo.

O algoritmo utiliza estruturas "dicionário" e "listas" para o tratamento de dados. 

Os outros dois arquivos atuam na tradução dos códigos para uma identificação por extenso da área de conhecimento e do nível de formação. Estes rótulos serão usados na identificação de cada área/nível na apresentação dos gráficos. 

Para geração dos gráficos estatísticos foi usada a biblioteca Python <a href="http://www.pygal.org/en/stable/" target="_blank">pyGal</a> que permite a apresentação em browser. O projeto ainda apresenta uma dificuldade na exibição de caracteres latinos (com acentuação) e 


# Considerações finais 



# Referências

