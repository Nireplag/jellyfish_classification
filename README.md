# jellyfish_classification
This repo is created for the projects done for the ML_ZOOMCAMP from data.talks

## Files present
- notebook.ipynb: jupyter notebook file with image ingestion, checking, EDA and deep learning model hyperparameter tuning
- train.py: python file that was used to create final ml model available at jellyfish.h5 and jellyfish-classification(in case you want to create a tf-serving cloud model) 
- jellyfish.h5:  file created with train.py with ml model to be used into classification
- predict.py: python file created to generate a flask app to allow usage of jellyfish.h5 as a webservice.
- predict-test.py: python file created to test the webservice. This can be used for localhost only since allow usage of local path files.
- Pipfile and Pipfile.lock: files to create a pipenv to execute files and build container.
- Dockerfile: docker configuration file to create containerto be run locally or at cloud.
- dataset.zip: dataset to be used in case link to original file repository is removed. This dataset was originated from [link]([https://github.com/MainakRepositor/Datasets/tree/master](https://www.kaggle.com/datasets/anshtanwar/jellyfish-types?select=Train_Test_Valid).
  
## Description of the problem
The dataset used is related to determine the jellyfish species and can be used into image analysis for invasive species and also if they are dangerous to humans and other animals.

The species are as the following:

- Moon_jellyfish 
- barrel_jellyfish
- blue_jellyfish
- compass_jellyfish
- lions_mane_jellyfish
- mauve_stinger_jellyfish

## How to run project

### Clone project locally
Plase fork the project and create a local clone of the project locally using:

``` git clone <your-repo-url> ``` 

### Start pipenv environent

The files Pipfile and Pipfile.lock conatin the dependencies to execute the code without issues, therefore it is recomended to install and start the virtual environment as following:

- ``` pip install pipenv ``` in case you do not already have if
- ``` pipenv install ```
- From within the directory that have the Pipfile and Pipfile.lock execute the following command in prompt ``` pipenv shell```

### Create jellyfish.h5, no need to be executed

This step is not mandatory since we already have the file model available. You can execute the file using the command:
``` python train.py```

### Run webservice locally 

It is possible to run the webservice locally using the following command: ``` python predict.py```.

In order to locally test the serviceuse the file predict_test.py for localhost, save it and run the file predict_test.py from a differnt enviroment. Trying to use the same from pipenv will cause an error since it is already running the webservice.

In order to stop the webservice send the command: ``` CTRL + c```.

### Creating a docker image and save it to docker hub

In order to create a docker image, we assume you already have a docker installed in your computer.

To build the image locally execute the following command into the directory with Dockerfile:

``` docker build -t jellyfish-classification .```

Create a docker hub account. This can be easily done using your github account. 

Once logged, create a repository as public with same name as your already created docker image. 

Next a access token need to be created as following:

- Click your username at right top corner,
- Enter Account setting,
- Select Security,
- Click on "Create Access token",
- Populate name and leave it as "Read, write, Delete",
- run the steps prompted to connect your environment to the docker hub.

After we will deploy the imageb to the docker hub using the following command:

``` docker push <your_username>/jellyfish-classification```

### Deployment to Google Cloud Platform

We assume you already have a GCP account. 

Search for Cloud run service and click create service.

Populate the needed information as following: 

- Container image URL: <your_username>/jellyfish-classification
- Service Name: jellyfish-classification
- Ingress Control: All
- Authentication: Allow unauthenticated invocations
- Memory: 1Gb
- Container port: 9696

It is also recommneded to change the region and Autoscaling feautres as you see fit.
At end of deployment you will have the following:
![image](https://github.com/Nireplag/jellyfish_classification/assets/70478646/6e2c8d8e-8c1b-4323-af5c-5f5d1aab832a)


### Testing Cloud deployment

The service is already running under the url [[https://jellyfish-classification-2rtrkbrwna-uc.a.run.app](https://jellyfish-classification-2rtrkbrwna-uc.a.run.app)].

This url can be tested using test_cloud.py file with an additional '/predict'.

In order to use new urls to be tested, you can use the dataset/valid files available into the repository. Just nothe that the url need to be edited by changing the 'blob' to 'raw'.

As result of the execution, we will get a json with the payload being passed and the jellyfish species determined.

The file after executing will respond the following:
![image](https://github.com/Nireplag/jellyfish_classification/assets/70478646/1e70bea7-dbf5-4053-8a9d-95bb41ee950d)

