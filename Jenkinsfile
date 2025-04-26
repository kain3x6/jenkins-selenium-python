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

        stage('Check and Remove Orphan Containers') {
            steps {
                timeout(time: 2, unit: 'MINUTES') {
                    script {
                        echo 'Checking for orphan containers and cleaning up...'
                        sh '''
                            sudo docker-compose -f ${DOCKER_COMPOSE_FILE} down --remove-orphans || echo "No orphan containers to remove"
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

        stage('Install Dependencies in Selenium Container') {
            steps {
                timeout(time: 2, unit: 'MINUTES') {
                    script {
                        echo 'Upgrading pip and installing requirements...'
                        sh '''
                            sudo docker-compose -f ${DOCKER_COMPOSE_FILE} exec -T selenium bash -c "python3 -m pip install --upgrade pip -vvv"
                            sudo docker-compose -f ${DOCKER_COMPOSE_FILE} exec -T selenium bash -c "cat /mnt/requirements.txt"
                            sudo docker-compose -f ${DOCKER_COMPOSE_FILE} exec -T selenium bash -c "python3 -m pip install -r /mnt/requirements.txt -vvv"
                        '''
                    }
                }
            }
        }

        stage('Run Selenium Tests') {
            steps {
                timeout(time: 2, unit: 'MINUTES') {
                    script {
                        echo 'Running tests inside Selenium container...'
                        sh '''
                            sudo docker-compose -f ${DOCKER_COMPOSE_FILE} exec -T selenium bash -c "pytest --browser_name=chrome /mnt/tests"
                        '''
                    }
                }
            }
        }

        stage('Stop Selenium Container') {
            steps {
                timeout(time: 2, unit: 'MINUTES') {
                    script {
                        echo 'Stopping Selenium container...'
                        sh 'sudo docker-compose -f ${DOCKER_COMPOSE_FILE} down --volumes --remove-orphans'
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully'
        }
        failure {
            echo 'Pipeline failed. Cleaning up...'
            script {
                // Принудительно останавливаем контейнеры в случае ошибки
                sh 'sudo docker-compose -f ${DOCKER_COMPOSE_FILE} down --volumes --remove-orphans || echo "Error during cleanup"'
            }
        }
    }
}
