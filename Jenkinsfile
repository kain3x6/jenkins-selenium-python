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

        stage('Log docker-compose file') {
            steps {
                timeout(time: 2, unit: 'MINUTES') {
                    script {
                        sh 'cat ${DOCKER_COMPOSE_FILE}'
                    }
                }
            }
        }

        stage('Start Selenium Container') {
            steps {
                timeout(time: 2, unit: 'MINUTES') {
                    script {
                        sh 'sudo docker-compose -f ${DOCKER_COMPOSE_FILE} up -d'
                    }
                }
            }
        }

        stage('Install Dependencies in Selenium Container') {
            steps {
                timeout(time: 2, unit: 'MINUTES') {
                    script {
                        sh '''
                            sudo docker-compose -f ${DOCKER_COMPOSE_FILE} exec -T selenium bash -c "python3 -m pip install --upgrade pip"
                            sudo docker-compose -f ${DOCKER_COMPOSE_FILE} exec -T selenium bash -c "python3 -m pip install -r /mnt/requirements.txt"
                        '''
                    }
                }
            }
        }

        stage('Run Selenium Tests') {
            steps {
                timeout(time: 2, unit: 'MINUTES') {
                    script {
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
            echo 'Pipeline failed'
        }
    }
}
