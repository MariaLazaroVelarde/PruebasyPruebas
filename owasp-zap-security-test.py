"""
Script de pruebas de seguridad OWASP ZAP para aplicaciones Spring Boot + Angular

Este script muestra cómo realizar pruebas de seguridad utilizando la API OWASP ZAP
para detectar vulnerabilidades comunes en su aplicación web.
"""

import requests
import json
import time
from urllib.parse import urljoin

class OWASPZAPSecurityTester:
    def __init__(self, zap_url="http://localhost:8081", api_key="TU_CLAVE_AQUI"):
        self.zap_url = zap_url
        self.api_url = f"{zap_url}/JSON"
        self.api_key = api_key
        self.target_url = "http://localhost:8080"
        self.frontend_url = "http://localhost:4201"

    def check_zap_connection(self):
        print("==============================================================")
        print("Starting OWASP ZAP Security Tests for Spring Boot + Angular Application")
        print("==============================================================")
        
        try:
            response = requests.get(f"{self.api_url}/core/view/version/", params={'apikey': self.api_key})
            if response.status_code == 200:
                print("✅ OWASP ZAP is accessible")
            else:
                print("❌ ZAP Connection Failed")
        except:
            print("❌ Cannot connect to ZAP. Make sure ZAP is running.")

    def spider_site(self, url):
        print(f"=== Spidering {url} ===")
        spider_response = requests.get(
            f"{self.api_url}/spider/action/scan/",
            params={'url': url, 'apikey': self.api_key}
        )

        if spider_response.status_code != 200:
            print(f"❌ Failed to start spidering: {spider_response.text}")
            return
        
        scan_id = spider_response.json().get("scan")
        print(f"   Spider started with scan ID: {scan_id}")

        while True:
            progress = requests.get(
                f"{self.api_url}/spider/view/status/",
                params={'scanId': scan_id, 'apikey': self.api_key}
            ).json().get("status")

            print(f"   Spider progress: {progress}%")
            if progress == "100":
                break
            time.sleep(2)
        
        print("✅ Spidering completed\n")

    def active_scan(self, url):
        print(f"=== Active Scanning {url} ===")
        scan_response = requests.get(
            f"{self.api_url}/ascan/action/scan/",
            params={'url': url, 'apikey': self.api_key}
        )

        if scan_response.status_code != 200:
            print(f"❌ Failed to start active scan: {scan_response.text}")
            return

        scan_id = scan_response.json().get("scan")
        print(f"   Active scan started with scan ID: {scan_id}")

        while True:
            progress = requests.get(
                f"{self.api_url}/ascan/view/status/",
                params={'scanId': scan_id, 'apikey': self.api_key}
            ).json().get("status")

            print(f"   Scan progress: {progress}%")
            if progress == "100":
                break
            time.sleep(2)

        print("✅ Active scanning completed\n")

    def get_alerts(self):
        print("=== Retrieving Security Alerts ===")
        alerts = requests.get(
            f"{self.api_url}/core/view/alerts/",
            params={'apikey': self.api_key}
        )

        if alerts.status_code != 200:
            print(f"❌ Failed to retrieve alerts: {alerts.text}")
            return

        data = alerts.json().get("alerts", [])

        if len(data) == 0:
            print("ℹ️  No security alerts found\n")
        else:
            print(f"⚠ Found {len(data)} alerts\n")
            for alert in data:
                print(f"- {alert['alert']} (Risk: {alert['risk']}) | URL: {alert['url']}")

    def run_tests(self):
        self.check_zap_connection()

        print("=== Accessing Target Application ===")
        try:
            requests.get(self.target_url, proxies={"http": self.zap_url})
            requests.get(self.frontend_url, proxies={"http": self.zap_url})
            print("✅ Accessed both endpoints through ZAP proxy")
        except:
            print("❌ Failed accessing target URLs")

        self.spider_site(self.target_url)
        self.spider_site(self.frontend_url)

        self.active_scan(self.target_url)

        self.get_alerts()


# ==========================
# MAIN EXECUTION
# ==========================
tester = OWASPZAPSecurityTester(
    zap_url="http://localhost:8081",
    api_key="337ssn885kd499812ps11v0hrg"
)
tester.run_tests()