from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing",
    version="0.0.1",
    author="Mateus Klein",
    author_email="mateusklein0@gmail.com",
    description="Projeto de processamento de imagens para fins de estudo clonado do seguinte repositório https://github.com/tiemi/image-processing-package/blob/master/README.md",
    long_description=page_description,
    long_description_content_type="text/markdown",
    #url="https://github.com/mateusklein/cursoPythonDIO"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
