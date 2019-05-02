pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building'
                bat label: '', script: 'env\\Scripts\\activate'
                git 'https://github.com/RobsonAssis/Desafio-Indra'
            }
        }
        stage('Test') {
            steps {
               bat 'cd submarino'               
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
