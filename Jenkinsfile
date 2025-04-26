pipeline {
    agent any

    environment {
        DOCKER_COMPOSE_FILE = 'docker-compose.yml'
    }

    stages {
        stage('Checkout') {
            steps {
                timeout(time: 2, unit: 'MINUTES') {
                    sshagent(['ssh_key']) {
                        git credentialsId: 'ssh_key', url: 'git@github.com:kain3x6/jenkins-selenium-python.git'
                    }
                }
            }
        }

        stage('Cleanup Orphan Containers') {
            steps {
                timeout(time: 2, unit: 'MINUTES') {
                    script {
                        echo 'Checking and removing any orphan containers...'
                        sh '''
                            sudo docker-compose -f ${DOCKER_COMPOSE_FILE} down --volumes --remove-orphans || echo "No orphan containers to remove"
                        '''
                    }
                }
            }
        }

        stage('Start Selenium Container') {
            steps {
                timeout(time: 2, unit: 'MINUTES') {
                    script {
                        echo 'Starting Selenium container...'
                        sh 'sudo docker-compose -f ${DOCKER_COMPOSE_FILE} up -d'
                    }
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                timeout(time: 5, unit: 'MINUTES') {  // Чуть увеличил время
                    script {
                        echo 'Installing dependencies inside Selenium container...'
                        sh '''
                            sudo docker-compose -f ${DOCKER_COMPOSE_FILE} exec -T selenium bash -c "python3 -m pip install --upgrade pip --no-cache-dir -vvv"
                            sudo docker-compose -f ${DOCKER_COMPOSE_FILE} exec -T selenium bash -c "cat /mnt/requirements.txt"
                            sudo docker-compose -f ${DOCKER_COMPOSE_FILE} exec -T selenium bash -c "python3 -m pip install -r /mnt/requirements.txt --no-cache-dir -vvv"
                        '''
                    }
                }
            }
        }

        stage('Run Selenium Tests') {
            steps {
                timeout(time: 5, unit: 'MINUTES') {  // Чуть увеличил время
                    script {
                        echo 'Running Selenium tests...'
                        sh '''
                            sudo docker-compose -f ${DOCKER_COMPOSE_FILE} exec -T selenium bash -c "pytest --browser_name=chrome /mnt/tests"
                        '''
                    }
                }
            }
        }
    }

    post {
        always { // Теперь контейнеры стопаются всегда, даже если упало на любой стадии
            echo 'Cleaning up containers...'
            script {
                sh '''
                    sudo docker-compose -f ${DOCKER_COMPOSE_FILE} down --volumes --remove-orphans || echo "Cleanup skipped, no containers found"
                '''
            }
        }
        success {
            echo 'Pipeline completed successfully ✅'
        }
        failure {
            echo 'Pipeline failed ❌'
        }
    }
}
