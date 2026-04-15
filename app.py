from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/', methods=['GET'])
def msg():
 # Extrai o nome do corpo da requisicao
 dados = request.get_json() or {}
 nome = dados.get('nome', 'Visitante')
 # Cria a mensagem de saudacao
 mensagem = f'Ola, {nome}! Bem-vindo ao mundo dos Microservicos.'
 # Retorna a resposta em JSON
 return jsonify({'statusCode': 200, 'body': mensagem})
@app.route('/health')
def health():
 return jsonify({'status': 'ok'})
if __name__ == '__main__':
 app.run(host='0.0.0.0', port=8080)
