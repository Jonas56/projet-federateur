pipeline {
        agent any
        tools{
            maven 'maven-3.8.7'
            docker 'Docker'
        }
        stages {
            stage('package') {
                steps {
                        sh 'ls'
                    //sh 'cd ./spark-streaming-app && mvn clean package'
                    //sh 'cd ../kafka-mqtt-connect && mvn clean package'
                }
            }
            stage('deploy') {
                steps {
                        sh 'ls'
                    //sh 'docker-compose -f ./IoT-data-simulator/docker-compose.yml up -d' //Run the IOT-DATA-SIMULATOR
                    //sh 'docker-compose up -d' //Run the Spark Cluster & Kafka/zookeeper/Mosquitto
                    //sh 'docker cp ./spark-streaming-app/target/spark-demo-1.0-SNAPSHOT-jar-with-dependencies.jar docker-spark-cluster-master_spark-master_1:/opt/spark'
            
                    //sh 'docker exec -it docker-spark-cluster-master_spark-master_1 /bin/bash -c "./bin/spark-submit --class org.example.StreamingJob --master spark://localhost:7077 --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.0 spark-demo-1.0-SNAPSHOT-jar-with-dependencies.jar”'
                }
            }
        }
}
