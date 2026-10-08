## Hello World! <img alt="wave" src="https://raw.githubusercontent.com/MartinHeinz/MartinHeinz/master/wave.gif" width="30px">

<div align="center"> 🚀 Welcome to my git repo :FakeAdClicksDetection:</div>

### Fake Ad Clicks Detection Using Tensorflow and Machine Learning 
<img src="https://github.com/himalayaashish/FakeAdClicksDetection/blob/master/mlops.gif?raw=true" alt="Lumbar Detection" width="500"/>

###### This project focuses on detecting fake ad clicks using advanced machine learning techniques. I applied models to classify legitimate and fraudulent clicks based on patterns and user behavior data. The system leverages data preprocessing, model training, and evaluation to optimize the detection process for real-time applications.

###### To identify the best model with the highest performance, various machine learning algorithms were evaluated. The models were fine-tuned using class weighting to account for data imbalance, resulting in improved detection accuracy for fraudulent clicks.

###### This project demonstrates how combining cutting-edge ML techniques with user-friendly interfaces can transform document interactions.




###### To run notebook - Please make sure to have the csv file in the same location or change the path.

 

### Run the application

Use Python 3.11 on Windows. TensorFlow does not provide a native Windows
installation for the newer Python versions used by this project environment.
The setup below uses `uv` to select Python 3.11.
From the repository root, create and activate a virtual environment, install
the project dependencies, and run the entry point:

```powershell
uv venv --python 3.11 .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python main.py
```

Open **http://127.0.0.1:5000** to use the live demo. Choose a user profile,
click event, and ad category to see the saved TensorFlow model classify the
click. The page also shows dataset totals and recent predictions from the
current browser session. Keep the terminal running while using the website;
press `Ctrl+C` to stop it.

The website uses the trained model in `saved_models/click_model/1/`. To
retrain it and regenerate the CSV predictions instead, run:

```powershell
python main.py --train
```


###### Projects details are as follows 

###### configs :- In this module I defined everything that can be configurable and can be changed in future.

###### dataloader :- I defined all dataloading, preprocessing steps in this module

###### executor :- This module is responsible for training the model.

###### evaluation :- Kept empty for now. Mainly responsible for evaluating the model.

###### model :- This module only contains the actual deep learning / machine learning code.

###### Experiments :- This directory contains the notebook which I have used for experiments. It is the same notebook attached in this email.

###### ops :- Empty as of now. Could be used in future for operational related operations

###### utils :- Utility functions that are used in more than one place.

###### saved_models :- Saved the model after training.

###### main.py :- The entry point of the project.


#### Scope for enhancement are as follows.
1- We may need to use a weighted class for training so that we can achieve a high score.

2- We could use docker containers while productionizing the model.

 ---

### Languages and Tools 

### Languages
  **Python**:
 ![Python](https://img.shields.io/badge/-Python-black?style=flat&logo=python)
 ![Keras](https://img.shields.io/badge/-Keras-D00000?style=flat&logo=Keras)
 ![Tensorflow](https://img.shields.io/badge/-Tensorflow-gray?style=flat&logo=tensorflow)
 ![PyTorch](https://img.shields.io/badge/-PyTorch-EE4C2C?style=flat&logo=PyTorch&logoColor=white)
 ![Pandas](https://img.shields.io/badge/-Pandas-150458?style=flat&logo=Pandas)
 ![Numpy](https://img.shields.io/badge/-Numpy-lightgray?style=flat&logo=Numpy&logoColor=white)
 ![Scipy](https://img.shields.io/badge/-Scipy-blue?style=flat&logo=Scipy&logoColor=white)
 ![Matplotlib](https://img.shields.io/badge/-Matplotlib-black?style=flat&logo=Matplotlib&logoColor=white)
  

  **JavaScript**: 
  ![JavaScript](https://img.shields.io/badge/-JavaScript-black?style=flat&logo=javascript)
  ![HTML5](https://img.shields.io/badge/-HTML5-E34F26?style=flat&logo=html5&logoColor=white) 
  ![CSS3](https://img.shields.io/badge/-CSS3-1572B6?style=flat&logo=css3) 
  ![Bootstrap](https://img.shields.io/badge/-Bootstrap-purple?style=flat&logo=bootstrap) 

  **SQL:**
  ![SQL](https://img.shields.io/badge/-SQL-orange?style=flat&logo=sql)
  ![MySQL](https://img.shields.io/badge/-MySQL-lightgray?style=flat&logo=mysql)
  ![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-blue?style=flat&logo=postgresql)

### Tools

**Software Development:**
![Pycharm IDE](https://img.shields.io/badge/PyCharm-000000?logo=PyCharm&logoColor=white)
![IntelliJ IDEA](https://img.shields.io/badge/-red?style=flat&logo=IntelliJ-IDEA&logoColor=white)
![Docker](https://img.shields.io/badge/-2496ED?style=flat&logo=Docker&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-gray?style=flat&logo=jenkins) 
![XML](https://img.shields.io/badge/-XML-orange?style=flat&logo=xml)
![JSON](https://img.shields.io/badge/-JSON-lightgray?style=flat&logo=json)
![Vim](https://img.shields.io/badge/-019733?style=flat&logo=Vim&logoColor=white)

**SDLC:**
![Agile](https://img.shields.io/badge/Agile-blue?style=flat&logo=Agile&logoColor=white) ![Scrum](https://img.shields.io/badge/Scrum-green?style=flat&logo=Scrum&logoColor=white) ![Kanban](https://img.shields.io/badge/Kanban-red?style=flat&logo=Kanban&logoColor=white)

**Software Engineering:**
[![Jira](https://img.shields.io/badge/-Jira-0052CC?style=flat&logo=jira&logoColor=white&link=https://github.com/Quananhle)](https://github.com/Quananhle)
[![Travis](https://img.shields.io/badge/-Travis-red?style=flat&logo=travis&logoColor=white&link=https://github.com/Quananhle)](https://github.com/Quananhle) 

**Version Control:**
![Bitbucket](https://img.shields.io/badge/-Bitbucket-blue?style=flat&logo=bitbucket)
![Git](https://img.shields.io/badge/-Git-black?style=flat&logo=git) 
![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat&logo=github)

---


<!--START_SECTION:waka-->
<div style="display: flex; justify-content: space-between; align-items: center;">
  <img src="http://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=himalayaashish&theme=apprentice" alt="Profile Details" />
  <img src="http://github-profile-summary-cards.vercel.app/api/cards/productive-time?username=himalayaashish&theme=apprentice&utcOffset=8" alt="Productive time" />
  <img align="left" src="http://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=himalayaashish&theme=apprentice" alt="Repos per language" />
  <img align="left" src="http://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=himalayaashish&theme=apprentice" alt="Most commit language" />
  <img align="center" src="http://github-profile-summary-cards.vercel.app/api/cards/stats?username=himalayaashish&theme=apprentice" alt="Stats" />
</div>


---
<div align="center">
  <h3 align="center">Connect with me<img align="center" src="https://github.com/rajput2107/rajput2107/blob/master/Assets/Handshake.gif" height="33px" /></h3> 
</div>
<p align="center">
 <a href="https://www.linkedin.com/in/himalayaashish/" target="blank">
  <img align="center" alt="Pramod's LinkedIn" width="30px" src="https://www.vectorlogo.zone/logos/linkedin/linkedin-icon.svg" /> &nbsp; &nbsp;
 </a>
 <a href="https://www.kaggle.com/himalayaashish" target="blank">
  <img align="center" alt="Gumalaya's Kaggle" width="60px" src="https://www.vectorlogo.zone/logos/kaggle/kaggle-ar21.svg" /> &nbsp; &nbsp;
 </a>
 <a href="https://twitter.com/himalayaashish" target="blank">
  <img align="center" alt="Pramod's Twitter" width="30px" src="https://www.vectorlogo.zone/logos/twitter/twitter-official.svg" /> &nbsp; &nbsp;
 </a>
 <a href="https://medium.com/@himalayaashish" target="blank">
  <img align="center" alt="Himalaya's Twitter" width="30px" src="https://www.vectorlogo.zone/logos/medium/medium-tile.svg" />
 </a>
