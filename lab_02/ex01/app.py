from flask import Flask, render_template, request, jsonify
from cipher.caesar import CaesarCipher
from flask import Flask, render_template, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template('index.html')

# ===== CAESAR CIPHER =====
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt/caesar", methods=['POST'])
def encrypt_caesar():
    data = request.get_json()
    text = data.get('inputPlainText')
    key = int(data.get('inputKeyPlain'))
    result = CaesarCipher().encrypt_text(text, key)
    return jsonify({'encrypted_text': result})

@app.route("/decrypt/caesar", methods=['POST'])
def decrypt_caesar():
    data = request.get_json()
    text = data.get('inputCipherText')
    key = int(data.get('inputKeyCipher'))
    result = CaesarCipher().decrypt_text(text, key)
    return jsonify({'decrypted_text': result})


# ===== VIGENERE CIPHER =====
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/encrypt/vigenere", methods=['POST'])
def encrypt_vigenere():
    data = request.get_json()
    text = data.get('inputPlainText')
    key = data.get('inputKeyPlain')
    result = VigenereCipher().vigenere_encrypt(text, key)
    return jsonify({'encrypted_text': result})

@app.route("/decrypt/vigenere", methods=['POST'])
def decrypt_vigenere():
    data = request.get_json()
    text = data.get('inputCipherText')
    key = data.get('inputKeyCipher')
    result = VigenereCipher().vigenere_decrypt(text, key)
    return jsonify({'decrypted_text': result})


# ===== RAILFENCE CIPHER =====
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/encrypt/railfence", methods=['POST'])
def encrypt_railfence():
    data = request.get_json()
    text = data.get('inputPlainText')
    key = int(data.get('inputKeyPlain'))
    result = RailFenceCipher().rail_fence_encrypt(text, key)
    return jsonify({'encrypted_text': result})

@app.route("/decrypt/railfence", methods=['POST'])
def decrypt_railfence():
    data = request.get_json()
    text = data.get('inputCipherText')
    key = int(data.get('inputKeyCipher'))
    result = RailFenceCipher().rail_fence_decrypt(text, key)
    return jsonify({'decrypted_text': result})


# ===== PLAYFAIR CIPHER =====
@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route("/encrypt/playfair", methods=['POST'])
def encrypt_playfair():
    data = request.get_json()
    text = data.get('inputPlainText')
    key = data.get('inputKeyPlain')
    matrix = PlayFairCipher().create_playfair_matrix(key)
    result = PlayFairCipher().playfair_encrypt(text, matrix)
    return jsonify({'encrypted_text': result})

@app.route("/decrypt/playfair", methods=['POST'])
def decrypt_playfair():
    data = request.get_json()
    text = data.get('inputCipherText')
    key = data.get('inputKeyCipher')
    matrix = PlayFairCipher().create_playfair_matrix(key)
    result = PlayFairCipher().playfair_decrypt(text, matrix)
    return jsonify({'decrypted_text': result})


# ===== TRANSPOSITION CIPHER =====
@app.route("/transposition")
def transposition():
    return render_template('transposition.html')

@app.route("/encrypt/transposition", methods=['POST'])
def encrypt_transposition():
    data = request.get_json()
    text = data.get('inputPlainText')
    key = int(data.get('inputKeyPlain'))
    result = TranspositionCipher().encrypt(text, key)
    return jsonify({'encrypted_text': result})

@app.route("/decrypt/transposition", methods=['POST'])
def decrypt_transposition():
    data = request.get_json()
    text = data.get('inputCipherText')
    key = int(data.get('inputKeyCipher'))
    result = TranspositionCipher().decrypt(text, key)
    return jsonify({'decrypted_text': result})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
