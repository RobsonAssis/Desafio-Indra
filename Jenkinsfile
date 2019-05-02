#!groovy
pipeline{
    agent any
    stages {
        stage ("Build"){
            steps{
                echo 'Building'
                git 'https://github.com/RobsonAssis/Desafio-Indra'
            }
        }
        stage ("Test"){
            steps{
                bat '''
                pip install python-jenkins
                python -m pip install --upgrade pip
                pip install virtualenv
                virtualenv env
                env//Scripts//activate
                '''
                bat '''
                cd Submarino
                python -m Pyautomators -f json -o .//Submarinoj.json
                '''
            }
        }
    }
}
