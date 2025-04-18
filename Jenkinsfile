pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/master']],
                    userRemoteConfigs: [[
                        url: 'git@github.com:kain3x6/jenkins-selenium-python.git',
                        credentialsId: 'github-ssh-key'
                    ]],
                    extensions: [
                        [$class: 'HostKeyVerificationStrategy$NonVerifyingKeyVerificationStrategy']
                    ]
                ])
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                sh 'python -m unittest discover tests'
            }
        }

        stage('Push to GitHub') {
            when {
                branch 'master'
            }
            steps {
                sh 'git push origin master'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully'
        }
        failure {
            echo 'Pipeline failed'
        }
    }
}
