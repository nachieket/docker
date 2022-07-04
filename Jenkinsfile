pipeline {
    agent any

    environment {
        dockerImage = ''
    }

    stages {
        stage ('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '**']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/nachieket/spring-petclinic']]])
            }
        }

        stage ('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build registry
                }
            }
        }
    }
}
