pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                 sh 'pip3 install -r requirements.txt'
                 sh 'python3 manage.py runserver'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'

                sh 'python3 manage.py test'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
