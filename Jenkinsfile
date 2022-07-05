#!groovy

pipeline {
    agent any

    environment {
        dockerImage = ''
        registry = 'nachiketj/pythondev'
        registryCredential = 'dockerhub_id'
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

        stage ('Upload Image') {
            steps {
                script {
                    docker.withRegistry('', registryCredential) {
                        dockerImage.push()
                    }
                }
            }
        }
    }
}
