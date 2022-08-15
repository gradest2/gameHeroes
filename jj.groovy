pipeline {

  agent {
      docker {
        image 'docker:latest'
        args '-u root --privileged'
      }
    }

  parameters {
    //Choose application branch
    gitParameter name: 'TAG',
                 type: 'PT_BRANCH_TAG',
                 defaultValue: 'v0.0.1',
                 useRepository: "https://github.com/gradest2/gameHeroes.git"
  }

  environment {
    project = "gameheroes"
    version = "${TAG}".toLowerCase().replaceAll("origin/", "")
  }
  options {
    timestamps()
    disableConcurrentBuilds()
    buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '10'))
  }

  stages {
    stage('Build') {
      steps {
        script {
          git branch: "${version}",
            //credentialsId: '12345-1234-4696-af25-123455',
            url: 'https://github.com/gradest2/gameHeroes.git'
          sh "docker build -t '${project}:${version}' ."
          def image = docker.image("${project}:${version}")
             image.inside {
               sh "cp /dist/gameHeroes ${WORKSPACE}"
               sh "cp /data.yaml ${WORKSPACE}"
             }
          sh "tar -czvf ${project}_${version}.tar.gz gameHeroes data.yaml"
          archiveArtifacts "gameHeroes, data.yaml, ${project}_${version}.tar.gz"
        }
      }
    }
  }

  post {
    always {
      cleanWs()
    }
    success {
      sh "docker rmi -f \$(docker image ls --quiet --filter 'reference=${project}:${version}') || true"
    }
    failure {
      sh "echo 'FAILED'"
    }
  }
}
