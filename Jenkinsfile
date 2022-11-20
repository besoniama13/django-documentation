pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                docker-compose build
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                docker-compose up -d
            }
        }
    }
}
