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
                bat 'cd C:\Users\Marcone l\Desktop\projeto'
                git init
                git remote add origin https://github.com/RobsonAssis/Desafio-Indra.git
                git clone https://github.com/RobsonAssis/Desafio-Indra.git
                git pull
                bat 'cd ..\..'
                bat 'C:\Users\Marcone l\env\Scripts\activate'
                bat 'cd C:\Users\Marcone l\Desktop\projeto\Desafio-Indra\submarino'
                bat 'python -m Pyautomators -f json -o .\submarino.json'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
