#!groovy
pipeline{
    agent any
    stages {
        stage ("Build"){
            steps{
                echo '-------------------------------------------------------------------------------------'
                echo 'Building..........'
                echo '-------------------------------------------------------------------------------------'
                git 'https://github.com/RobsonAssis/Desafio-Indra'
                echo '-------------------------------------------------------------------------------------'
            }
        }
        stage ("Test"){
            steps{
                echo '-------------------------------------------------------------------------------------'
                echo 'Testing..........'
                echo '-------------------------------------------------------------------------------------'
                bat '''
                pip install python-jenkins
                python -m pip install --upgrade pip
                pip install virtualenv
                virtualenv env
                env//Scripts//activate
                '''     
                echo '-------------------------------------------------------------------------------------'
            }
        }
        stage ("Deploy"){
            steps{
               echo '-------------------------------------------------------------------------------------'
               echo 'Deploing........'
               echo '-------------------------------------------------------------------------------------'
               bat '''
               cd Submarino
               python -m Pyautomators -f json -o .//submarino.json
               type submarino.json
               '''
           }
        }
    }
}
