pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat 'echo Building...'
                bat '"C:\\Users\\kshow\\AppData\\Local\\Programs\\Python\\Python39\\python.exe" train_model.py'
            }
        }

        stage('Stop Old Container') {
            steps {
                bat 'docker stop laptop-price-prediction || exit 0'
            }
        }

        stage('Remove Old Container') {
            steps {
                bat 'docker rm laptop-price-prediction || exit 0'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t laptop-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker run -d --name laptop-price-prediction -p 5000:5000 laptop-app'
            }
        }
    }
}