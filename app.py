from flask import Flask, render_template, request, jsonify
import mj  # Importing your mj.py module

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # This will serve your index.html

@app.route('/generate-prompt', methods=['POST'])
def generate_prompt():
    style_artist_input = request.json.get('style_artist')
    randomDescriptions = request.json.get('randomDescriptions')
    randomDetailedModifiers = request.json.get('randomDetailedModifiers')
    randomStylesArtists = request.json.get('randomStylesArtists')
    randomTechniques = request.json.get('randomTechniques')
    randomThemesConcepts = request.json.get('randomThemesConcepts')
    randomTechnicalModifiers = request.json.get('randomTechnicalModifiers')
    
    prompt = mj.generate_prompt(
        style_artist_input,
        randomDescriptions=randomDescriptions,
        randomDetailedModifiers=randomDetailedModifiers,
        randomStylesArtists=randomStylesArtists,
        randomTechniques=randomTechniques,
        randomThemesConcepts=randomThemesConcepts,
        randomTechnicalModifiers=randomTechnicalModifiers
    )
    
    return jsonify({'prompt': prompt})

if __name__ == '__main__':
    app.run(debug=True)
