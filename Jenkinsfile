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

        stage('Check Files') {
            steps {
                timeout(time: 2, unit: 'MINUTES') {
                    script {
                        // Логируем содержимое текущей директории и docker-compose.yml
                        sh 'echo "Current directory contents:"'
                        sh 'ls -l'
                        sh 'echo "Contents of docker-compose.yml:"'
                        sh 'cat docker-compose.yml'
                    }
                }
            }
        }

        stage('Start Selenium Container') {
            steps {
                timeout(time: 2, unit: 'MINUTES') {
                    script {
                        // Поднимем контейнеры с Selenium
                        sh 'docker-compose -f ${DOCKER_COMPOSE_FILE} up -d'  // Запуск контейнеров в фоновом режиме
                    }
                }
            }
        }

        stage('Install Dependencies in Selenium Container') {
            steps {
                timeout(time: 2, unit: 'MINUTES') {
                    script {
                        // Установим зависимости внутри контейнера
                        sh '''
                            docker-compose -f ${DOCKER_COMPOSE_FILE} exec selenium bash -c "python3 -m pip install --upgrade pip"
                            docker-compose -f ${DOCKER_COMPOSE_FILE} exec selenium bash -c "python3 -m pip install -r /mnt/requirements.txt"
                        '''
                    }
                }
            }
        }

        stage('Run Selenium Tests') {
            steps {
                timeout(time: 2, unit: 'MINUTES') {
                    script {
                        // Запуск тестов внутри контейнера с Selenium
                        sh '''
                            docker-compose -f ${DOCKER_COMPOSE_FILE} exec selenium bash -c "pytest --browser_name=chrome /mnt/tests"
                        '''
                    }
                }
            }
        }

        stage('Stop Selenium Container') {
            steps {
                timeout(time: 2, unit: 'MINUTES') {
                    script {
                        // Остановим контейнеры после выполнения тестов
                        sh 'docker-compose -f ${DOCKER_COMPOSE_FILE} down'
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
