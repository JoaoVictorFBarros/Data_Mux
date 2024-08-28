import socket
import numpy as np
import time

HOST = 'localhost'
PORT = 65432
CHANNEL_COUNT = 4 
DATA_COUNT = 100  
DATA_SIZE = 1024 

def generate_data():
    """Gera um pacote de dados de exemplo."""
    return np.random.rand(DATA_SIZE).tobytes()

def send_tdm_data(conn):
    """Envia dados usando Multiplexação por Divisão de Tempo (TDM)."""
    conn.sendall(b'START_TDM\n')  
    for channel_id in range(DATA_COUNT):
        data = generate_data()
        data_with_channel = channel_id.to_bytes(1, 'big') + data
        conn.sendall(data_with_channel)
        time.sleep(0.1)  
    conn.sendall(b'END_TDM\n')

def send_fdm_data(conn):
    """Envia dados usando Multiplexação por Divisão de Frequência (FDM)."""
    conn.sendall(b'START_FDM\n')
    for i in range(DATA_COUNT):
        data = generate_data()
        channel_id = i % CHANNEL_COUNT
        data_with_channel = channel_id.to_bytes(1, 'big') + data
        conn.sendall(data_with_channel)
        time.sleep(0.1)
    conn.sendall(b'END_FDM\n')

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Emissor aguardando conexão em {HOST}:{PORT}")
        conn, addr = s.accept()
        with conn:
            print(f"Conectado por {addr}")
            print("Enviando dados usando TDM...")
            send_tdm_data(conn)
            print("Enviando dados usando FDM...")
            send_fdm_data(conn)

if __name__ == "__main__":
    main()
