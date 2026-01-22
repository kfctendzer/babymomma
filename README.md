============================================================
OSINT – Ashihiro’s Recon Toolkit
============================================================

A clean, modular open‑source intelligence framework designed for fast,
repeatable reconnaissance. Simple structure, predictable output, and
easy integration into automation pipelines.

============================================================
FEATURES
============================================================
• Username, domain, IP, email, and phone lookups
• Modular collector system
• JSON or table output
• Config‑driven API keys and settings
• Passive OSINT only (no active attacks)
• Pipeline‑friendly output

============================================================
INSTALLATION
============================================================
Clone and install:

    git clone https://example.com/osint.git
    cd osint
    python -m venv .venv
    source .venv/bin/activate   (Windows: .venv\Scripts\activate)
    pip install -r requirements.txt
    pip install -e .

Check:

    osint --help
    osint modules list

============================================================
USAGE
============================================================
Syntax:

    osint <resource-type> <value> [options]

Resource types:
    user, domain, ip, email, phone, custom

Examples:

    osint user ashihiro --modules social,dev --format table
    osint domain example.com --modules dns,whois --format json
    osint ip 1.1.1.1 --modules geo,asn --format table

============================================================
CONFIGURATION
============================================================
Config file:

    ~/.config/osint/config.toml

Example:

    [core]
    concurrency = 8
    timeout = 15

    [output]
    default_format = "table"
    color = true

    [modules]
    enabled = ["social", "dns", "whois", "geo", "asn"]

    [secrets]
    github_token = "..."
    shodan_api_key = "..."
    virustotal_key = "..."

============================================================
MODULE EXAMPLE
============================================================
    # osint/modules/social/github.py

    from osint.core.module import Module
    from osint.core.result import Result
    import requests

    class GitHubModule(Module):
        name = "github"
        category = "social"

        def run(self, username: str) -> Result:
            url = f"https://api.github.com/users/{username}"
            resp = requests.get(url, timeout=self.config.timeout)

            if resp.status_code == 404:
                return self.result_empty("User not found")

            data = resp.json()

            return Result(
                module=self.name,
                raw=data,
                summary={
                    "login": data.get("login"),
                    "name": data.get("name"),
                    "public_repos": data.get("public_repos"),
                    "followers": data.get("followers"),
                },
            )

============================================================
CLI ENTRYPOINT
============================================================
    # osint/cli.py

    import argparse
    from osint.core.loader import load_modules
    from osint.core.runner import run_task
    from osint.core.output import render

    def main():
        parser = argparse.ArgumentParser(
            prog="osint",
            description="Modular OSINT console."
        )

        sub = parser.add_subparsers(dest="resource", required=True)

        user_p = sub.add_parser("user")
        user_p.add_argument("value")
        user_p.add_argument("--modules")
        user_p.add_argument("--format", default="table")
        user_p.add_argument("--output")

        args = parser.parse_args()

        modules = load_modules(args.resource, args.modules)
        results = run_task(args.resource, args.value, modules)
        render(results, args.format, args.output)

    if __name__ == "__main__":
        main()

============================================================
DIRECTORY STRUCTURE
============================================================
    osint/
    ├── README.md
    ├── requirements.txt
    ├── pyproject.toml
    ├── setup.cfg
    ├── out/
    ├── tests/
    └── osint/
        ├── cli.py
        ├── core/
        │   ├── module.py
        │   ├── runner.py
        │   ├── output.py
        │   └── config.py
        └── modules/
            ├── social/
            │   └── github.py
            ├── dns/
            ├── whois/
            ├── geo/
            ├── asn/
            └── blacklists/

============================================================
END OF FILE
============================================================
