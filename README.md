# AutoFAIR
### Marco Haro-Crespo, Patrick Doran, Carlos J Landos, Carmina Echipare

## Introduction
Oportun is a fintech company that provides financial services. They have created a risk analysis tool based on FAIR (Factor Analysis of Information Risk). The FAIR tool was developed in excel to allow Oportun to perform quantitative, cybersecurity risk analyses and utilize data to estimate loss frequency and magnitude of loss for specific security risks. It currently requires manual data input into an excel workbook and relies on complex derivation formulas. Our project focuses on developing front- and back-end functionality for the FAIR tool in a very user friendly web application to move away from their old excel sheet.

## Requirements
- [Python3](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/) (Installs via pip)
- A linux kernel or equivalent, like [Bash](https://www.gnu.org/software/bash/)
- Repository through github: https://github.com/Patrick-Doran/FairTool

With everything installed run `python3 manage.py runserver` within the FairTool directory
- Tip: you should see the `manage.py` file when you use `ls` to know if you are in the right directory

Once running go to your localhost:8000, can be done manually or a link is provided in the terminal

## File Structure
Fair: The overall directory

Fair/Fair: Files for the overall project

Fair/fairTool: Python Scripts, CSS, Javascript, HTML coding areas for the application

Fair/RiskDB: Database storage for all of inputs

Fair/manage.py: Python script to run commands in Django

Fair/fairTool/static: Houses the CSS files for styling the sections of the web app, risktool.js is where the logic of the tool resides.

Fair/fairTool/templates: The main HTML file folder where all the HTML scripts are housed.
