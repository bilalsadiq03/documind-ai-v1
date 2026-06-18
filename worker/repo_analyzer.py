import os

SUPPORTED_EXTENSIONS = {
    ".py",
    ".js",
    ".ts",
    ".tsx",
    ".jsx",
    ".json",
    ".md"
}

IGNORE_DIRS = {
    ".git",
    "node_modules",
    "dist",
    "build",
    "__pycache__",
    ".next"
}


def collect_files(repo_path):
    collected = []

    for root, dirs, files in os.walk(repo_path):

        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        for file in files:

            ext = os.path.splitext(file)[1]

            if ext not in SUPPORTED_EXTENSIONS:
                continue

            path = os.path.join(root, file)

            try:
                with open(
                    path,
                    "r",
                    encoding="utf-8",
                    errors="ignore"
                ) as f:

                    content = f.read()

                    collected.append(
                        {
                            "path": path,
                            "content": content
                        }
                    )

            except Exception:
                continue

    return collected


MAX_PROMPT_SIZE = 15000


def build_prompt(files):

    prompt = """
You are a senior software architect.

Analyze this repository and generate:

1. Project Overview
2. Tech Stack
3. Folder Structure
4. Features
5. Setup Instructions
6. API Endpoints (if applicable)
7. Architecture Overview

Repository Files:

"""

    total_size = len(prompt)

    for file in files:

        snippet = file["content"][:1500]

        block = f"""

FILE: {file['path']}

{snippet}

"""

        if total_size + len(block) > MAX_PROMPT_SIZE:
            break

        prompt += block
        total_size += len(block)

    return prompt