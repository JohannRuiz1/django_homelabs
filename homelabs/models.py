from typing import List
from datetime import datetime

from django.db import models
from enum import Enum

class CategoryEnum(Enum):
    NETWORKING = "Networking"
    VIRTUALIZATION = "Virtualization"
    KUBERNETES = "Kubernetes"
    STORAGE = "Storage"
    AUTOMATION = "Automation"
    MONITORING = "Monitoring"
    OPERATING_SYSTEMS = "Operating Systems"
    CLOUD_HYBRID = "Cloud/Hybrid"
    DEVELOPMENT_TESTING = "Development/Testing"
    POWER_COOLING = "Power/Cooling"
    SECURITY_HARDENING = "Security/Hardening"
    HARDWARE_BUILDS = "Hardware/Builds"

class LabelEnum(Enum):
    BEGINNER_FRIENDLY = "Beginner-Friendly"
    ADVANCED = "Advanced"
    BUDGET_FRIENDLY = "Budget-Friendly"
    ENTERPRISE_LEVEL = "Enterprise-Level"
    CLOUD_BASED = "Cloud-Based"
    HOMELAB_ESSENTIALS = "Homelab Essentials"
    SECURITY_FOCUSED = "Security-Focused"
    OPTIMIZATION = "Optimization"
    HA = "High Availability"
    ENERGY_EFFICIENT = "Energy Efficient"
    HEADLESS = "Headless"
    WEB_BASED = "Web-Based"
    CLI_BASED = "CLI-Based"
    BARE_METAL = "Bare-Metal"
    VIRTUALIZED = "Virtualized"
    CONTAINERIZATION = "Containerization"
    OFFLINE_CAPABLE = "Offline Capable"
    BEST_PRACTICES = "Best Practices"

class Step:
    def __init__(self, id: int, step_title: str, step_description: str, command: str = None):
        self.id = id
        self.step_title = step_title
        self.step_description = step_description
        self.command = command

# Needs to be expanded
class Suggestion:
    def __init__(self, id: int, suggestion_title: str, suggestion_likes: int):
        self.id = id
        self.suggestion_title = suggestion_title
        self.suggestion_likes = suggestion_likes

# Create your models here.
class GuideInfo:
    # id is a shadow property
    def __init__(self, id: int, title: str, author: str, image_url: str, category: CategoryEnum, labels: List[LabelEnum],
                 views: int = 0, edits: int = 0, likes: int = 0, date: datetime = datetime.now()):
        self.id = id
        self.title = title
        self.author = author
        self.image_url = image_url
        self.category = category
        self.labels = labels
        self.views = views
        self.edits = edits
        self.likes = likes
        self.date = date

class GuideContent:
    # id is a shadow property
    def __init__(self, id: int, guide_info_id: int, prerequisites: List[str], steps: List[Step], suggestions: List[Suggestion]):
        self.id = id
        self.guide_info_id = guide_info_id
        self.prerequisites = prerequisites
        self.steps = steps
        self.suggestions = suggestions

featured_guide_info = GuideInfo(
    id=1,
    title="Setting Up",
    author="JohannRuiz176",
    image_url="img/gitlab-logo.png",
    category=CategoryEnum.DEVELOPMENT_TESTING,
    labels=[LabelEnum.VIRTUALIZED, LabelEnum.WEB_BASED],
    views=12,
    edits=5,
    likes=8
)

featured_guide_content = GuideContent(
    id=1,
    guide_info_id=1,
    prerequisites=[],
    steps=[],
    suggestions=[]
)

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
        {"description": "Start by updating your package list.", "command": "sudo apt update\nsudo apt upgrade -y"},
        {"description": "Install necessary dependencies.", "command": "sudo apt install -y curl openssh-server ca-certificates"},
        {"description": "Add GitLab repo and install.", "command": "curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.deb.sh | sudo bash\nsudo EXTERNAL_URL=\"http://your_domain_or_ip\" apt-get install gitlab-ee"},
        {"description": "Reconfigure GitLab settings.", "command": "sudo gitlab-ctl reconfigure"},
        {"description": "Open a browser and navigate to GitLab."},
        {"description": "Allow HTTP/HTTPS traffic.", "command": "sudo ufw allow http\nsudo ufw allow https\nsudo ufw enable"},
        {"description": "Enable SSL for GitLab.", "command": "sudo gitlab-ctl reconfigure"},
        {"description": "Log in and create a project."},
        {"description": "Create automated backups.", "command": "sudo gitlab-rake gitlab:backup:create"}
    ],
    "suggestions": [
        {"value": "option1", "text": "Better clarification", "likes": 10},
        {"value": "option2", "text": "Spelling fixes", "likes": 4},
        {"value": "option3", "text": "Adding a fourth step", "likes": 10}
    ]
}

guide1 = GuideInfo(
    id=1,
    title="Setting Up VLANs for Home Networks",
    author="TechWizard",
    image_url="img/networking.png",
    category=CategoryEnum.NETWORKING,
    labels=[LabelEnum.BEGINNER_FRIENDLY],
    views=34,
    edits=10,
    likes=15
)

guide2 = GuideInfo(
    id=2,
    title="First time with ESXi",
    author="ServerNerd",
    image_url="img/virtualization.png",
    category=CategoryEnum.VIRTUALIZATION,
    labels=[LabelEnum.VIRTUALIZED, LabelEnum.ENTERPRISE_LEVEL],
    views=27,
    edits=7,
    likes=12
)

guide3 = GuideInfo(
    id=3,
    title="Deploying a Kubernetes Cluster",
    author="DevOpsDude",
    image_url="img/kubernetes.png",
    category=CategoryEnum.KUBERNETES,
    labels=[LabelEnum.CONTAINERIZATION, LabelEnum.HA],
    views=42,
    edits=15,
    likes=18
)

guide4 = GuideInfo(
    id=4,
    title="Setting up RAID Storage",
    author="DataGuardian",
    image_url="img/storage.jpeg",
    category=CategoryEnum.STORAGE,
    labels=[LabelEnum.HA, LabelEnum.ENTERPRISE_LEVEL],
    views=19,
    edits=5,
    likes=9
)

guide5 = GuideInfo(
    id=5,
    title="Automating with Ansible Playbooks",
    author="ScriptMaster",
    image_url="img/automation.png",
    category=CategoryEnum.AUTOMATION,
    labels=[LabelEnum.CLI_BASED, LabelEnum.BEST_PRACTICES],
    views=31,
    edits=9,
    likes=11
)

guide6 = GuideInfo(
    id=6,
    title="Securing Your Home Lab",
    author="CyberSentinel",
    image_url="img/security.png",
    category=CategoryEnum.SECURITY_HARDENING,
    labels=[LabelEnum.SECURITY_FOCUSED, LabelEnum.BEST_PRACTICES],
    views=50,
    edits=20,
    likes=25
)

guide7 = GuideInfo(
    id=7,
    title="Monitoring with Grafana & Prometheus",
    author="MetricManiac",
    image_url="img/monitoring.jpeg",
    category=CategoryEnum.MONITORING,
    labels=[LabelEnum.OPTIMIZATION, LabelEnum.WEB_BASED],
    views=23,
    edits=6,
    likes=8
)

guide8 = GuideInfo(
    id=8,
    title="Hybrid Cloud with AWS & Proxmox",
    author="CloudCrafter",
    image_url="img/cloud.png",
    category=CategoryEnum.CLOUD_HYBRID,
    labels=[LabelEnum.CLOUD_BASED, LabelEnum.VIRTUALIZED],
    views=29,
    edits=8,
    likes=14
)

# Store all guides in a list
guides_info = [guide1, guide2, guide3, guide4, guide5, guide6, guide7, guide8]

users = {
    "johannruiz176": {
        "password": "pass123",
        "role": "regular"
    },
    "ScriptMaster": {
        "password": "abc123",
        "role": "regular"
    },
    "admin": {
        "password": "123pass",
        "role": "admin"
    }
}


