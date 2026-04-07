import datetime

def greet():
    now = datetime.datetime.now()
    print("=" * 40)
    print("  Hello from Akshat's CI/CD Pipeline!")
    print(f"  Run Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print("  Status: Pipeline is working ✅")
    print("=" * 40)

if __name__ == "__main__":
    greet()
