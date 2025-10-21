from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    page_description = f.read()

# Lê as dependências do requirements.txt
with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="marcos-image-processing",  # 🔹 nome único e identificável
    version="0.1.4",
    description="Image Processing Package using Skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    author="Marcos Luiz",
    author_email="marcos.luiz@gmx.us",
    url="https://github.com/Cempressa/image-processing",  # 🔹 link do projeto
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.6",
)
