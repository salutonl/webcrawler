pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "Hello World"'
                bat '''
                    echo "Multiline shell steps works too"
                    ls -lah
                '''
            }
        }
    }
}
