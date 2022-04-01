# MLflow-project-template

mlflow-project-template

## STEPS -

### STEP 01- Create a repository by using template repository

### STEP 02- Clone the new repository

### STEP 03- Create a conda environment after opening the repository in VSCODE

```bash
conda create --prefix ./env python=3.7 -y
```

```bash
conda activate ./env
```

OR

```bash
source activate ./env
```

### STEP 04- install the requirements

```bash
pip install -r requirements.txt
```

### STEP 05 - Create conda.yaml file -

```bash
conda env export > conda.yaml
```

### STEP 06 - to run init_setup.sh(to run all commands through single (shell)script file)

```bash
bash init_setup.sh
```

### STEP 07- commit and push the changes to the remote repository

### STEP 08 - to create an environemnt using conda.yaml file

```bash
conda env create -f conda.yaml
```

### to run mlflow (--no-conda --> dont want new conda environment)

```bash
mlflow run . --no-conda
```

### mlflow - to want to run a specific stage(here get_data is the stage i want to run)

```bash
mlflow run . -e get_data --no-conda
```

### mlflow - to want to run a specific stage(here get_data is the stage i want to run) and passing different config paramters

```bash
mlflow run . -e get_data -P config=config/config2.yaml --no-conda
```

### to delete a file(ex:data/model/init_model.h5) which already present in git

```bash
git rm -f data/model/init_model.h5
```
