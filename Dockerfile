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

# Install Python, pip, and venv
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv && \
    ln -s /usr/bin/python3 /usr/bin/python

# Create Python venv
RUN python -m venv /app/venv

# Upgrade pip and install dependencies in venv
COPY requirements.txt ./PythonModule/requirements.txt
RUN /app/venv/bin/pip install --upgrade pip && \
    /app/venv/bin/pip install -r ./PythonModule/requirements.txt

# Copy published .NET output
COPY --from=build-env /app/out ./ 

# Copy Python module code
COPY --from=build-env /app/PythonModule ./PythonModule

# Make Python script executable
RUN chmod +x ./PythonModule/8ball.py

# Optional: Run AI integration test on build
# RUN /app/venv/bin/python ./PythonModule/8ball.py --test

# Set environment for ASP.NET Core
EXPOSE 5000
ENV ASPNETCORE_URLS=http://+:5000

# Entry point: run the .NET server
ENTRYPOINT ["dotnet", "Magic8BallDashboard.dll"]
