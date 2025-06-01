pipeline {
    agent any

    environment {
        VENV_DIR = '.venv'
    }

    stages {
        stage('Clone Repo') {
            steps {
                echo 'Kod klonlanıyor...'
                checkout([$class: 'GitSCM',
                branches: [[name: '*/main']],
                userRemoteConfigs: [[url: 'https://github.com/bomobye/test_ci.git']]])
            }

        }

        stage('Setup Python Env') {
            steps {
                sh 'python3 -m venv .venv'
                sh '. .venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt'
            }
        }

        stage('Format Check (Black)') {
            steps {
                sh '. .venv/bin/activate && black --check app tests'
            }
        }

        stage('Lint (Flake8 & Pylint)') {
            steps {
                sh '. .venv/bin/activate && flake8 app tests'
                sh '. .venv/bin/activate && pylint app'
            }
        }

        stage('Run Tests') {
            steps {
                sh '. .venv/bin/activate && pytest'
            }
        }

        stage('SonarQube Analysis') {
            environment {
                SONAR_SCANNER_HOME = tool 'SonarQubeScanner'
            }
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh "${SONAR_SCANNER_HOME}/bin/sonar-scanner"
                }
            }
        }

        stage('Deploy to Remote Server') {
            steps {
                sshagent (credentials: ['remote-server-ssh']) {
                    sh '''
                    scp -r * user@192.168.1.204:/home/user/                    
                    '''
                }
            }
        }
    }
}
