      ___           _     _ _     _           
     / _ \   ___  _| |_  (_) |__ (_)_ __  _ __ 
    / /_)/  / _ \/ _` |  | | '_ \| | '_ \| '__|
   / ___/  |  __/ (_| |  | | | | | | | | | |   
   \/       \___|\__,_|  |_|_| |_|_|_| |_|_|   

        A S H I H R I O   •   O S I N T


██████╗  ██████╗ ███████╗██╗███╗   ██╗████████╗
██╔══██╗██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝
██████╔╝██║   ██║███████╗██║██╔██╗ ██║   ██║   
██╔══██╗██║   ██║╚════██║██║██║╚██╗██║   ██║   
██████╔╝╚██████╔╝███████║██║██║ ╚████║   ██║   
╚═════╝  ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝   

              P R O J E C T   0


============================================================
OSINT – Ashihiro’s Recon Toolkit
============================================================

OSINT is a modular, script‑driven reconnaissance framework designed for fast, repeatable, and clean intelligence gathering. Everything is structured, predictable, and built for real workflows.

============================================================
FEATURES
============================================================

- Modular collectors for usernames, domains, IPs, emails, and more
- Unified CLI with consistent flags and output
- JSON, table, or file export
- Config‑driven API keys, rate limits, and module toggles
- Safe, passive OSINT only
- Pipeline‑ready output for dashboards or automation

============================================================
INSTALLATION
============================================================

From source:

    git clone https://example.com/ashihiro/osint.git
    cd osint
    python -m venv .venv
    source .venv/bin/activate   (Windows: .venv\Scripts\activate)
    pip install -r requirements.txt
    pip install -e .

Check installation:

    osint --help
    osint modules list

============================================================
USAGE
============================================================

Basic syntax:

    osint <resource-type> <value> [options]

Resource types:
    user
    domain
    ip
    email
    phone
    custom

Examples:

Username reconnaissance:

    osint user ashihiro --modules social,dev,forums --format table

Domain footprint:

    osint domain example.com --modules dns,whois,certs,subdomains,breaches --format json --output out/example.com.json

IP enrichment:

    osint ip 1.1.1.1 --modules geo,asn,blacklists --format table

============================================================
CONFIGURATION
============================================================

Config file location:

    ~/.config/osint/config.toml

Example:

    [core]
    concurrency = 8
    timeout     = 15
    user_agent  = "Ashihiro-OSINT/1.0"

    [output]
    default_format = "table"
    color          = true

    [modules]
    enabled  = ["social", "dev", "dns", "whois", "certs", "subdomains", "breaches", "geo", "asn", "blacklists"]
    disabled = []

    [secrets]
    github_token   = "ghp_..."
    shodan_api_key = "SHODAN_..."
    virustotal_key = "VT_..."

============================================================
MODULE EXAMPLE (REAL CODE)
============================================================

    # osint/modules/social/github.py

    from osint.core.module import Module
    from osint.core.result import Result
    import requests

    class GitHubModule(Module):
        name = "github"
        category = "social"
        description = "Enumerate GitHub profile and metadata for a username."

        def run(self, username: str) -> Result:
            url = f"https://api.github.com/users/{username}"
            resp = requests.get(url, timeout=self.config.timeout)

            if resp.status_code == 404:
                return self.result_empty(reason="User not found")

            resp.raise_for_status()
            data = resp.json()

            return Result(
                module=self.name,
                raw=data,
                summary={
                    "login": data.get("login"),
                    "name": data.get("name"),
                    "public_repos": data.get("public_repos"),
                    "followers": data.get("followers"),
                    "created_at": data.get("created_at"),
                    "html_url": data.get("html_url"),
                },
            )

Module registration:

    # osint/modules/social/__init__.py

    from .github import GitHubModule

    MODULES = [
        GitHubModule,
    ]

============================================================
CLI ENTRYPOINT
============================================================

    # osint/cli.py

    import argparse
    from osint.core.loader import load_modules
    from osint.core.runner import run_task
    from osint.core.output import render

    def main() -> None:
        parser = argparse.ArgumentParser(
            prog="osint",
            description="Ashihiro's modular OSINT console."
        )

        sub = parser.add_subparsers(dest="resource", required=True)

        # user
        user_p = sub.add_parser("user", help="Username reconnaissance")
        user_p.add_argument("value", help="Username to investigate")
        user_p.add_argument("--modules", help="Comma-separated module list", default=None)
        user_p.add_argument("--format", choices=["table", "json"], default="table")
        user_p.add_argument("--output", help="Write results to file")

        # TODO: domain, ip, email, etc.

        args = parser.parse_args()

        modules = load_modules(resource=args.resource, filter_string=args.modules)
        results = run_task(resource=args.resource, value=args.value, modules=modules)
        render(results, fmt=args.format, output_path=args.output)

    if __name__ == "__main__":
        main()

============================================================
PROJECT STRUCTURE
============================================================

    osint/
      ├─ osint/
      │   ├─ cli.py
      │   ├─ core/
      │   │   ├─ module.py
      │   │   ├─ runner.py
      │   │   ├─ output.py
      │   │   └─ config.py
      │   └─ modules/
      │       ├─ social/
      │       │   ├─ __init__.py
      │       │   └─ github.py
      │       ├─ dns/
      │       ├─ whois/
      │       └─ ...
      ├─ tests/
      ├─ README.md
      └─ pyproject.toml / setup.cfg

============================================================
ROADMAP
============================================================

- More modules (breaches, infra, social platforms)
- Full TUI dashboard
- Exporters: CSV, SQLite, webhook
- Python scripting API
- Live recon session mode

============================================================
END OF FILE
============================================================
