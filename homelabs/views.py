from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        "image_url": "img/gitlab-logo.png",
        "author": "JohannRuiz176",
        "title": "Setting Up GitLab",
        "category": "Development/Testing",
        "labels": ["Virtualized", "Web-Based"],
        "views": 12,
        "edits": 5,
        "likes": 8
    }
    return render(request, "homelabs/home.html", {"guide": context})

def guide_list(request):
    context = [
        {
            "image_url": "img/networking.png",
            "author": "TechWizard",
            "title": "Setting Up VLANs for Home Networks",
            "category": "Networking",
            "labels": ["Beginner-Friendly", "Networking"],
            "views": 34,
            "edits": 10,
            "likes": 15
        },
        {
            "image_url": "img/virtualization.png",
            "author": "ServerNerd",
            "title": "First time with ESXi",
            "category": "Enterprise-Level",
            "labels": ["Virtualized", "Enterprise-Level"],
            "views": 27,
            "edits": 7,
            "likes": 12
        },
        {
            "image_url": "img/kubernetes.png",
            "author": "DevOpsDude",
            "title": "Deploying a Kubernetes Cluster",
            "category": "Containerization",
            "labels": ["Containerization", "Redundancy/HA"],
            "views": 42,
            "edits": 15,
            "likes": 18
        },
        {
            "image_url": "img/storage.jpeg",
            "author": "DataGuardian",
            "title": "Setting up RAID Storage",
            "category": "Enterprise-Level",
            "labels": ["Redundancy/HA", "Enterprise-Level"],
            "views": 19,
            "edits": 5,
            "likes": 9
        },
        {
            "image_url": "img/automation.png",
            "author": "ScriptMaster",
            "title": "Automating with Ansible Playbooks",
            "category": "Best Practices",
            "labels": ["CLI-Based", "Best Practices"],
            "views": 31,
            "edits": 9,
            "likes": 11
        },
        {
            "image_url": "img/security.png",
            "author": "CyberSentinel",
            "title": "Securing Your Home Lab",
            "category": "Best Practices",
            "labels": ["Security-Focused", "Best Practices"],
            "views": 50,
            "edits": 20,
            "likes": 25
        },
        {
            "image_url": "img/monitoring.jpeg",
            "author": "MetricManiac",
            "title": "Monitoring with Grafana & Prometheus",
            "category": "Optimization",
            "labels": ["Optimization", "Web-Based"],
            "views": 23,
            "edits": 6,
            "likes": 8
        },
        {
            "image_url": "img/cloud.png",
            "author": "CloudCrafter",
            "title": "Hybrid Cloud with AWS & Proxmox",
            "category": "Cloud-Based",
            "labels": ["Cloud-Based", "Virtualized"],
            "views": 29,
            "edits": 8,
            "likes": 14
        }
    ]

    return render(request, "homelabs/guides/list.html", {"guides": context})

def guide_add(request):
    return render(request, "homelabs/guides/add.html")


def guide_view(request):
    guide = {
        "image_url": "img/gitlab-logo.png",
        "author": "JohannRuiz176",
        "title": "Setting Up GitLab",
        "category": "Development/Testing",
        "labels": ["Virtualized", "Web-Based"],
        "views": 12,
        "edits": 5,
        "likes": 8
    }

    guide_content = {
        "prerequisites": [
            "A Linux-based system (Ubuntu 20.04 LTS or later recommended)",
            "Root access to the server (or sudo privileges)",
            "A domain name or IP address to access GitLab",
            "At least 4GB of RAM (8GB recommended for better performance)",
            "Docker installed on the system (if using Docker for installation)",
            "A firewall configured to allow HTTP and HTTPS traffic (ports 80, 443)",
            "Basic knowledge of Linux command-line operations"
        ],
        "steps": [
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
        "suggestions": [
            {"value": "option1", "text": "Better clarification", "likes": 10},
            {"value": "option2", "text": "Spelling fixes", "likes": 4},
            {"value": "option3", "text": "Adding a fourth step", "likes": 10}
        ]
    }

    context = {
        "guide": guide,
        "guide_content": guide_content
    }

    return render(request, "homelabs/guides/view.html", context)


def guide_suggestion(request):
    guide = {
        "image_url": "img/gitlab-logo.png",
        "author": "JohannRuiz176",
        "title": "Setting Up GitLab",
        "category": "Development/Testing",
        "labels": ["Virtualized", "Web-Based"],
        "views": 12,
        "edits": 5,
        "likes": 8
    }

    guide_content = {
        "prerequisites": [
            "A Linux-based system (Ubuntu 20.04 LTS or later recommended)",
            "Root access to the server (or sudo privileges)",
            "A domain name or IP address to access GitLab",
            "At least 4GB of RAM (8GB recommended for better performance)",
            "Docker installed on the system (if using Docker for installation)",
            "A firewall configured to allow HTTP and HTTPS traffic (ports 80, 443)",
            "Basic knowledge of Linux command-line operations"
        ],
        "steps": [
            {"title": "Update the System", "description": "Start by updating your package list.",
             "command": "sudo apt update\nsudo apt upgrade -y"},
            {"title": "Install Required Dependencies", "description": "Install necessary dependencies.",
             "command": "sudo apt install -y curl openssh-server ca-certificates"},
            {"title": "Download and Install GitLab", "description": "Add GitLab repo and install.",
             "command": "curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.deb.sh | sudo bash\nsudo EXTERNAL_URL=\"http://your_domain_or_ip\" apt-get install gitlab-ee"},
            {"title": "Configure GitLab", "description": "Reconfigure GitLab settings.",
             "command": "sudo gitlab-ctl reconfigure"},
            {"title": "Access GitLab", "description": "Open a browser and navigate to GitLab."},
            {"title": "Configure Firewall", "description": "Allow HTTP/HTTPS traffic.",
             "command": "sudo ufw allow http\nsudo ufw allow https\nsudo ufw enable"},
            {"title": "Set Up SSL (Optional)", "description": "Enable SSL for GitLab.",
             "command": "sudo gitlab-ctl reconfigure"},
            {"title": "Create a New Project", "description": "Log in and create a project."},
            {"title": "Set Up Backups", "description": "Create automated backups.",
             "command": "sudo gitlab-rake gitlab:backup:create"}
        ],
        "suggestions": [
            {"value": "option1", "text": "Better clarification", "likes": 10},
            {"value": "option2", "text": "Spelling fixes", "likes": 4},
            {"value": "option3", "text": "Adding a fourth step", "likes": 10}
        ]
    }

    context = {
        "guide": guide,
        "guide_content": guide_content
    }

    return render(request, "homelabs/guides/suggestion.html", context)

