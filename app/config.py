from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
MODEL_PATH = DATA_DIR / "model.json"


PORT = int(os.getenv("PORT", 8050))
DEBUG = os.getenv("DEBUG", "0") == "1"