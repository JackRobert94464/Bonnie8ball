# ===== Build Stage =====
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build-env
WORKDIR /app

# Copy csproj and restore as distinct layers
COPY Magic8BallDashboard.csproj ./
RUN dotnet restore Magic8BallDashboard.csproj

# Copy the full project and publish it
COPY . ./
RUN dotnet publish Magic8BallDashboard.csproj -c Release -o out

# ===== Runtime Stage =====
FROM mcr.microsoft.com/dotnet/aspnet:8.0
WORKDIR /app

# Install Python and alias it
RUN apt-get update && apt-get install -y python3 python3-pip && ln -s /usr/bin/python3 /usr/bin/python

# Copy published output
COPY --from=build-env /app/out ./

# Copy Python script and database
COPY --from=build-env /app/PythonModule ./PythonModule

# Make script executable
RUN chmod +x ./PythonModule/8ball.py

# Set environment for ASP.NET Core
EXPOSE 5000
ENV ASPNETCORE_URLS=http://+:5000

ENTRYPOINT ["dotnet", "Magic8BallDashboard.dll"]
