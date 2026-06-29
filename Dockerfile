FROM eclipse-temurin:17-jre
WORKDIR /app

COPY /target/*.war app.jar

ENTRYPOINT ["java", "-jar", "app.jar"]