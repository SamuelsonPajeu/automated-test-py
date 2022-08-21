# ao rodar o pytest, ele vai buscar pela pasta tests e executar todos os 
# métodos que comecem com test_ e estejam dentro dos arquivos que começam com test_[...].py

# @pytest.mark.skip(reason="Not implemented yet") <= Vai pular o teste naquele metodo
# @pytest.mark.xfail(reason="Not implemented yet") <= Vai ignorar o erro e continuar o teste
# with pytest.raises(Exception) as e: <= Vai esperar que o teste lance uma exceção, e vai falhar caso não dê o erro

# @pytest.fixture(scope="session") <= Cria uma fixture que vai ser executada apenas uma vez durante toda a sessão de testes 
# (Ex, uma coenxão com o banco de dados)
import pytest
from automated_testing import main as m


class Mock():
    def start(self):
        print("> [Mock] start ...")

    def stop(self):
        print("> [Mock] stop ...")


# Executa o teste de forma geral, desse jeito, o main.start chama o Conectar.start e o ReceberDados.start, 
# porém existe um erro no Receber dados, o que causa a falha do teste
def test_main_without_mock():
    main = m.Main()
    # Com o pytest.raises, o teste espera que o método dar_erro lance uma exceção do tipo declarado, caso não lance, o teste falha
    with pytest.raises(Exception):
        main.start()
    assert main.stop() is None


# Com a injeção de dependência, o main.start chama o Mock.start o que permite que o teste seja realizado 
# apenas dentro da função main, isolando o teste
def test_main_with_mock():
    main = m.Main(Mock(), Mock())
    assert main.start() is None
    assert main.stop() is None


# Com o mark.xfail, o teste ignora o erro e continua a execução
@pytest.mark.xfail(reason="Erro Proposital")
def test_xfail():
    m.Main().dar_erro()
