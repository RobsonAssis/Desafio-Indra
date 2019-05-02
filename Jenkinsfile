pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building'
                
                git 'https://github.com/RobsonAssis/Desafio-Indra'
                bat label: '', script: 'env\\Scripts\\activate'
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
