pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                git 'https://github.com/RobsonAssis/Desafio-Indra'
                git 'git init'
                git 'git remote add origin https://github.com/RobsonAssis/Desafio-Indra.git'
            }
        }
        stage('Test') {
            steps {
                
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
