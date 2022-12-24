pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                 sh 'pip install -r requirements.txt'
                 sh 'python manage.py runserver'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh 'python manage.py test'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
