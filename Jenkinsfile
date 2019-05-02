pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                git 'https://github.com/RobsonAssis/Desafio-Indra'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                git 'https://github.com/RobsonAssis/Desafio-Indra'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                git 'https://github.com/RobsonAssis/Desafio-Indra'
            }
        }
    }
}
