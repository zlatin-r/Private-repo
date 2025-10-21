import subprocess

def git_auto_push(message="solutions added", branch="main"):
    try:
        # Stage all changes
        subprocess.run(["git", "add", "."], check=True)
        
        # Commit changes with the provided message
        subprocess.run(["git", "commit", "-m", message], check=True)
        
        # Push to the specified branch
        subprocess.run(["git", "push", "origin", branch], check=True)
        
        print(f"✅ Successfully pushed to {branch} with message: '{message}'")
    except subprocess.CalledProcessError:
        print("❌ Error: Git command failed.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

if __name__ == "__main__":
    git_auto_push()
