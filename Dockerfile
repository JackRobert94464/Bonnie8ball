FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build-env
WORKDIR /app

COPY Magic8BallDashboard.csproj ./
RUN dotnet restore Magic8BallDashboard.csproj

COPY . ./
RUN dotnet publish Magic8BallDashboard.csproj -c Release -o out

FROM mcr.microsoft.com/dotnet/aspnet:8.0
WORKDIR /app
COPY --from=build-env /app/out .

RUN apt-get update && apt-get install -y python3 python3-pip

# Explicitly copy PythonModule directory from host to container
COPY --from=build-env /app/PythonModule ./PythonModule
RUN chmod +x ./PythonModule/8ball.py

EXPOSE 5000
ENV ASPNETCORE_URLS=http://+:5000

ENTRYPOINT ["dotnet", "Magic8BallDashboard.dll"]
