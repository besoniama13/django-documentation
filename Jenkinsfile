pipeline {
    agent { label 'node-01' }

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'docker-compose build'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh 'sudo docker-compose up -d'
            }
        }
    }
}
