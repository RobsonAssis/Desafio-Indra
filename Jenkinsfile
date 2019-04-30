node{
  tool name : 'maven-3', type:'maven'
  stage('SCM Checkout'){
    git 'https://github.com/RobsonAssis/Desafio-Indra'
  }
  stage('Compile-Package'){
    sh 'mvn package'
  }
}
