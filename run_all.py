import os
import sys

# Ensure the generator folder is in the python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from engine import write_category_files
from qa_gen import generate_qa
from chat_gen import generate_chat
from coding_gen import generate_coding
from advanced_categories_gen import (
    generate_most_basics_general,
    generate_emotions,
    generate_coding_master,
    generate_maths_advanced,
    generate_machine_learning_advanced,
    generate_deep_learning_very_advanced,
    generate_ai_ultra_advanced,
    generate_physics_master,
    generate_chemistry_normal,
    generate_science_overall_master,
    generate_religion_all_master,
    generate_encyclopedia_species_things_basic,
    generate_foods_and_recipes_professional,
    generate_recipe_usage_understanding,
    generate_unity_ultra,
    generate_unreal_master,
    generate_godot_ultra,
    generate_hacking_safe_basics,
    generate_internet_ultra,
    generate_anime_master,
)

try:
    from safety_gen import generate_safety
except ModuleNotFoundError:
    generate_safety = None

import warnings
warnings.filterwarnings("ignore")

def main():
    base_dir = "e:/Dataset/Categories"
    
    print("Starting procedural generation to match ai_dataset_blueprint.md...")
    
    # 100 files for each category as requested.
    num_files = 100
    
    categories = [
        ("QA", generate_qa, 30000),
        ("GeneralChat", generate_chat, 30000),
        ("Coding", generate_coding, 30000),
        ("MostBasicsGeneral", generate_most_basics_general, 30000),
        ("Emotions", generate_emotions, 32000),
        ("CodingMaster", generate_coding_master, 50000),
        ("MathsAdvanced", generate_maths_advanced, 50000),
        ("MachineLearningAdvanced", generate_machine_learning_advanced, 44000),
        ("DeepLearningVeryAdvanced", generate_deep_learning_very_advanced, 46000),
        ("AIUltraAdvanced", generate_ai_ultra_advanced, 47000),
        ("PhysicsMaster", generate_physics_master, 42000),
        ("ChemistryNormal", generate_chemistry_normal, 30000),
        ("ScienceOverallAdvancedMaster", generate_science_overall_master, 43000),
        ("ReligionAllMaster", generate_religion_all_master, 32000),
        ("EncyclopediaSpeciesThingsBasic", generate_encyclopedia_species_things_basic, 30000),
        ("FoodsAndRecipesProfessionalUltraAdvanced", generate_foods_and_recipes_professional, 45000),
        ("RecipeUsageUnderstanding", generate_recipe_usage_understanding, 32000),
        ("Unity2D3DPlaymakerUltraMasterAdvanced", generate_unity_ultra, 50000),
        ("Unreal2D3DBlueprintsMasterAdvanced", generate_unreal_master, 48000),
        ("Godot2D3DUltra", generate_godot_ultra, 43000),
        ("HackingSafeBasicsKnowledgeOnly", generate_hacking_safe_basics, 30000),
        ("InternetUltraMasterAdvanced", generate_internet_ultra, 45000),
        ("AnimeMaster", generate_anime_master, 33000),
    ]

    if generate_safety is not None:
        categories.append(("Safety", generate_safety, 30000))
    
    for category_name, generator_func, lines_per_file in categories:
        print(f"\n--- Generating Category: {category_name} ({lines_per_file} lines/file) ---")
        write_category_files(
            base_dir,
            category_name,
            generator_func,
            num_files=num_files,
            lines_per_file=lines_per_file,
        )

if __name__ == "__main__":
    main()
