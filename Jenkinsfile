pipeline {
     agent any
 
     stages {
         stage('Checkout') {
             steps {
                 git 'https://github.com/username/repository.git'
             }
         }
 
         stage('Install Dependencies') {
             steps {
                 sh 'pytest -v --tb=short tests/'
             }
         }
 
         stage('Run Selenium Tests') {
             steps {
                 sh 'python -m unittest discover tests'
             }
         }
 
         stage('Push to GitHub') {
             when {
                 branch 'main'
             }
             steps {
                 sh 'git push origin main'
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
