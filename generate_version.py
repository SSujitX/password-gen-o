import subprocess


def get_version():
    try:
        version = (
            subprocess.run(
                ["git", "describe", "--tags", "--abbrev=0"], stdout=subprocess.PIPE
            )
            .stdout.decode("utf-8")
            .strip()
        )
        return version
    except Exception:
        return "0.0.0"  # Default version if no tag is found


version = get_version()
with open("VERSION", "w", encoding="utf-8") as version_file:
    version_file.write(f"{version}\n")

print(f"Version generated: {version}")
