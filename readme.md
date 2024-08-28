# Multiplexação de Dados

Este projeto demonstra o envio e a recepção de dados utilizando duas técnicas de multiplexação: **Multiplexação por Divisão de Tempo (TDM)** e **Multiplexação por Divisão de Frequência (FDM)**. 

### Clone o repositório
```bash
git clone https://github.com/JoaoVictorFBarros/Data_Mux.git
```


### Instalação das Dependências

Se ainda não tiver as bibliotecas instaladas, use:

```
pip install numpy
```

## Instruções para Executar

1. **Execute o emissor**

   ```
   python3 sender.py
   ```

1. **Em outro terminal, execute o receptor**

   ```
   python3 receiver.py
   ```

<div align="center">
<img src=print.png >
</div>


## Funcionamento

O projeto consiste em dois scripts Python: um emissor (sender) e um receptor(receiver).

### Emissor

O emissor é responsável por enviar pacotes de dados usando as técnicas de TDM e FDM.

- **TDM (Multiplexação por Divisão de Tempo)**: O emissor envia dados de diferentes canais de forma sequencial. Cada pacote de dados é precedido pelo ID do canal a que pertence. O emissor sinaliza o início e o fim da multiplexação TDM.
- **FDM (Multiplexação por Divisão de Frequência)**: O emissor envia pacotes de dados de forma intercalada entre os canais, com cada canal transmitido em um intervalo de tempo específico. Semelhante ao TDM, cada pacote de dados é precedido pelo ID do canal.

### Receptor

O receptor se conecta ao emissor, recebe os pacotes de dados e processa as informações conforme a técnica de multiplexação utilizada. O receptor coleta estatísticas sobre os pacotes recebidos e os bytes totais para cada canal e para a multiplexação total.

## Explicação das Técnicas de Multiplexação

- **Multiplexação por Divisão de Tempo (TDM)**: Técnica onde múltiplos sinais são transmitidos em diferentes intervalos de tempo. Cada canal tem um período de tempo reservado para transmitir seus dados, e esses períodos são repetidos ciclicamente.

- **Multiplexação por Divisão de Frequência (FDM)**: Técnica onde múltiplos sinais são transmitidos simultaneamente, mas em diferentes frequências. Cada canal ocupa uma faixa de frequência distinta, permitindo a transmissão paralela de sinais.

## Observações

- Certifique-se de que o emissor esteja em execução antes de iniciar o receptor.
- O código está configurado para usar `localhost` e a porta `65432` por padrão. Ajuste conforme necessário para seu ambiente.
