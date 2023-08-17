from flask import Flask, render_template, request, jsonify
import mj  # Importing your mj.py module

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # This will serve your index.html

@app.route('/generate-prompt', methods=['POST'])
def generate_prompt():
    style_artist_input = request.json.get('style_artist')
    
    # New input fields
    inputDescriptions = request.json.get('inputDescriptions')
    inputDetailedModifiers = request.json.get('inputDetailedModifiers')
    inputTechniques = request.json.get('inputTechniques')
    inputThemesConcepts = request.json.get('inputThemesConcepts')
    inputTechnicalModifiers = request.json.get('inputTechnicalModifiers')
    
    randomDescriptions = request.json.get('randomDescriptions')
    randomDetailedModifiers = request.json.get('randomDetailedModifiers')
    randomStylesArtists = request.json.get('randomStylesArtists')
    randomTechniques = request.json.get('randomTechniques')
    randomThemesConcepts = request.json.get('randomThemesConcepts')
    randomTechnicalModifiers = request.json.get('randomTechnicalModifiers')
    
    prompt = mj.generate_prompt(
        style_artist_input,
        description_input=inputDescriptions,  # Passing the new inputs
        detailed_modifier_input=inputDetailedModifiers,
        technique_input=inputTechniques,
        theme_concept_input=inputThemesConcepts,
        technical_modifier_input=inputTechnicalModifiers,
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
