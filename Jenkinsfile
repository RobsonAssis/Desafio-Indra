pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                clone 'https://github.com/RobsonAssis/Desafio-Indra'
                
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                run 'python -m Pyautomators'
             
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                
            }
        }
    }
}
