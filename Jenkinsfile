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

        stage('Start Selenium Container') {
            steps {
                script {
                    // Поднимем контейнеры с Selenium
                    sh 'docker-compose up -d'  // Запуск контейнеров в фоновом режиме
                }
            }
        }

        stage('Install Dependencies in Selenium Container') {
            steps {
                script {
                    // Установим зависимости внутри контейнера
                    sh '''
                        docker-compose exec selenium python3 -m pip install --upgrade pip
                        docker-compose exec selenium python3 -m pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Selenium Tests') {
            steps {
                script {
                    // Запуск тестов внутри контейнера с Selenium
                    sh '''
                        docker-compose exec selenium pytest --browser_name=chrome
                    '''
                }
            }
        }

        stage('Stop Selenium Container') {
            steps {
                script {
                    // Остановим контейнеры после выполнения тестов
                    sh 'docker-compose down'
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
