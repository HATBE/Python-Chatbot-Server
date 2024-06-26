class ResponseManager:
    def __init__(self):
        self.responses = {
            "restart": "Have you tried restarting your {}? It often resolves many issues.",
            "slow": "To fix a slow {} performance, try closing unnecessary applications.",
            "overheat": "If your {} is overheating, ensure it's placed in a well-ventilated area and clean any dust from the vents.",
            "greeting": "I'm doing well, thank you! How can I assist you with your computer problem?",
            "wifi": "If you're having Wi-Fi issues with your {}, try restarting your router or checking your network settings.",
            "battery": "If your {} battery is draining quickly, try reducing screen brightness and closing unused applications.",
            "software": "To resolve software issues on your {}, try reinstalling the problematic application.",
            "update": "Ensure your {} has the latest updates installed. Sometimes updates fix many issues.",
            "virus": "If you suspect a virus on your {}, run a full system antivirus scan.",
            "password": "If you've forgotten your {} password, you can reset it using the 'Forgot Password' option on the login screen.",
            "backup": "It's important to regularly backup your {} data to prevent data loss.",
            "hardware": "If you're experiencing hardware issues with your {}, check for any loose cables or connections.",
            "screen": "If your {} screen is flickering or not displaying properly, try adjusting the display settings.",
            "keyboard": "If your {} keyboard isn't working, try reconnecting it or checking for driver updates.",
            "sound": "If you're having sound issues on your {}, ensure the audio drivers are up to date and check the volume settings.",
            "default": "I did not understand that. Can you please describe your problem in more detail?"
        }
        self.keywords = {
            "restart": ["restart", "reboot", "boot"],
            "slow": ["slow", "lag", "performance"],
            "overheat": ["overheat", "hot", "heat"],
            "greeting": ["hello", "hi", "how are you"],
            "wifi": ["wifi", "wireless", "internet", "network"],
            "battery": ["battery", "draining", "charge", "charging"],
            "software": ["software", "application", "app", "program"],
            "update": ["update", "upgrade", "patch"],
            "virus": ["virus", "malware", "spyware", "antivirus"],
            "password": ["password", "login", "signin", "forgotten", "forgot"],
            "backup": ["backup", "save", "restore"],
            "hardware": ["hardware", "device", "component"],
            "screen": ["screen", "display", "monitor"],
            "keyboard": ["keyboard", "keys", "typing"],
            "sound": ["sound", "audio", "volume", "speaker"]
        }
        self.blank_spot = "computer"
        self.names = [
            "Rajesh Kumar",
            "Anjali Singh",
            "Vikram Patel",
            "Priya Sharma",
            "Arun Gupta",
            "Sneha Reddy",
            "Rohan Desai",
            "Neha Kapoor",
            "Suresh Nair",
            "Kavita Joshi"
        ]

    def get_response(self, key, entity=None):
        # fetch a response based on the key, formatting it with the entity if provided
        if key not in self.responses:
            return self.responses["default"]
        return self.responses[key].format(entity)

    def find_intent(self, processed_message):
        # convert the processed message list to a string for easier phrase matching
        processed_message = " ".join(processed_message)  # Convert list to string for phrase matching

        # check the processed message for any keywords corresponding to an intent
        for intent, words in self.keywords.items():
            for word in words:
                if word in processed_message:
                    return intent
                
        # Return default if no keywords match
        return "default"