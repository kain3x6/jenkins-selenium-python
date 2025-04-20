pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                sshagent(['ssh_key_for_git']) {
                    git 'kain3x6/jenkins-selenium-python.git'
                }
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
