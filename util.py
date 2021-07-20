from models import Pessoas
#insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Lucimar', idade=42)
    print(pessoa)
    pessoa.save()

#consulta dados na tabela pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)

#altera o dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Lucimar').first()
    pessoa.idade = 25
    pessoa.save()

#exclui dados na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Lucimar').first()
    pessoa.delete()



if __name__ == '__main__':
    #insere_pessoas()
    consulta_pessoas()
    #altera_pessoa()
    #exclui_pessoa()
