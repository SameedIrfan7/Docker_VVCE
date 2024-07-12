import os
import subprocess

# Configuration
REPO_URL = 'https://github.com/SameedIrfan7/Docker_VVCE.git'
CLONE_DIR = 'cloned_repo'
IMAGE_NAME = 'sameedirfan7/docker_vvce'
CONTAINER_NAME = 'docker_vvce_container'

def run_command(command):
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running command {command}: {e.stderr}")

# Clone the Git repository
def clone_repo():
    if os.path.exists(CLONE_DIR):
        subprocess.run(['rm', '-rf', CLONE_DIR])
    run_command(['git', 'clone', REPO_URL, CLONE_DIR])

# Build the Docker image
def build_docker_image():
    dockerfile_path = os.path.join(CLONE_DIR, 'Dockerfile')
    if not os.path.exists(dockerfile_path):
        print(f"Error: Dockerfile not found in {CLONE_DIR}")
        return
    run_command(['docker', 'build', '-t', IMAGE_NAME, CLONE_DIR])

# Run the Docker container
def run_docker_container():
    run_command(['docker', 'run', '--name', CONTAINER_NAME, IMAGE_NAME])

# Main function to execute the tasks
def main():
    clone_repo()
    build_docker_image()
    run_docker_container()

if __name__ == '__main__':
    main()
