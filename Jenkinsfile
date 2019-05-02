pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat 'cd C:\Users\Marcone l\Desktop\projeto'
                git init
                git remote add origin https://github.com/RobsonAssis/Desafio-Indra.git
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
