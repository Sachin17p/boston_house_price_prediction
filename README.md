# Boston House Price Prediction
## Softwares and tools required 
1. [VS Code IDE](https://code.visualstudio.com)
2. [Github account](https://github.com)
3. [Heroku account](https://heroku,com)
4. GIT CLI

## Create an environment

GIT Configuration :
git config --global user.name "Your User Name"
git congig --global user.name
git config --global user.email "Your email"
git config --global user.email 

Mention the files which you do not want to commit to the github repository in .gitignore file.

git add requirement.txt (Will add requirements.txt file to the github repo)
git status
git add .   (Add all the files to repo)

git commit -m "Commit message" (Commit message)

git push origin main


**After creating Dockerfile and Procfile follow these steps:** 
- Create .github/workflows directory
- Create a file named main.yaml in the .github/workflows
- Go to github and got to the Secrets -> Actions tab under Security in the repository of interest
- Create a HEROKU_API_KEY, get the key from HEROKU account
- Create HEROKU_EMAIL key ans HEROKU_APP_NAME key (same name as given on heroku)
- You are set with github actions
- Commit and push everything on github repo
- Go to commits on github and build and run
- Go to heroku and then open and run the app
- That's it! Your app is good to go!
