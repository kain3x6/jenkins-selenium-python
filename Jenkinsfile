pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                sshagent(['ssh_key_for_git']) {
                    git branch: 'master', credentialsId: 'ssh_key_for_git', url: 'git@github.com:kain3x6/jenkins-selenium-python.git'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                sh 'pytest tests'
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
