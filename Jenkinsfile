#!groovy

pipeline {
    agent any

    environment {
        dockerImage = ''
        registry = 'nachiketj/pythondev'
    }

    stages {
        stage ('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '**']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/nachieket/docker']]])
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
