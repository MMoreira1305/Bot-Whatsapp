class Respostas:
    def __init__(self):
        pass

    def respostaInicial(self):
        return """Olá tudo bem? Sou o Suporte da loja [nome da loja], para que nosso sistema possa funcionar corretamente, digite o número da informação que você quer: 
1 - Horário de funcionamento
2 - Localização
3 - Cardápio
4 - Reserva de mesa
5 - Falar com o atendente
6 - Voltar
7 - Finalizar"""
    
    def respostaDoNumero1(self):
        return "Claro, o nosso horário de funcionamento é de terça a domingo, sendo domingos as quartas das 12h as 22h e sextas e sabados das 12h as 24h"
    
    def respostaDoNumero2(self):
        return "Ficamos localizados na Rua desembargador João Paes 565, Boa viagem, Recife"
    
    def respostaDoNumero3(self):
        link = "www.instagram.com"
        return "Claro, aqui está o cardápio\n\n" + link

    def respostaDoNumero4(self):
        return "No momento eu não consigo reservar a mesa diretamente, irei te passar com um atendente ok? Só um momento"
    
    def respostaDoNumero5(self):
        return "Claro, vou chama-lo agora"
    
    def respostaNulaComeco(self):
        return "Desculpe, no momento só consigo responder quando você digitar um número. \n\n"
    