
import urllib.request
import os
import zipfile
import csv
import pygal
import lxml
import pygal_maps_world

sigla_paises_3digitos = {}
sigla_paises_3digitos["AFG"] = "Afeganistão"
sigla_paises_3digitos["ZAF"] = "África do Sul"
sigla_paises_3digitos["ALB"] = "Albânia"
sigla_paises_3digitos["DEU"] = "Alemanha"
sigla_paises_3digitos["AND"] = "Andorra"
sigla_paises_3digitos["AGO"] = "Angola"
sigla_paises_3digitos["AIA"] = "Anguila"
sigla_paises_3digitos["ATA"] = "Antártida"
sigla_paises_3digitos["ATG"] = "Antigua e Barbuda"
sigla_paises_3digitos["ANT"] = "Antilhas Holandesas"
sigla_paises_3digitos["SAU"] = "Arábia Saudita"
sigla_paises_3digitos["DZA"] = "Argélia"
sigla_paises_3digitos["ARG"] = "Argentina"
sigla_paises_3digitos["ARM"] = "Arménia"
sigla_paises_3digitos["ABW"] = "Aruba"
sigla_paises_3digitos["AUS"] = "Austrália"
sigla_paises_3digitos["AUT"] = "Áustria"
sigla_paises_3digitos["AZE"] = "Azerbaijão"
sigla_paises_3digitos["BHS"] = "Baamas"
sigla_paises_3digitos["BHS"] = "Bahamas"
sigla_paises_3digitos["BHR"] = "Bahrein"
sigla_paises_3digitos["BGD"] = "Bangladesh"
sigla_paises_3digitos["BRB"] = "Barbados"
sigla_paises_3digitos["BEL"] = "Bélgica"
sigla_paises_3digitos["BLZ"] = "Belize"
sigla_paises_3digitos["BEN"] = "Benim"
sigla_paises_3digitos["BMU"] = "Bermudas"
sigla_paises_3digitos["BLR"] = "Bielorrússia"
sigla_paises_3digitos["BOL"] = "Bolívia"
sigla_paises_3digitos["BES"] = "Bonaire, San Eustaquio y Saba"
sigla_paises_3digitos["BIH"] = "Bósnia-Herzegovina"
sigla_paises_3digitos["BWA"] = "Botsuana"
sigla_paises_3digitos["BRA"] = "Brasil"
sigla_paises_3digitos["BRN"] = "Brunei"
sigla_paises_3digitos["BGR"] = "Bulgária"
sigla_paises_3digitos["BFA"] = "Burkina Fasso"
sigla_paises_3digitos["BDI"] = "Burundi"
sigla_paises_3digitos["BTN"] = "Butão"
sigla_paises_3digitos["CPV"] = "Cabo Verde"
sigla_paises_3digitos["CMR"] = "Camarões"
sigla_paises_3digitos["KHM"] = "Camboja"
sigla_paises_3digitos["CAN"] = "Canadá"
sigla_paises_3digitos["KAZ"] = "Cazaquistão"
sigla_paises_3digitos["TCD"] = "Chade"
sigla_paises_3digitos["CHL"] = "Chile"
sigla_paises_3digitos["CHN"] = "China"
sigla_paises_3digitos["CYP"] = "Chipre"
sigla_paises_3digitos["COL"] = "Colômbia"
sigla_paises_3digitos["COM"] = "Comoras"
sigla_paises_3digitos["COG"] = "Congo"
sigla_paises_3digitos["PRK"] = "Coreia do Norte"
sigla_paises_3digitos["KOR"] = "Coreia do Sul"
sigla_paises_3digitos["CIV"] = "Costa do Marfim"
sigla_paises_3digitos["CRI"] = "Costa Rica"
sigla_paises_3digitos["HRV"] = "Croácia"
sigla_paises_3digitos["CUB"] = "Cuba"
sigla_paises_3digitos["CUW"] = "Curazao"
sigla_paises_3digitos["DNK"] = "Dinamarca"
sigla_paises_3digitos["DJI"] = "Djibouti"
sigla_paises_3digitos["DMA"] = "Dominica"
sigla_paises_3digitos["EGY"] = "Egito"
sigla_paises_3digitos["SLV"] = "El Salvador"
sigla_paises_3digitos["ARE"] = "Emirados Árabes Unidos"
sigla_paises_3digitos["ECU"] = "Equador"
sigla_paises_3digitos["ERI"] = "Eritreia"
sigla_paises_3digitos["SVK"] = "Eslováquia"
sigla_paises_3digitos["SVN"] = "Eslovênia"
sigla_paises_3digitos["ESP"] = "Espanha"
sigla_paises_3digitos["USA"] = "Estados Unidos da América"
sigla_paises_3digitos["EST"] = "Estônia"
sigla_paises_3digitos["ETH"] = "Etiópia"
sigla_paises_3digitos["FJI"] = "Fiji"
sigla_paises_3digitos["PHL"] = "Flipinas"
sigla_paises_3digitos["FIN"] = "Finlândia"
sigla_paises_3digitos["FRA"] = "França"
sigla_paises_3digitos["GAB"] = "Gabão"
sigla_paises_3digitos["GMB"] = "Gâmbia"
sigla_paises_3digitos["GHA"] = "Gana"
sigla_paises_3digitos["GEO"] = "Geórgia"
sigla_paises_3digitos["GIB"] = "Gibraltar"
sigla_paises_3digitos["GBR"] = "Grã-Bretanha"
sigla_paises_3digitos["GRD"] = "Granada"
sigla_paises_3digitos["GRC"] = "Grécia"
sigla_paises_3digitos["GRL"] = "Gronelândia"
sigla_paises_3digitos["GLP"] = "Guadalupe"
sigla_paises_3digitos["GUM"] = "Guam"
sigla_paises_3digitos["GTM"] = "Guatemala"
sigla_paises_3digitos["GGY"] = "Guernsey"
sigla_paises_3digitos["GUY"] = "Guiana"
sigla_paises_3digitos["GUF"] = "Guiana Francesa"
sigla_paises_3digitos["GIN"] = "Guiné"
sigla_paises_3digitos["GNQ"] = "Guinea Ecuatorial"
sigla_paises_3digitos["GNQ"] = "Guiné Equatorial"
sigla_paises_3digitos["GNB"] = "Guiné-Bissau"
sigla_paises_3digitos["HTI"] = "Haiti"
sigla_paises_3digitos["NLD"] = "Holanda"
sigla_paises_3digitos["HND"] = "Honduras"
sigla_paises_3digitos["HKG"] = "Hong Kong"
sigla_paises_3digitos["HUN"] = "Hungria"
sigla_paises_3digitos["YEM"] = "Iémen"
sigla_paises_3digitos["BVT"] = "Ilhas Bouvet"
sigla_paises_3digitos["IMN"] = "Ilha de Man"
sigla_paises_3digitos["CXR"] = "Ilha do Natal"
sigla_paises_3digitos["PCN"] = "Ilha Pitcairn"
sigla_paises_3digitos["REU"] = "Ilha Reunião"
sigla_paises_3digitos["ALA"] = "Ilhas Aland"
sigla_paises_3digitos["CYM"] = "Ilhas Cayman"
sigla_paises_3digitos["CCK"] = "Ilhas Cocos"
sigla_paises_3digitos["COM"] = "Ilhas Comores"
sigla_paises_3digitos["COK"] = "Ilhas Cook"
sigla_paises_3digitos["FRO"] = "Ilhas Faroé"
sigla_paises_3digitos["SGS"] = "Ilhas Geórgia do Sul e Sandwich do Sul"
sigla_paises_3digitos["HMD"] = "Ilhas Heard e McDonald"
sigla_paises_3digitos["MNP"] = "Ilhas Marianas do Norte"
sigla_paises_3digitos["MHL"] = "Ilhas Marshall"
sigla_paises_3digitos["FLK"] = "Ilhas Malvinas"
sigla_paises_3digitos["UMI"] = "Ilhas Menores dos Estados Unidos"
sigla_paises_3digitos["NFK"] = "Ilhas Norfolk"
sigla_paises_3digitos["CXR"] = "Ilha de Páscoa"
sigla_paises_3digitos["SYC"] = "Ilhas Seychelles"
sigla_paises_3digitos["SLB"] = "Ilhas Salomão"
sigla_paises_3digitos["SJM"] = "Ilhas Svalbard e Jan Mayen"
sigla_paises_3digitos["TKL"] = "Ilhas Tokelau"
sigla_paises_3digitos["TCA"] = "Ilhas Turks e Caicos"
sigla_paises_3digitos["VIR"] = "Ilhas Virgens (EUA)"
sigla_paises_3digitos["VGB"] = "Ilhas Vírgens Britânicas"
sigla_paises_3digitos["WLF"] = "Ilhas Wallis e Futuna"
sigla_paises_3digitos["IND"] = "Índia"
sigla_paises_3digitos["IDN"] = "Indonésia"
sigla_paises_3digitos["IRN"] = "Irão"
sigla_paises_3digitos["IRQ"] = "Iraque"
sigla_paises_3digitos["IRL"] = "Irlanda"
sigla_paises_3digitos["ISL"] = "Islândia"
sigla_paises_3digitos["ISR"] = "Israel"
sigla_paises_3digitos["ITA"] = "Itália"
sigla_paises_3digitos["JAM"] = "Jamaica"
sigla_paises_3digitos["JPN"] = "Japão"
sigla_paises_3digitos["JEY"] = "Jersey"
sigla_paises_3digitos["JOR"] = "Jordânia"
sigla_paises_3digitos["KIR"] = "Kiribati"
sigla_paises_3digitos["KWT"] = "Kuwait"
sigla_paises_3digitos["LAO"] = "Laos"
sigla_paises_3digitos["LVA"] = "Letônia"
sigla_paises_3digitos["LSO"] = "Lesoto"
sigla_paises_3digitos["LBN"] = "Líbano"
sigla_paises_3digitos["LBR"] = "Libéria"
sigla_paises_3digitos["LBY"] = "Líbia"
sigla_paises_3digitos["LIE"] = "Liechtenstein"
sigla_paises_3digitos["LTU"] = "Lituânia"
sigla_paises_3digitos["LUX"] = "Luxemburgo"
sigla_paises_3digitos["MAC"] = "Macau"
sigla_paises_3digitos["MKD"] = "Macedônia"
sigla_paises_3digitos["MDG"] = "Madagascar"
sigla_paises_3digitos["MYS"] = "Malásia"
sigla_paises_3digitos["MWI"] = "Malaui"
sigla_paises_3digitos["MDV"] = "Maldivas"
sigla_paises_3digitos["MLI"] = "Mali"
sigla_paises_3digitos["MLT"] = "Malta"
sigla_paises_3digitos["MAR"] = "Marrocos"
sigla_paises_3digitos["MTQ"] = "Martinica"
sigla_paises_3digitos["MUS"] = "Maurício"
sigla_paises_3digitos["MRT"] = "Mauritânia"
sigla_paises_3digitos["MYT"] = "Mayotte"
sigla_paises_3digitos["MEX"] = "México"
sigla_paises_3digitos["FSM"] = "Micronésia"
sigla_paises_3digitos["MOZ"] = "Moçambique"
sigla_paises_3digitos["MDA"] = "Moldávia"
sigla_paises_3digitos["MCO"] = "Mônaco"
sigla_paises_3digitos["MNG"] = "Mongólia"
sigla_paises_3digitos["MNE"] = "Montenegro"
sigla_paises_3digitos["MSR"] = "Montserrat"
sigla_paises_3digitos["MMR"] = "Myanmar"
sigla_paises_3digitos["NAM"] = "Namíbia"
sigla_paises_3digitos["NRU"] = "Nauru"
sigla_paises_3digitos["NPL"] = "Nepal"
sigla_paises_3digitos["NIC"] = "Nicarágua"
sigla_paises_3digitos["NER"] = "Níger"
sigla_paises_3digitos["NGA"] = "Nigéria"
sigla_paises_3digitos["NIU"] = "Niue"
sigla_paises_3digitos["NOR"] = "Noruega"
sigla_paises_3digitos["NCL"] = "Nova Caledônia"
sigla_paises_3digitos["NZL"] = "Nova Zelândia"
sigla_paises_3digitos["OMN"] = "Omã"
sigla_paises_3digitos["PLW"] = "Palau"
sigla_paises_3digitos["PAN"] = "Panamá"
sigla_paises_3digitos["PNG"] = "Papua-Nova Guiné"
sigla_paises_3digitos["PAK"] = "Paquistão"
sigla_paises_3digitos["PRY"] = "Paraguai"
sigla_paises_3digitos["PER"] = "Peru"
sigla_paises_3digitos["PYF"] = "Polinésia Francesa"
sigla_paises_3digitos["POL"] = "Polônia"
sigla_paises_3digitos["PRI"] = "Porto Rico"
sigla_paises_3digitos["PRT"] = "Portugal"
sigla_paises_3digitos["QAT"] = "Qatar"
sigla_paises_3digitos["KEN"] = "Quênia"
sigla_paises_3digitos["KGZ"] = "Quirguistão"
sigla_paises_3digitos["CAF"] = "República Centro-Africana"
sigla_paises_3digitos["COD"] = "República Democrática do Congo"
sigla_paises_3digitos["DOM"] = "República Dominicana"
sigla_paises_3digitos["CZE"] = "República Checa"
sigla_paises_3digitos["ROM"] = "Romênia"
sigla_paises_3digitos["RWA"] = "Ruanda"
sigla_paises_3digitos["RUS"] = "Rússia"
sigla_paises_3digitos["ESH"] = "Saara Ocidental"
sigla_paises_3digitos["VCT"] = "São Vicente e Granadinas"
sigla_paises_3digitos["ASM"] = "Samoa Americana"
sigla_paises_3digitos["WSM"] = "Samoa Ocidental"
sigla_paises_3digitos["SMR"] = "San Marino"
sigla_paises_3digitos["SHN"] = "Santa Helena"
sigla_paises_3digitos["LCA"] = "Santa Lúcia"
sigla_paises_3digitos["BLM"] = "São Bartolomeu"
sigla_paises_3digitos["KNA"] = "São Cristóvão e Névis"
sigla_paises_3digitos["MAF"] = "São Martim"
sigla_paises_3digitos["STP"] = "São Tomé e Príncipe"
sigla_paises_3digitos["SEN"] = "Senegal"
sigla_paises_3digitos["SLE"] = "Serra Leoa"
sigla_paises_3digitos["SRB"] = "Sérvia"
sigla_paises_3digitos["SGP"] = "Singapura"
sigla_paises_3digitos["SYR"] = "Síria"
sigla_paises_3digitos["SOM"] = "Somália"
sigla_paises_3digitos["LKA"] = "Sri Lanka"
sigla_paises_3digitos["SPM"] = "São Pedro e Miquelon"
sigla_paises_3digitos["SWZ"] = "Suazilândia"
sigla_paises_3digitos["SDN"] = "Sudão"
sigla_paises_3digitos["SWE"] = "Suécia"
sigla_paises_3digitos["CHE"] = "Suíça"
sigla_paises_3digitos["SUR"] = "Suriname"
sigla_paises_3digitos["TJK"] = "Tajiquistão"
sigla_paises_3digitos["THA"] = "Tailândia"
sigla_paises_3digitos["TWN"] = "Taiwan"
sigla_paises_3digitos["TZA"] = "Tanzânia"
sigla_paises_3digitos["IOT"] = "Território Britânico do Oceano Índico"
sigla_paises_3digitos["ATF"] = "Território do Sul da França"
sigla_paises_3digitos["PSE"] = "Território Palestino Ocupado"
sigla_paises_3digitos["TMP"] = "Timor Leste"
sigla_paises_3digitos["TGO"] = "Togo"
sigla_paises_3digitos["TON"] = "Tonga"
sigla_paises_3digitos["TTO"] = "Trinidad e Tobago"
sigla_paises_3digitos["TUN"] = "Tunísia"
sigla_paises_3digitos["TKM"] = "Turcomenistão"
sigla_paises_3digitos["TUR"] = "Turquia"
sigla_paises_3digitos["TUV"] = "Tuvalu"
sigla_paises_3digitos["UKR"] = "Ucrânia"
sigla_paises_3digitos["UGA"] = "Uganda"
sigla_paises_3digitos["URY"] = "Uruguai"
sigla_paises_3digitos["UZB"] = "Usbequistão"
sigla_paises_3digitos["VUT"] = "Vanuatu"
sigla_paises_3digitos["VAT"] = "Vaticano"
sigla_paises_3digitos["VEN"] = "Venezuela"
sigla_paises_3digitos["VNM"] = "Vietnã"
sigla_paises_3digitos["ZMB"] = "Zâmbia"
sigla_paises_3digitos["ZWE"] = "Zimbabué"

# lista para receber o arquivo numero_identificador_lattes_zzzz.csv
identificador_list_cvs = list()
# dicionario para receber o arquivo tab_area_conhecimento_zzzz.csv
area_dict_csv = {}
# dicionario para receber o arquivo tab_nivel_formacao_zzzz.csv
nivel_formacao_dict_csv = {}

# url dos arquivos da plataforma lattes, disponivel em:  http://memoria.cnpq.br/web/portal-lattes/extracoes-de-dados
url = "http://memoria.cnpq.br/documents/313759/6935115b-a5e8-4cfb-96cf-00e2fd11c96c"
print("URL lattes: " + url)

# definicao do arquivo destino na maquina do usuario
arquivo_lattes = os.path.expanduser("~/lattes.zip")
print("Arquivo de download destino: " + arquivo_lattes)

dir_destino = os.path.dirname(arquivo_lattes)
print("Diretório de trabalho local: " + dir_destino)

print("Iniciando download do arquivo na plataforma lattes. Processo demorado...")
urllib.request.urlretrieve(url, arquivo_lattes)
print("Download concluído: " + arquivo_lattes)

print("Descompactando o arquivo ZIP... ")
with zipfile.ZipFile(arquivo_lattes, "r") as zip_ref:
    zip_ref.extractall(dir_destino)
print("Arquivos da plataforma lattes extraídos em: " + dir_destino)

def importa_csv_para_lista(arq):
    print("Importando o arquivo: " + arq + " para estrutura de dados em memória a fim de permitir análise.")
    with open(arq, 'r', encoding='latin-1') as f:
        reader = csv.reader(f, delimiter=';')
        lista = list(reader)
    print("Importação do arquivo: " + arq + " para a memória concluída.")
    return lista

def importa_csv_para_dicionario(arq):
    print("Importando o arquivo: " + arq + " para estrutura de dados em memória a fim de permitir análise.")
    dicionario = {}
    reader = csv.reader(open(arq, 'r', encoding='latin-1'))
    for row in reader:
        aux_linha = row[0]
        aux_linha_str = aux_linha.split(";")
        chave = aux_linha_str[0]
        valor = aux_linha_str[1]
        dicionario[chave] = valor
    print("Importação do arquivo: " + arq + " para a memória concluída.")
    return dicionario


for file in os.listdir(dir_destino):
    if file.endswith(".csv"):
        if file.startswith("numero_identificador_lattes"):
            identificador_arq = os.path.join(dir_destino, file)
            identificador_list_cvs = importa_csv_para_lista(identificador_arq)

        if file.startswith("tab_area_conhecimento"):
            area_arq = os.path.join(dir_destino, file)
            area_dict_csv = importa_csv_para_dicionario(area_arq)

        if file.startswith("tab_nivel_formacao"):
            nivel_arq = os.path.join(dir_destino, file)
            nivel_formacao_dict_csv = importa_csv_para_dicionario(nivel_arq)

# o algoritmo deve varrer a lista do identificador que eh o arquivo principal
# analisar cada linha do arquivo e trabalhar com geraçao estatistica
# em estruturas de dados em python, denominadas dicionario

nacionalidade_dict = {}
area_conhecimento_dict = {}
nivel_formacao_dict = {}

i = 1
valor = 0
while i < len(identificador_list_cvs):
    # le a linha
    aux_linha = identificador_list_cvs[i]
    # e extrai as strings para cada estatistica
    aux_nacionalidade = aux_linha[1]
    aux_area = aux_linha[3]
    aux_nivel = aux_linha[4]

    # trata a estatistica da nacionalidade
    valor_nacionalidade = nacionalidade_dict.get(aux_nacionalidade)
    if valor_nacionalidade is None:
        nacionalidade_dict[aux_nacionalidade] = 1
    else:
        valor_nacionalidade = valor_nacionalidade + 1
        nacionalidade_dict[aux_nacionalidade] = valor_nacionalidade

    # trata a estatistica da area de conhecimento
    valor_area = area_conhecimento_dict.get(aux_area)
    if valor_area is None:
        area_conhecimento_dict[aux_area] = 1
    else:
        valor_area = valor_area + 1
        area_conhecimento_dict[aux_area] = valor_area

    # trata a estatistica do nivel de formacao
    valor_nivel = nivel_formacao_dict.get(aux_nivel)
    if valor_nivel is None:
        nivel_formacao_dict[aux_nivel] = 1
    else:
        valor_nivel = valor_nivel + 1
        nivel_formacao_dict[aux_nivel] = valor_nivel

    i = i + 1

print(nacionalidade_dict.items())
print(area_conhecimento_dict.items())
print(nivel_formacao_dict.items())

# tratar os dicionarios para estruturas de listas
# a fim de permitir ordenacao e gerar graficos de melhor leitura
nacionalidade_list = list()
nacionalidade_list = sorted(nacionalidade_dict.items(), key = lambda x: x[1], reverse=True )

area_list = list()
area_list = sorted(area_conhecimento_dict.items(), key = lambda x: x[1], reverse=True)

nivel_formacao_list = list()
nivel_formacao_list = sorted(nivel_formacao_dict.items(), key = lambda x: x[1], reverse=True)


# ######################################################
# GRAFICOS
# gerar o grafico de barras de pesquisadores estrageiros
nacionalidade_chart = pygal.HorizontalBar()
nacionalidade_chart.title = 'Pesquisadores estrangeiros cadastrados na Plataforma Lattes'
i = 0
while i < len(nacionalidade_list):
    aux_linha = nacionalidade_list[i]
    aux_nacionalidade = aux_linha[0]
    valor_nacionalidade = aux_linha[1]
    if aux_nacionalidade != "BRA":
        nacionalidade_chart.add(aux_nacionalidade, valor_nacionalidade)
    i = i + 1
nacionalidade_chart.render_in_browser()

# gerar o grafico/mapa de pesquisadores por paises (incluindo Brasil desta vez)
worldmap_chart = pygal.maps.world.World()
worldmap_chart.title = 'Pesquisadores cadastrados na plataforma Lattes - por países.'
worldmap_chart.add('Mês/Ano', {
  'af': 14,
  'bd': 1,
  'by': 3,
  'cn': 1000,
  'gm': 9,
  'in': 1,
  'ir': 314,
  'iq': 129,
  'jp': 7
})
worldmap_chart.render_in_browser()

# gerar o grafico de area de atuaçao
area_chart = pygal.HorizontalBar()
area_chart.title = "Área de atuação dos pesquisadores"
i = 0
while i < len(area_list):
    aux_linha = area_list[i]
    aux_area = aux_linha[0]
    aux_area_extenso = area_dict_csv.get(aux_area)
    valor_area = aux_linha[1]
    if bool(aux_area_extenso and aux_area_extenso.strip()):
        area_chart.add(aux_area_extenso, valor_area)
    i = i + 1
area_chart.render_in_browser()

# gerar o grafico de nivel de formacao
nivel_formacao_chart = pygal.HorizontalBar()
nivel_formacao_chart.title = "Nível de formação dos pesquisadores"
i = 0
while i < len(nivel_formacao_list):
    aux_linha = nivel_formacao_list[i]
    aux_nivel = aux_linha[0]
    if (bool(aux_nivel and aux_nivel.strip())):
        aux_nivel_extenso = nivel_formacao_dict_csv.get(aux_nivel)
    else:
        aux_nivel_extenso = "Não informado"
    valor_nivel = aux_linha[1]
    nivel_formacao_chart.add(aux_nivel_extenso, valor_nivel)
    i = i + 1
nivel_formacao_chart.render_in_browser()




# excluir os arquivos de download no final do processo
print("Excluindo o arquivo: " + arquivo_lattes + " após a descompactação.")
#os.remove(file_name)
print("Excluindo o arquivo: " + identificador_arq)
#os.remove(arquivo_identificador)
print("Excluindo o arquivo: " + area_arq)
#os.remove(arquivo_area)
print("Excluindo o arquivo: " + nivel_arq)
#os.remove(arquivo_nivel)

