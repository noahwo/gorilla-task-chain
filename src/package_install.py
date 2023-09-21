# If any package missing reported in returned error, add it here
import pip

packages = [
    "openai",
    "torch",
    "torchvision",
    "torchaudio",
    "transformers",
    "sentencepiece",
    "protobuf",
    "PIL",
    "vc_models",
    "timm",
    "python-dotenv",
    "sacremoses",
]

for package in packages:
    try:
        __import__(package)
    except ImportError:
        pip.main(["install", package])
