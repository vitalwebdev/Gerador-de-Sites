import os
import argparse
from http.server import HTTPServer, SimpleHTTPRequestHandler


class CORSHTTPRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "*")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200, "OK")
        self.end_headers()


def run(
    server_class=HTTPServer,
    handler_class=CORSHTTPRequestHandler,
    port=8000,
    directory=None,
):
    if directory:  # Change the current working directory if directory is specified
        os.chdir(directory)
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Serving HTTP on http://localhost:{port} from directory '{directory}'...")
    httpd.serve_forever()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HTTP Server with CORS")
    parser.add_argument(
        "--dir", type=str, help="Directory to serve files from", default="."
    )
    parser.add_argument("--port", type=int, help="Port to serve HTTP on", default=8888)
    args = parser.parse_args()

    run(port=args.port, directory=args.dir)

"""Este trecho de código cria um servidor HTTP simples com suporte a Cross-Origin Resource Sharing (CORS) usando Python. Vamos entender o que cada parte faz:

1. **Importações:**
   - `os`: Módulo para interagir com o sistema operacional, usado aqui para manipular o diretório de trabalho.
   - `argparse`: Módulo para processar argumentos da linha de comando.
   - `HTTPServer` e `SimpleHTTPRequestHandler` do módulo `http.server`: Classes para criar um servidor HTTP e manipular solicitações HTTP básicas, respectivamente.

2. **Definição da classe `CORSHTTPRequestHandler`:**
   - Esta classe herda de `SimpleHTTPRequestHandler`.
   - Sobrescreve o método `end_headers` para adicionar cabeçalhos CORS à resposta HTTP.
   - Define o método `do_OPTIONS` para lidar com solicitações OPTIONS, necessárias para a implementação do CORS.

3. **Função `run`:**
   - Cria uma instância de `HTTPServer`, passando o endereço do servidor, a classe do manipulador e o número da porta.
   - Se um diretório for especificado, muda o diretório de trabalho para ele.
   - Inicia o servidor HTTP e imprime uma mensagem indicando o início do serviço.

4. **Condição `if __name__ == "__main__":`:**
   - Verifica se o script está sendo executado diretamente (não importado como um módulo).
   - Define e analisa argumentos da linha de comando usando o módulo `argparse`.
   - Chama a função `run`, passando os argumentos fornecidos ou os valores padrão se nenhum for fornecido.

Em resumo, este código cria um servidor HTTP que pode servir arquivos de um diretório especificado, com suporte a CORS para permitir 
solicitações de origens diferentes do servidor em que o código está sendo executado. Ele também usa a funcionalidade de argumentos da 
linha de comando para personalizar o diretório de serviço e a porta do servidor.
"""