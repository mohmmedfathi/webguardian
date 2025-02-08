import requests

VIRUSTOTAL_API_KEY = 'f0c22317d982d2f2b8d271d4a86bccdd12df82178d580d91f651b4efe07272b3'
VIRUSTOTAL_API_URL = "https://www.virustotal.com/api/v3"
VIRUSTOTAL_API_HEADERS = {"x-apikey": VIRUSTOTAL_API_KEY}

class VirusTotalService:
    """Handles interactions with VirusTotal API."""
    
    @staticmethod
    def scan_url(url):
        response = requests.post(
            f"{VIRUSTOTAL_API_URL}/urls",
            headers=VIRUSTOTAL_API_HEADERS,
            data={"url": url}
        )
        return response.json().get('data', {}).get('id')

    @staticmethod
    def get_analysis(scan_id):
        response = requests.get(
            f"{VIRUSTOTAL_API_URL}/analyses/{scan_id}",
            headers=VIRUSTOTAL_API_HEADERS
        )
        return response.json().get('data', {}).get('attributes', {}).get('stats', {})

    @staticmethod
    def check_url_safety(url):
        scan_id = VirusTotalService.scan_url(url)
        if not scan_id:
            return {'safe': False, 'message': "فشل الفحص", 'details': {}}

        stats = VirusTotalService.get_analysis(scan_id) or {}

        # Ensure default values exist
        return {
            'safe': stats.get('malicious', 0) == 0,
            'message': "آمن" if stats.get('malicious', 0) == 0 else "ضار",
            'details': {
                'harmless': stats.get('harmless', 0),
                'malicious': stats.get('malicious', 0),
                'suspicious': stats.get('suspicious', 0)
            }
        }
