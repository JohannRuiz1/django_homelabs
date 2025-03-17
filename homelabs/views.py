from django.shortcuts import render

# Create your views here.
def home(request):
    guide = {
        "image_url": "img/gitlab-logo.png",

    }
    return render(request, "homelabs/guides/view.html", featured_guide)

def guide_view(request):
    context = {
        "image_url": "img/gitlab-logo.png",
        "prerequisites_list": [
            "A Linux-based system (Ubuntu 20.04 LTS or later recommended)",
            "Root access to the server (or sudo privileges)",
            "A domain name or IP address to access GitLab",
            "At least 4GB of RAM (8GB recommended for better performance)",
            "Docker installed on the system (if using Docker for installation)",
            "A firewall configured to allow HTTP and HTTPS traffic (ports 80, 443)",
            "Basic knowledge of Linux command-line operations"
        ],
        "steps_list": [
            {"title": "Update the System", "description": "Start by updating your package list.", "command": "sudo apt update\nsudo apt upgrade -y"},
            {"title": "Install Required Dependencies", "description": "Install necessary dependencies.", "command": "sudo apt install -y curl openssh-server ca-certificates"},
            {"title": "Download and Install GitLab", "description": "Add GitLab repo and install.", "command": "curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.deb.sh | sudo bash\nsudo EXTERNAL_URL=\"http://your_domain_or_ip\" apt-get install gitlab-ee"},
            {"title": "Configure GitLab", "description": "Reconfigure GitLab settings.", "command": "sudo gitlab-ctl reconfigure"},
            {"title": "Access GitLab", "description": "Open a browser and navigate to GitLab."},
            {"title": "Configure Firewall", "description": "Allow HTTP/HTTPS traffic.", "command": "sudo ufw allow http\nsudo ufw allow https\nsudo ufw enable"},
            {"title": "Set Up SSL (Optional)", "description": "Enable SSL for GitLab.", "command": "sudo gitlab-ctl reconfigure"},
            {"title": "Create a New Project", "description": "Log in and create a project."},
            {"title": "Set Up Backups", "description": "Create automated backups.", "command": "sudo gitlab-rake gitlab:backup:create"}
        ],
        "suggestions_list": [
            {"value": "option1", "text": "Better clarification", "likes": 10},
            {"value": "option2", "text": "Spelling fixes", "likes": 4},
            {"value": "option3", "text": "Adding a fourth step", "likes": 10}
        ]
    }
    return render(request, "homelabs/guides/view.html", context)

