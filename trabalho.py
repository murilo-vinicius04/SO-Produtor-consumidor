import threading
import time
import random
from queue import Queue

# Buffer e Semáforos
tamanho_buffer = 5
buffer = Queue(tamanho_buffer)
sem_espacos = threading.Semaphore(tamanho_buffer)
sem_itens = threading.Semaphore(0)
mutex = threading.Lock()

contador_espacos = tamanho_buffer 
contador_itens = 0
contador_lock = threading.Lock()

# Lista de nomes brasileiros comuns
nomes = [
    "Maria da Conceição",
    "João Vicente",
    "Ana Paula",
    "Carlos Eduardo",
    "Fernanda Lima",
    "Lucas Oliveira",
    "Mariana Silva",
    "Pedro Albuquerque",
    "Juliana Martins",
    "Ricardo Santos"
]

# Lista de arquivos comuns que as pessoas imprimem
arquivos = [
    "trabalho_fisica.pdf",
    "recibo.pdf",
    "apostila_matematica.pdf",
    "lista_de_compras.pdf",
    "olerite.pdf",
    "relatorio_atividade.pdf",
    "projeto_final.pdf",
    "resumo_quimica.pdf",
    "exercicio_programacao.pdf",
    "anotacoes_aula.pdf"
]

def exibir_estado_semaforos():
    with contador_lock:
        print(f"  [Semáforos] Espaços: {contador_espacos} | Itens: {contador_itens}")

def produzir_item():
    nome = random.choice(nomes)
    arquivo = random.choice(arquivos)
    return f"{nome} - {arquivo}"

def consumir_item(item):
    print(f"[Impressora] Consumiu '{item}'")

def produtor(nome):
    global contador_espacos, contador_itens
    while True:
        item = produzir_item()
        sem_espacos.acquire()
        with contador_lock:
            contador_espacos -= 1

        mutex.acquire()
        buffer.put(item)
        print(f"[{nome}] Enviou '{item}' para impressão | Buffer: {list(buffer.queue)}")
        mutex.release()

        sem_itens.release()
        with contador_lock:
            contador_itens += 1

        exibir_estado_semaforos()

def consumidor(nome):
    global contador_espacos, contador_itens
    while True:
        sem_itens.acquire()
        with contador_lock:
            contador_itens -= 1

        mutex.acquire()
        item = buffer.get()
        print(f"[{nome}] Retirou '{item}' da fila | Buffer: {list(buffer.queue)}")
        mutex.release()

        sem_espacos.release()
        with contador_lock:
            contador_espacos += 1

        exibir_estado_semaforos()
        consumir_item(item)

def modo_interativo():
    global contador_espacos, contador_itens
    print("Modo Interativo Iniciado! Pressione:")
    print("'e' para enviar impressão  'p' para processar impressão | 'q' para sair")

    while True:
        acao = input("Ação: ").lower()
        if acao == 'e':
            if sem_espacos.acquire(blocking=False):
                with contador_lock:
                    contador_espacos -= 1

                mutex.acquire()
                item = produzir_item()
                buffer.put(item)
                print(f"[Você] Enviou '{item}' para impressão | Buffer: {list(buffer.queue)}")
                mutex.release()

                sem_itens.release()
                with contador_lock:
                    contador_itens += 1

                exibir_estado_semaforos()
            else:
                print("[!] Fila cheia! Aguarde processamento.")
        elif acao == 'p':
            if sem_itens.acquire(blocking=False):
                with contador_lock:
                    contador_itens -= 1

                mutex.acquire()
                item = buffer.get()
                print(f"[Você] Processou '{item}' da fila | Buffer: {list(buffer.queue)}")
                mutex.release()

                sem_espacos.release()
                with contador_lock:
                    contador_espacos += 1

                exibir_estado_semaforos()
                consumir_item(item)
            else:
                print("[!] Fila vazia! Aguarde envios.")
        elif acao == 'q':
            print("Encerrando modo interativo.")
            break
        else:
            print("Comando inválido.")

def main():
    print("=== Simulador de Impressão (Produtor-Consumidor) ===")

    try:
        modo_interativo()
    except KeyboardInterrupt:
        print("\nEncerrando...")

if __name__ == "__main__":
    main()
