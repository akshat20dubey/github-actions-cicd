import requests
import datetime

urls = [
    "https://google.com",
    "https://github.com",
    "https://python.org"
]

print("=" * 45)
print("   Server Availability Report")
print(f"   Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 45)

for url in urls:
    try:
        response = requests.get(url, timeout=5)
        print(f"  UP   {url} — {response.status_code}")
    except requests.exceptions.RequestException:
        print(f"  DOWN {url}")

print("=" * 45)
print("  Report complete!")
