pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building'
                git 'https://github.com/RobsonAssis/Desafio-Indra'
                git 'git init'
                git 'git remote add add https://github.com/RobsonAssis/Desafio-Indra.git'
            }
        }
        stage('Test') {
            steps {
                echo 'Building'
                
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
