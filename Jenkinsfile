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

        stage('Run Selenium Tests in Docker') {
            steps {
                script {
                    // Запускаем Docker контейнер с Selenium, в котором уже установлен Chrome и ChromeDriver
                    docker.image('selenium/standalone-chrome:latest').inside {
                        // Установка зависимостей внутри контейнера
                        sh 'python3 -m pip install --upgrade pip'
                        sh 'python3 -m pip install -r requirements.txt'

                        // Запуск тестов
                        sh 'pytest -n 2 tests/'
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
