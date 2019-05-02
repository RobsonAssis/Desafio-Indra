pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building'
                git 'https://github.com/RobsonAssis/Desafio-Indra'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing'
                bat 'cd desafio-indra'
                bat 'cd submarino'
                bat 'virtualenv env'
                bat 'pip install Pyautomators'
                bat 'python -m Pyautomators'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
