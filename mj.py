import random


# Predefined lists
# Descriptions
descriptions = [
    "forest scene", 
    "portrait of an unknown figure", 
    "bustling cityscape", 
    "tranquil ocean view", 
    "mountainous landscape"
]

# Styles/Artists
styles_artists = [
    "Paul Klee", 
    "Salvador Dali", 
    "Picasso", 
    "Douglas Adams", 
    "Wes Anderson"
]

# Techniques
techniques = [
    "watercolor techniques", 
    "paper cut animation methods", 
    "spray painted realism", 
    "digital art rendering", 
    "oil painting strokes"
]

# Themes/Concepts
themes_concepts = [
    "grim dark cryptidwave", 
    "surrealism", 
    "romantic nostalgia", 
    "futuristic dystopia", 
    "Victorian elegance"
]

# Detailed Modifiers
detailed_modifiers = [
    "anatomical precision", 
    "Fibonacci sequence patterns", 
    "vibrant color contrasts", 
    "intricate shadow play", 
    "geometric distortions"
]

# Technical Modifiers
technical_modifiers = [
    "--ar 2:3", 
    "--ar 16:9", 
    "--test", 
    "--niji", 
    
]


def random_element(elements_list):
    return random.choice(elements_list)


def generate_prompt(style_artist=None):
    if not style_artist:
        style_artist = random_element(styles_artists)  # Corrected variable assignment
    description = random_element(descriptions)
    technique = random_element(techniques)
    theme_concept = random_element(themes_concepts)
    detailed_modifier = random_element(detailed_modifiers)
    technical_modifier = random_element(technical_modifiers)
    
    # Revised prompt structure
    prompt = f"Create a {description} inspired by {style_artist}, portrayed through {technique}, evoking a sense of {theme_concept}. It should feature {detailed_modifier} and adhere to settings {technical_modifier}."
    
    return prompt

def user_input(category):
    user_choice = input(f"Enter your choice for {category} or type 'random' to randomize: ")
    if user_choice == "random":
        return random_element(eval(category))
    else:
        return user_choice  # Use the user's input directly


def main():
    style_artist_input = user_input("styles_artists")  # Renamed variable to avoid shadowing
    print(generate_prompt(style_artist_input))

if __name__ == "__main__":
    main()