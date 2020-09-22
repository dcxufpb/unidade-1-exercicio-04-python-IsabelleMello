import cupom
import pytest

nome_loja = "Arcos Dourados Com. de Alimentos LTDA"
logradouro = "Av. Projetada Leste"
numero = 500
complemento = "EUC F32/33/34"
bairro = "Br. Sta Genebra"
municipio = "Campinas"
estado = "SP"
cep = "13080-395"
telefone = "(19) 3756-7408"
observacao = "Loja 1317 (PDP)"
cnpj = "42.591.651/0797-34"
inscricao_estadual = "244.898.500.113"

def test_loja_completa():
    assert cupom.dados_loja() == '''Arcos Dourados Com. de Alimentos LTDA
Av. Projetada Leste, 500 EUC F32/33/34
Br. Sta Genebra - Campinas - SP
CEP:13080-395 Tel (19) 3756-7408
Loja 1317 (PDP)
CNPJ: 42.591.651/0797-34
IE: 244.898.500.113
'''

def test_nome_vazio():
    global nome_loja
    cupom.nome_loja = ""
    with pytest.raises(Exception) as excinfo:
        cupom.dados_loja()
    the_exception = excinfo.value
    assert "O campo nome da loja é obrigatório" in str(the_exception) 
    cupom.nome_loja = "Arcos Dourados Com. de Alimentos LTDA"

def test_logradouro_vazio():
    global logradouro
    cupom.logradouro = ""
    with pytest.raises(Exception) as excinfo:
        cupom.dados_loja()
    the_exception = excinfo.value
    assert "O campo logradouro do endereço é obrigatório" in str(the_exception) 
    cupom.logradouro = "Av. Projetada Leste"

def test_numero_zero():
    global numero
    cupom.numero = 0
    assert cupom.dados_loja() == '''Arcos Dourados Com. de Alimentos LTDA
Av. Projetada Leste, s/n EUC F32/33/34
Br. Sta Genebra - Campinas - SP
CEP:13080-395 Tel (19) 3756-7408
Loja 1317 (PDP)
CNPJ: 42.591.651/0797-34
IE: 244.898.500.113
'''
    cupom.numero = 500

def test_municipio_vazio():
    global municipio
    cupom.municipio = ""
    with pytest.raises(Exception) as excinfo:
        cupom.dados_loja()
    the_exception = excinfo.value
    assert "O campo município do endereço é obrigatório" in str(the_exception) 
    cupom.municipio = "Campinas"

def test_estado_vazio():
    global estado
    cupom.estado = ""
    with pytest.raises(Exception) as excinfo:
        cupom.dados_loja()
    the_exception = excinfo.value
    assert "O campo estado do endereço é obrigatório" in str(the_exception) 
    cupom.estado = "SP"

def test_cnpj_vazio():
    global cnpj
    cupom.cnpj = ""
    with pytest.raises(Exception) as excinfo:
        cupom.dados_loja()
    the_exception = excinfo.value
    assert "O campo CNPJ da loja é obrigatório" in str(the_exception) 
    cupom.cnpj = "42.591.651/0797-34"

def test_inscricao_estadual_vazia():
    global inscricao_estadual
    cupom.inscricao_estadual = ""
    with pytest.raises(Exception) as excinfo:
        cupom.dados_loja()
    the_exception = excinfo.value
    assert "O campo inscrição estadual da loja é obrigatório" in str(the_exception) 
    cupom.inscricao_estadual = "244.898.500.113"

def test_exercicio2_customizado():
    global nome_loja
    global logradouro
    global numero
    global complemento
    global bairro
    global municipio
    global estado
    global cep
    global telefone
    global observacao
    global cnpj
    global inscricao_estadual
    
    # Defina seus próprios valores para as variáveis a seguir
    cupom.nome_loja = "Boa vista Flores"
    cupom.logradouro = "Rua Jardim Peres"
    cupom.numero = 122
    cupom.complemento = "EUC F30/31/44"
    cupom.bairro = "Centro"
    cupom.municipio = "Monteiro"
    cupom.estado = "PB"
    cupom.cep = "58500000"
    cupom.telefone = "(99) 9999-9999"
    cupom.observacao = "Loja 122 (PDB)"
    cupom.cnpj = "22.300.551/0110-56"
    cupom.inscricao_estadual = "432.118.667.777"

    #E atualize o texto esperado abaixo
    assert cupom.dados_loja() == ( 
'''Boa vista Flores
Rua Jardim Peres, 122 EUC F30/31/44
Centro - Monteiro - PB
CEP:58500000 Tel (99) 9999-9999
Loja 122 (PDB)
CNPJ: 22.300.551/0110-56
IE: 432.118.667.777
''')
