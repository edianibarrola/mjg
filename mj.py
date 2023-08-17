import random
from descriptions import descriptions
from detailed_modifiers import detailed_modifiers
from styles_artists import styles_artists
from techniques import techniques
from themes import themes_concepts



technical_modifiers = [
    "--ar 2:3", 
    "--ar 16:9", 
    "--test", 
    "--niji", 
    
]


def random_element(elements_list):
    return random.choice(elements_list)


def generate_prompt(style_artist=None, randomDescriptions=True, randomDetailedModifiers=True, randomStylesArtists=True, randomTechniques=True, randomThemesConcepts=True, randomTechnicalModifiers=True):
    if not style_artist and randomStylesArtists:
        style_artist = random_element(styles_artists)

    description = random_element(descriptions) if randomDescriptions else ""
    technique = random_element(techniques) if randomTechniques else ""
    theme_concept = random_element(themes_concepts) if randomThemesConcepts else ""
    detailed_modifier = random_element(detailed_modifiers) if randomDetailedModifiers else ""
    technical_modifier = random_element(technical_modifiers) if randomTechnicalModifiers else ""

    prompt_parts = []

    if randomDescriptions:
        prompt_parts.append(description)
    if randomStylesArtists:
        prompt_parts.append(f"inspired by {style_artist}")
    if randomTechniques:
        prompt_parts.append(f"portrayed through {technique}")
    if randomThemesConcepts:
        prompt_parts.append(f"evoking a sense of {theme_concept}")
    if randomDetailedModifiers:
        prompt_parts.append(detailed_modifier)
    if randomTechnicalModifiers:
        prompt_parts.append(technical_modifier)

    prompt = " ".join(part for part in prompt_parts if part)  # Join only non-empty parts

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