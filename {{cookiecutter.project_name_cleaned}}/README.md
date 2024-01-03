# {{cookiecutter.project_name_cleaned}}

In this repository, we'll train a masked autoencoder based on transformers (ViT)


# Installation
```bash
conda create -n {{cookiecutter.project_env}} python=3.8
conda activate {{cookiecutter.project_env}}
pip install -r requirements.txt
# Install the library in dev mode...
pip install -e .
```

# Rules
In this repository, you can follow theses different rules : 
- Add your "library" code in ***{{cookiecutter.project_name_cleaned}}***
- Add your tests in ***tests***
If you want to create a project that directly use your library
- Create a ***scripts*** folder for your scripts
- Create a ***src*** folder if you want to build more complex things in your scripts
- Create a ***.azureml*** folder if you want to run Azureml pipelines


