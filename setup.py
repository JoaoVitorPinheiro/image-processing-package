from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="pct-processamento-imagens",
    version="0.0.1",
    author="João Vitor Pinheiro da Costa",
    author_email="joaovpro17@gmail.com",
    description="Image processing",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JoaoVitorPinheiro/image-processing-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
