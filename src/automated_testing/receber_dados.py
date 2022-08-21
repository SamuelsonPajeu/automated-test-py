class ReceberDados():
    def start(self):
        print("> [ReceberDados - start] Recebendo dados do cliente X...")
        raise Exception("Erro!")
        # print("> [ReceberDados - start] Dados: {}...")

    def stop(self):
        print("> [ReceberDados - stop] Atualizando dados do cliente X antes de desconectar...")
        self.atualizar()
        # do stuff
        print("> [ReceberDados - stop] Cliente desconectado...")

    def atualizar(self):
        print("> [ReceberDados - atualizar] Atualizando dados do cliente X...")
        # do stuff
        print("> [ReceberDados - atualizar] Dados atualizados...")
