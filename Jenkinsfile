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
                sh 'python -m Pyautomators'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
