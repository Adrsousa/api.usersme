from flask import Flask, jsonify, request 
app = Flask(__name__) 

@app.route('/users', methods=['GET'])
def test():
	return jsonify({'message' : 'Aqui serao listados todos os usuarios!'})

if __name__ == '__main__':
	app.run() 