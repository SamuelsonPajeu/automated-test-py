from automated_testing.conectar import Conectar
from automated_testing.receber_dados import ReceberDados
from dataclasses import dataclass, field


@dataclass(frozen=True, order=True)
class Main():
    c: Conectar = field(default=Conectar())
    r: ReceberDados = field(default=ReceberDados())


    def start(self):
        print("> [Main - start] starting...")
        # Conectar na DB
        self.c.start()
        # Receber dados do cliente
        self.r.start()
        # do stuff
        print("> [Main - start] done!")

    def stop(self):
        print("> [Main - stop] stopping...")
        self.c.stop()
        self.r.stop()
        print("> [Main - stop] done!")

    def dar_erro(self):
        raise Exception("Erro!")

    def nao_implementado(self):
        pass


if __name__ == "__main__":
    main = Main()
    main.start()
    main.stop()
