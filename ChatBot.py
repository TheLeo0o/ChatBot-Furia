import time
import unicodedata
import openai

openai.api_key = "sua_api" #Tentei usar a API do OpenAI, mas acabou meu limite de créditos, então não consegui testar o código com a IA inteligente da openai, mas o código está pronto para ser testado.

print("ChatBot: Salve, torcedor(a) da FURIA! No que posso te ajudar?")
time.sleep(2)
def menu():
    print("1-Próximos jogos")
    print("2-Produtos da Loja")
    print("3-Notícias da FURIA")
    print("4-Redes sociais oficiais")
    print("5-Atendimento Especializado")

def redes_sociais():
    return("X/Twitter: https://x.com/FURIA \n "
           "Instagram: https://www.instagram.com/furiagg/ \n "
           "Facebook: https://www.facebook.com/furiagg/ \n "
           "TikTok: https://www.tiktok.com/@furia ")

def normalizar_texto(texto):
    texto = texto.lower()
    texto = unicodedata.normalize('NFKD', texto)
    texto = texto.encode('ascii', 'ignore').decode('utf-8')
    return texto

def conversar(mensagem, lista_mensagem=None):
    if lista_mensagem is None:
        lista_mensagem = [{
            "role": "system",
            "content": "Você é um assistente que só responde com informações relacionadas à equipe de e-sports FURIA. Nunca fale sobre outros assuntos."
        }]
    lista_mensagem.append({"role": "user", "content": mensagem})
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=lista_mensagem
    )

    return response

def interpreta_mensagem(mensagem):  
    comandos = [] 
    mensagem = normalizar_texto(mensagem)

    if "jogos" in mensagem or "partidas" in mensagem or "1" in mensagem or "confrontos" in mensagem or "jogo" in mensagem:
        comandos.append("1")
        
    if "produtos" in mensagem or "loja" in mensagem or  "site" in mensagem or "2" in mensagem or "mercadorias" in mensagem or "comprar" in mensagem or "camisetas" in mensagem or "roupas" in mensagem or "acessorios" in mensagem:
        comandos.append("2")
    
    if "noticias" in mensagem or "novidades" in mensagem or "3" in mensagem or "atualizacoes" in mensagem or "ultimas" in mensagem or "ultima" in mensagem:
        comandos.append("3")
    
    if "redes sociais" in mensagem or "instagram" in mensagem or "4" in mensagem or "twitter" in mensagem or "facebook" in mensagem or "tiktok" in mensagem or "social" in mensagem or "foruns" in mensagem or "forum" in mensagem or "comunidade" in mensagem or "canal" in mensagem:
        comandos.append("4")

    if "atendimento" in mensagem or "ajuda" in mensagem or "5" in mensagem or "suporte" in mensagem or "contato" in mensagem or "assistencia" in mensagem or "atendente" in mensagem:
        comandos.append("5")
    
    if "sair" in mensagem or "encerrar" in mensagem or "fechar" in mensagem or "desligar" in mensagem or "parar" in mensagem or "fim" in mensagem:
        return ["sair"]

    else:
        return comandos if comandos else  [mensagem]

def opcoes(resposta):
        if resposta == "1":
            time.sleep(1)
            return ("Aqui estão os próximos confrontos dos nossos times:\n"
            "FURIA x Apogee [06/04/2025]-[12:35]-[CS:GO]\n"
            "FURIA x Complexity [07/04/2025]-[11:05]-[CS:GO]\n"
            "FURIA x Virtus.pro [08/04/2025]-[06:05]-[CS:GO]\n"
            "FURIA x The MongolZ [08/04/2025]-[09:50]-[CS:GO]")
        
        elif resposta == "2":
            time.sleep(1)
            return("Acesse o site oficial da FURIA para conferir os produtos disponíveis: \n https://www.furia.gg/ \n Fica esperto que sempre rola cupom especial pra quem é fiel 😎")
        
        elif resposta == "3":
            time.sleep(1)
            return("Acompanhe as últimas notícias da FURIA em nosso site oficial: https://draft5.gg/major/noticias \n"
                   "E também nas redes sociais\n" + redes_sociais())
        
        elif resposta == "4":
            time.sleep(1)
            return("E Aqui estão as redes sociais \n Siga a FURIA nas redes sociais ok ein! 😎👍\n" + redes_sociais())
        
        elif resposta == "5":
            time.sleep(1)
            return("Você será direcionado para o atendimento especializado da FURIA.")
        
        else:
           return("Desculpe, não entendi 😕. Tente digitar um número de 1 a 5 ou algo como 'ver produtos', 'jogos da furia', 'notícias'...")
           
modo_atendimento = False

while True:
    if not modo_atendimento:
        menu()        
    entrada = input("Escolha uma opção ou digite uma dúvida: ") 
    resposta = interpreta_mensagem(mensagem=entrada)
    if "sair" in resposta:
        time.sleep(3)
        print("Até uma próxima Furioso(a)!👋😄")
        break
    elif isinstance(resposta, list):
        for item in resposta:
            if item in ["1", "2", "3", "4", "5"]:
                mensagem_final = opcoes(item)
                print(mensagem_final)
                time.sleep(2) 
                if item == "5":
                    modo_atendimento = True
                    print("ChatBot Profissa: Opa 😎👍 me chamou?")
            else:
                print("ChatBot Profissa: Consultando Informações...")
                ia = conversar(item)
                print("ChatBot Profissa: ", ia)
        print("Precisa de mais alguma coisa? Apenas digite um número de 1 a 5 ou digite 'sair' para encerrar.")
    elif modo_atendimento:
        print("ChatBot Profissa: Até uma próxima Furioso(a)!👋😄 ")
        modo_atendimento = False
