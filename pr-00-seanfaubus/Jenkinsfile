pipeline {
    agent { docker { image 'shahatuh/dp2306' } }

    environment {
        PATH = "env/bin/:$PATH"
    }
    stages {
        stage('build') {
            steps {
                sh 'python pr_01.py -kv input/ciphercode.txt -m input/messages.txt'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'output/**/*.* ', onlyIfSuccessful: true
        }
    }
}
