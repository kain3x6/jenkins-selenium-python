pipeline {
    agent any

    environment {
        DOCKER_COMPOSE_FILE = 'docker-compose.yml'
    }

    stages {
        stage('Checkout') {
            steps {
                sshagent(['ssh_key']) {
                    git credentialsId: 'ssh_key', url: 'git@github.com:kain3x6/jenkins-selenium-python.git'
                }
            }
        }

        stage('Start Selenium Container') {
            steps {
                script {
                    // Поднимем контейнеры с Selenium
                    sh 'docker-compose -f ${DOCKER_COMPOSE_FILE} up -d'  // Запуск контейнеров в фоновом режиме
                }
            }
        }

        stage('Install Dependencies in Selenium Container') {
            steps {
                script {
                    // Установим зависимости внутри контейнера
                    sh '''
                        docker-compose -f ${DOCKER_COMPOSE_FILE} exec selenium bash -c "python3 -m pip install --upgrade pip"
                        docker-compose -f ${DOCKER_COMPOSE_FILE} exec selenium bash -c "python3 -m pip install -r requirements.txt"
                    '''
                }
            }
        }

        stage('Run Selenium Tests') {
            steps {
                script {
                    // Запуск тестов внутри контейнера с Selenium
                    sh '''
                        docker-compose -f ${DOCKER_COMPOSE_FILE} exec selenium bash -c "pytest --browser_name=chrome /tests"
                    '''
                }
            }
        }

        stage('Stop Selenium Container') {
            steps {
                script {
                    // Остановим контейнеры после выполнения тестов
                    sh 'docker-compose -f ${DOCKER_COMPOSE_FILE} down'
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
