from datetime import datetime
import time
import rpa
from git import Repo

# git.cmd.Git().pull('https://github.com/rarikmilkrai/TesteTelegram.git', 'master')

# C:\Users\rarsilva\OneDrive - Capgemini\Documents\MeusProjetos\TesteTelegram.git

# repo.index.checkout


# verificar essa forma de fazer
# g = git.Git('git-repo')
# g.pull('origin','branch-name')


#  repo.remotes.origin.pull("master")


PATH_OF_GIT_REPO = r'C:CAMINHO DO SEU REPOSITORIO LOCAL AQUI.git'
COMMIT_MESSAGE = 'feito o push'


def git_pull():
    try:
        print('Entrou no metodo')
        repo = Repo(PATH_OF_GIT_REPO)  # variavel do repositorio local
        print(repo.index.checkout)
       # repo.git.add(update=True)
        # repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')  # pasta origem remota
        origin.pull()
    except:
        print('Some error occurred while pushing the code')




rarik_id = '' # você consegue esse id enviando uma mensagem para o boot do rpa no telegram.
mensagem = "Rarik,Error:"
# data = datetime.now()

# data_string = datetime.now().strftime('%H:%M:%S -- %d/%m/%Y ')



if __name__ == '__main__':

    git_pull()

    while True:
        # É PRECISO MODIFICAR A DATA PARA A VERSÃO BRASILEIRA = HORA:MINUTO:SEGUNDO--DIA/MES/ANO
        data_string = datetime.now().strftime('%H:%M:%S -- %d/%m/%Y ')
        rpa.telegram(rarik_id, mensagem + data_string)

        # rpa.telegram(rarik_id, mensagem + datetime.now().strftime('%H:%M:%S - %d/%m/%Y')

        if datetime.now().strftime('%H:%M:%S -- %d/%m/%Y') == 8: # aqui eu digo que é para me mandar mensagem ate as 8 da manhã.
            break
        break



    time.sleep(60)

# URL = "https://api.telegram.org/bot5686938871:
# AAEe-lmqtIIIcFb6M7NXdld48v998eYvGKo/sendMessage?
# chat_id=5063949626&text= Rarik,Error: " + data_string

# resposta = requests.get(URL)

# print(resposta.json())
