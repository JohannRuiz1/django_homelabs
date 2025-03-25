from typing import List

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
    PERFORMANCE_OPTIMIZATION = "Optimization"
    REDUNDANCY_HIGH_AVAILABILITY = "Redundancy/High_Availability"
    ENERGY_EFFICIENT = "Energy Efficient"
    HEADLESS_SETUP = "Headless Setup"
    WEB_BASED_MANAGEMENT = "Web-Based"
    CLI_BASED_SETUP = "CLI-Based"
    BARE_METAL = "Bare-Metal"
    VIRTUALIZED_DEPLOYMENT = "Virtualized"
    CONTAINERIZATION = "Containerization"
    OFFLINE_CAPABLE = "Offline Capable"
    BEST_PRACTICES = "Best Practices"

class Step:
    def __init__(self, id: int, step_title: str, step_description: str, command: str = None):
        self.id = id
        self.step_title = step_title
        self.step_description = step_description

class Suggestion:
    def __init__(self, id: int, suggestion_title: str, suggestion_description: str = None):
        self.id = id

# Create your models here.
class GuideInfo:
    # id is a shadow property
    def __init__(self, id: int, title: str, author: str, category: CategoryEnum, label: List[LabelEnum],
                 views: int, edits: int, likes: int):
        self.id = id
        self.title = title
        self.author = author
        self.category = category
        self.labels = label
        self.views = views
        self.edits = edits
        self.likes = likes

class GuideContent:
    # id is a shadow property
    def __init__(self, id: int, guide_info_id: int, prerequisites: List[str], steps: List[Step]):
        self.id = id
        self.title = title
        self.author = author
        self.category = category
        self.labels = label
        self.views = views
        self.edits = edits
        self.likes = likes

