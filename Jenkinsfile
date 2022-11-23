pipeline {
    agent { label 'django-documentation' }

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'sudo docker-compose build'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh 'sudo docker-compose up -d'
            }
        }

        stage('Migrate database....') {
            steps {
                echo 'Migrating databse....'
                sh 'sudo docker-compose run tutorials python3 manage.py migrate'
            }
        }
        stage('Rebuild and Deploy....') {
            steps {
                echo 'Rebuilding and Deploying....'
                sh 'sudo docker-compose up --build -d'
            }
        }
    }
}
