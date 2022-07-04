pipeline {
    agent any

    environment {
        dockerImage = ''
        registry = 'nachiketj/pythondev'
    }

    stages {
        stage('Initialize') {
            def dockerHome = tool 'myDocker'
            env.PATH = "${dockerHome}/bin:${env.PATH}"
        }
        
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
