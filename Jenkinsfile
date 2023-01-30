pipeline {
        agent any
             tools{
                 maven 'maven-3.8.7'
            
             }
        stages {
            stage('package') {
                steps {
                    sh 'ls'
                    sh 'cd ./spark-streaming-app && mvn clean package'
                    sh 'ls'
                    sh 'cd ./kafka-mqtt-connect && mvn clean package'
                }
            }
            stage('deploy') {
                steps {
                  
                    sh 'sudo docker-compose -f ./IoT-data-simulator/docker-compose.yml up -d' //Run the IOT-DATA-SIMULATOR
                    sh "sudo docker-compose build --pull"
                    sh 'sudo docker-compose up -d' //Run the Spark Cluster & Kafka/zookeeper/Mosquitto && mqtt-to-kafka
                    sh 'sudo docker cp ./spark-streaming-app/target/spark-demo-1.0-SNAPSHOT-jar-with-dependencies.jar projet-federateur-job_spark-master_1:/opt/spark'
                    sh 'sudo docker cp ./spark-streaming-app/target/spark-demo-1.0-SNAPSHOT-jar-with-dependencies.jar projet-federateur-job_spark-worker-b_1:/opt/spark'
                    sh 'sudo docker cp ./spark-streaming-app/target/spark-demo-1.0-SNAPSHOT-jar-with-dependencies.jar projet-federateur-job_spark-worker-a_1:/opt/spark'
                    sh "sudo docker exec projet-federateur-job_spark-master_1 /bin/bash -c './bin/spark-submit --class org.example.StreamingJob --master spark://spark-master:7077 --deploy-mode cluster --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.0 spark-demo-1.0-SNAPSHOT-jar-with-dependencies.jar'"
                }
            }
        }
}
