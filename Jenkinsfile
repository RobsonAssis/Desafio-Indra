pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                git 'https://github.com/RobsonAssis/Desafio-Indra'
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
