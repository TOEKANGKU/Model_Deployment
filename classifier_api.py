import os
import string
from flask import Flask, request, jsonify
import tensorflow as tf
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

app = Flask(__name__)

# Load the pre-trained text classification model
model_worker = tf.keras.models.load_model('model_worker.h5')
model_user = tf.keras.models.load_model('model_user.h5')

# Tokenizer configuration
vocab_size = 10000
oov_token = "<OOV>"
max_length = 100
trunc_type = 'post'

# Helper functions for text preprocessing
def remove_punctuation(sentences):
    translator = str.maketrans('', '', string.punctuation)
    no_punct = sentences.translate(translator)
    return no_punct

def remove_stopword(sentences):
    sentences = sentences.lower()
    sentences = remove_punctuation(sentences)
    factory = StopWordRemoverFactory()
    stopwords = factory.get_stop_words()
    words = sentences.split()
    words_result = [word for word in words if word not in stopwords]
    sentences = ' '.join(words_result)
    return sentences

# API endpoint for text classification
@app.route('/classify-worker', methods=['POST'])
def classify_worker():
    try:
        data = request.json
        text = data['text']
        preprocessed_text = remove_stopword(text)

        # Tokenize and pad the input text
        tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_token)
        tokenizer.fit_on_texts([preprocessed_text])
        sequence = tokenizer.texts_to_sequences([preprocessed_text])
        padded_sequence = pad_sequences(sequence, maxlen=max_length, truncating=trunc_type, padding='post')


        # Make a prediction
        prediction = model_worker.predict(padded_sequence)
        predicted_class = int(tf.argmax(prediction, axis=1)[0].numpy())

        # Convert the prediction to human-readable form
        #worker
        classes = ['service kulkas', 'service soundsystem', 'tukang batu', 'tukang semen', 'service sistem', 'tukang las', 'tukang cat', 'service perangkat lunak', 'service keamanan', 'service ac', 'tukang kayu', 'service mesin cuci', 'service televisi', 'service data', 'service perangkat keras']
        #classes = ['service ac', 'service kulkas', 'service mesin cuci', 'service soundsystem', 'service televisi', 'service data', 'service keamanan', 'service perangkat keras', 'service perangkat lunak', 'service sistem', 'tukang batu', 'tukang cat', 'tukang kayu', 'tukang las', 'tukang semen']
        
        result = {
            "predicted_class": classes[predicted_class],
        }

        return jsonify(result)

    except Exception as e:
        response = {
            'error': str(e),
            'message': 'Error processing the request'
        }
        return jsonify(response), 400

@app.route('/classify-user', methods=['POST'])
def classify_user():
    try:
        data = request.json
        text = data['text']
        preprocessed_text = remove_stopword(text)

        # Tokenize and pad the input text
        tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_token)
        tokenizer.fit_on_texts([preprocessed_text])
        sequence = tokenizer.texts_to_sequences([preprocessed_text])
        padded_sequence = pad_sequences(sequence, maxlen=max_length, truncating=trunc_type, padding='post')


        # Make a prediction
        prediction = model_user.predict(padded_sequence)
        predicted_class = int(tf.argmax(prediction, axis=1)[0].numpy())

        # Convert the prediction to human-readable form
        classes = ['servis mesin cuci', 'service keamanan', 'service sistem', 'servis soundsystem', 'service perangkat keras', 'tukang kayu', 'servis televisi', 'tukang las', 'servis ac', 'tukang batu', 'tukang semen', 'servis kulkas', 'service data', 'service perangkat lunak', 'tukang cat']
        #classes = ['service data', 'service keamanan', 'service perangkat keras', 'service perangkat lunak', 'service sistem', 'servis ac', 'servis kulkas', 'servis mesin cuci', 'servis soundsystem', 'servis televisi', 'tukang batu', 'tukang cat', 'tukang kayu', 'tukang las', 'tukang semen']
  
        result = {
            "predicted_class": classes[predicted_class],
        }

        return jsonify(result)

    except Exception as e:
        response = {
            'error': str(e),
            'message': 'Error processing the request'
        }
        return jsonify(response), 400

# Default route for health check
@app.route('/')
def health_check():
    return 'OK'

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))