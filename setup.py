from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing_package",
    version="0.0.1",
    author="Ruan Mateus",
    author_email="ruanmateusbsb@gmail.com",
    description="Programa que pega duas imagens e retorna a diferença entre elas, a imagem 1 com o histograma da imagem 2",
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.5',
)
