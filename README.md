# Recipe Generator App 
This is a web application that can take an ingredient list provided by the user and generate a recipe that they can make with these ingredients. This should especially help those with limited pantries or those who do not know what to make with the stuff that they have on hand. 
## Table of Contents  
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
## Installation 
If you already have both pip and python3 installed, skip to step 3. If they need to be upgraded, your terminal will tell you the appropriate command to input. 
1. Install python. This can be done by going to the python website and following the appropriate steps for your operating system. Recent python releases can be found here: https://www.python.org/downloads/ 
I would recommend installing the latest release as this will help you avoid any hassles during the usage stage. 
2. Pip usually comes pre-installed if you downloaded from python.org. However, if it was not, pip's maintainers have provided commands to install and upgrade it for for Windows, MacOS, and Linux here: https://pip.pypa.io/en/stable/installation/
3.  Assuming you have pip and python 3 installed, you must install flask. This can be done by opening your terminal and inputting: 
pip install flask. 
4. You must also install OpenAI's python library (If you have this done already, skip this step). This can be done either independetly or after setting up a virtual python environment for installing the OpenAI python library. Information for setting up the virtual python environment is provided here for Windows, MacOS nd Unix: https://platform.openai.com/docs/quickstart?context=python 
You can install OpenAI's python library by inputting: 
pip install --upgrade openai 
5. To further configure OpenAI, you need to configure your unique OpenAI API key (provided by creating an account with OpenAI) and ensure it is attached to your computer. OpenAI provides instructions for attaching it to your computer for Windows and MacOS in step 2 of their quickstart manual found here: https://platform.openai.com/docs/quickstart?context=python  
## Usage  
1. Once you have flask and OpenAI's python library installed, you need to initialize the db file before you can run the app. You can do this by inputting: python3 init_db.py 
If this command does not work, try inputting: 
python init_db.py
2. Now it's time to run the app! To do this type: 
python3 -m flask --app app run. 
3. Go to the link for the local host address provided by flask. This will bring you to a webpage where you can expriment with the app.
## Contributing  
1. This app could use some additional features such as settings for amount of servings a meal should make, the amount of ingredients that a user has, and user skill level. 
2. The app's recipe is hard to read. The space where OpenAI's recipe is generated should look more like an actual recipe where ingredients and amounts are placed at the top and the steps for making the recipe should be shown as a numbered list as opposed to everything being in one paragraph.
## License 
This project is licensed under the [MIT License](License) 