import os


def create_directories():
    # 列出所有必要的資料夾
    dirs = [
        "docs",
        "scripts/initialization",
        "scripts/etl",
        "scripts/analysis",
        "scripts/scheduler",
        "scripts/tests",
        "src/db",
        "src/core"
    ]

    for d in dirs:
        if not os.path.exists(d):
            os.makedirs(d)
            print(f"Directory created: {d}")
        else:
            print(f"Directory exists: {d}")


if __name__ == "__main__":
    create_directories()
