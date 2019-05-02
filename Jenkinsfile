
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building'
                
                git 'https://github.com/RobsonAssis/Desafio-Indra'
                bat 'env//Scripts//activate'
            }
        }
        stage('Test') {
            steps {
               bat 'cd ./submarino && python -m Pyautomators'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying'
            }
        }
    }
}
