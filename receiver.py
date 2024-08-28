import socket

HOST = 'localhost'
PORT = 65432
CHANNEL_COUNT = 4

def process_data(channel_id, data, stats, technique):
    """Processa os dados recebidos e atualiza estatísticas."""
    if channel_id not in stats[technique]:
        print(f"Canal: {channel_id} para técnica {technique}")
        return
    stats[technique][channel_id]['count'] += 1
    stats[technique][channel_id]['size'] += len(data)
    stats[technique]['total']['count'] += 1
    stats[technique]['total']['size'] += len(data)

def main():
    stats = {
        'TDM': {i: {'count': 0, 'size': 0} for i in range(CHANNEL_COUNT)},
        'FDM': {i: {'count': 0, 'size': 0} for i in range(CHANNEL_COUNT)},
    }
    stats['TDM']['total'] = {'count': 0, 'size': 0}
    stats['FDM']['total'] = {'count': 0, 'size': 0}
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"Conectado ao emissor em {HOST}:{PORT}")
        buffer = b''
        current_technique = None
        
        while True:
            chunk = s.recv(1024)
            if not chunk:
                break
            buffer += chunk
            
            while b'\n' in buffer:
                delimiter_index = buffer.index(b'\n')
                message = buffer[:delimiter_index]
                if message == b'START_TDM':
                    current_technique = 'TDM'
                elif message == b'START_FDM':
                    current_technique = 'FDM'
                elif message == b'END_TDM':
                    current_technique = None
                elif message == b'END_FDM':
                    current_technique = None
                else:
                    if current_technique:
                        if len(message) > 1:
                            channel_id = message[0]
                            data = message[1:]
                            process_data(channel_id, data, stats, current_technique)
                buffer = buffer[delimiter_index + 1:]

    print("\nEstatísticas de Recepção:")
    for technique in ['TDM', 'FDM']:
        print(f"\nTécnica: {technique}")
        for i in range(CHANNEL_COUNT):
            print(f"Canal {i}:")
            print(f"  Pacotes recebidos: {stats[technique][i]['count']}")
            print(f"  Total de bytes recebidos: {stats[technique][i]['size']}")
        print(f"Total de pacotes recebidos: {stats[technique]['total']['count']}")
        print(f"Total de bytes recebidos: {stats[technique]['total']['size']}")

if __name__ == "__main__":
    main()
