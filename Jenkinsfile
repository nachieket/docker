pipeline {
    agent any

    stages {
        stage ('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '**']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/nachieket/spring-petclinic']]])
            }
        }
    }
}
