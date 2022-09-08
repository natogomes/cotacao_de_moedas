"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install -e .`
- Use the same interpreter as the one used to install the bot (`pip install -e .`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""

from botcity.web import WebBot, Browser
from interface_grafica import *


class Bot(WebBot):
    def action(self, execution=None):
        # Configure whether or not to run on headless mode
        self.headless = False

        # Uncomment to change the default Browser to Firefox
        # self.browser = Browser.FIREFOX

        # Uncomment to set the WebDriver path
        self.driver_path = "./chromedriver.exe"

        # Inicia a janela do programa
        win_inicial()
        while True:
            window, event, values = sg.read_all_windows()
            moeda_sai = values['moeda_sai']
            moeda_ent = values['moeda_ent']

            if event == sg.WIN_CLOSED:
                self.stop_browser()
                break

            elif event == 'Sair':
                self.stop_browser()
                break

            elif event == 'Pesquisar':

                window['saida'].update('')

                # Abre o navegador
                self.browse("https://www.google.com")
                self.maximize_window()

                if moeda_ent == '':
                    sg.Popup('Preencha o campo "De:"', font='arial 12', title='Erro')
                else:
                    from datetime import datetime
                    data_hora = datetime.today()

                    # Clica em pesquisar do google
                    if not self.find( "pesquisar", matching=0.97, waiting_time=10000):
                        self.not_found("pesquisar")
                    self.click()
                    self.paste(f'Cotação {moeda_ent}')
                    self.enter()

                    # Clica para escolher a moeda para qual será cotada
                    if not self.find( "saida", matching=0.97, waiting_time=10000):
                        self.not_found("saida")
                    self.click()
                    cont = 0
                    for moeda in moedas:
                        cont += 1
                        if moeda == moeda_sai:

                            # 115 é a posição que se encontra o Real brasileiro que já é automático para o Brasil
                            if cont > 115:
                                passou = cont - 115
                                for c in range(0, passou):
                                    self.type_down(0)
                                self.enter()
                            else:
                                faltou = 115 - cont
                                for c in range(0, faltou):
                                    self.type_up(0)
                                self.enter()

                    # Clique relativo para chegar no valor final
                    if not self.find( "valor_relative", matching=0.97, waiting_time=10000):
                        self.not_found("valor_relative")
                    self.triple_click_relative(-520, 205)
                    self.wait(1000)
                    self.control_c()
                    cotacao = self.get_clipboard()
                    data = datetime.strftime(data_hora, "%d/%m/%y - %H:%Mh")
                    print(f'<< 1 {moeda_ent} igual a: >>')
                    print(cotacao)
                    print(f'{data:>78}', end='')
                    self.stop_browser()

        # Wait for 10 seconds before closing
        # self.wait(10000)

        # Stop the browser and clean up
        # self.stop_browser()

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()

