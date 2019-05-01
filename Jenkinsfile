node('windows') {

    stage('Checkout'){
        git('http://github.com/test/test')
        stdout = bat(returnStdout: true, script: 'git rev-parse HEAD')
        println("stdout ################ " + stdout + " ####################")
   }

}
