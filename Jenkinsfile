pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                sshagent(['ssh_key_for_git']) {
                    git credentialsId: 'ssh_key_for_git', url: 'git@github.com:kain3x6/jenkins-selenium-python.git'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install --upgrade pip'
                sh 'python3 -m pip install -r requirements.txt'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                timeout(time: 1, unit: 'MINUTES') {
                    sh '''
                        Xvfb :99 -screen 0 1920x1080x24 &
                        export DISPLAY=:99
                        python3 -m pytest tests
                    '''
                }
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
