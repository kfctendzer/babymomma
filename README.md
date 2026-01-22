ASHIHIRO — ADVANCED OSINT CONTROL PANEL
Owner: @9ukx

 ______             __        __  __        __                     
/      \           |  \      |  \|  \      |  \                    
|  $$$$$$\  _______ | $$____   \$$| $$____   \$$  ______    ______  
| $$__| $$ /       \| $$    \ |  \| $$    \ |  \ /      \  /      \ 
| $$    $$|  $$$$$$$| $$$$$$$\| $$| $$$$$$$\| $$|  $$$$$$\|  $$$$$$$\
| $$$$$$$$ \$$    \ | $$  | $$| $$| $$  | $$| $$| $$   \$$| $$  | $$
| $$  | $$ _\$$$$$$\| $$  | $$| $$| $$  | $$| $$| $$      | $$__/ $$
| $$  | $$|       $$| $$  | $$| $$| $$  | $$| $$| $$       \$$    $$
 \$$   \$$ \$$$$$$$  \$$   \$$ \$$ \$$   \$$ \$$ \$$        \$$$$$$ 

====================================================================
OVERVIEW
====================================================================

Ashihrio is a precision-built, analyst-focused OSINT Control Panel designed for 
researchers, threat hunters, and power-users who demand clarity, speed, and 
total operational control over their reconnaissance workflows.

Instead of scattering tools across terminals, scripts, and random GUIs, 
Ashihrio consolidates:

- Reconnaissance utilities
- Metadata and information extraction
- Builder and packaging tools
- Logging and monitoring

into a single, cohesive environment with a clean, modern interface.

Every part of Ashihrio reflects a core philosophy:

- Minimal noise.
- Maximum capability.
- Absolute control.

====================================================================
CORE PHILOSOPHY
====================================================================

1. Clean, Modern UI
   - No clutter, no unnecessary widgets, no visual noise.
   - Focus on readability, contrast, and intuitive layout.
   - Dark-theme friendly design for long sessions.

2. Fast Execution
   - Minimal blocking operations where possible.
   - Logical grouping of tasks to reduce friction.
   - Designed to keep the operator “in flow” instead of fighting the tool.

3. Modular Architecture
   - OSINT modules are logically separated.
   - Easy to extend with new modules or external tools.
   - Encourages experimentation without breaking the core.

4. Cross-Platform Friendly
   - Built on Python and CustomTkinter.
   - Aims to run wherever Python and Tkinter are available.
   - Windows-specific enhancements are optional, not mandatory.

5. Analyst-First Design
   - Built around real workflows, not just demos.
   - Emphasis on clarity of output and repeatability of actions.
   - Designed to be a control panel, not a toy.

====================================================================
FEATURES
====================================================================

1. Reconnaissance Suite
   - Username Enumeration:
     - Check presence of usernames across multiple platforms and services.
     - Useful for footprinting, correlation, and identity mapping.

   - Email Footprinting:
     - Basic checks and metadata gathering around email addresses.
     - Can assist in profiling, breach checks (where legally permitted), and 
       pivoting to other identifiers.

   - Passive Domain Intelligence:
     - Basic lookups and metadata extraction for domains.
     - Intended for reconnaissance, not active exploitation.

   - Metadata Extraction:
     - Extracts metadata from supported files (where implemented).
     - Useful for attribution, timeline building, and context gathering.

2. Builder System
   - Automation Bundles:
     - Combine selected modules into a single, repeatable workflow.
     - Ideal for standardizing recurring tasks.

   - Module Customization:
     - Enable/disable modules based on your current operation.
     - Adjust parameters and behavior where supported.

   - Standalone Builds:
     - Integrate with tools like PyInstaller or cx-Freeze (optional).
     - Package workflows into distributable artifacts for controlled environments.

   - Dependency Management:
     - Encourages use of virtual environments.
     - Keeps project dependencies isolated and clean.

3. Logging & Monitoring
   - System Information (via psutil):
     - Basic system stats for context and diagnostics.
     - Useful when running on multiple hosts or environments.

   - Event Logging:
     - Logs key actions, module runs, and outcomes.
     - Helps with auditability and repeatability.

   - Optional Encrypted Logs (via cryptography):
     - Where implemented, logs can be encrypted for sensitive workflows.
     - Intended for environments where log confidentiality matters.

4. UI Layer (CustomTkinter)
   - Modern Interface:
     - Uses CustomTkinter for a more polished look than classic Tkinter.
     - Smooth widgets, better theming, and a more modern feel.

   - Theme Support:
     - Dark/light themes where configured.
     - Visual consistency across modules.

   - Cross-Platform:
     - Built on top of Tkinter, which is widely available.
     - Aims to behave consistently across supported platforms.

====================================================================
DEPENDENCIES
====================================================================

Core Python Packages Used:

- psutil
- cryptography
- requests
- requests-toolbelt
- colorama
- pillow
- pycryptodomex
- customtkinter

Windows-Specific / Optional:

- pypiwin32 (Windows only)
- wmi (Windows only)

These Windows-specific packages are only required if you are using 
Windows-specific functionality. On Linux or other platforms, they can be 
safely omitted as long as the code paths that require them are not executed.

====================================================================
INSTALLATION
====================================================================

1. Clone the Repository

   Use Git to clone the project:

   git clone https://github.com/your/repo.git
   cd Ashihiro

   Replace the URL with your actual repository location if different.

2. Create a Virtual Environment

   It is strongly recommended to use a virtual environment to keep 
   dependencies isolated:

   python -m venv venv

   Activate it:

   - On Linux/macOS:
     source venv/bin/activate

   - On Windows (PowerShell):
     .\venv\Scripts\Activate.ps1

3. Install Dependencies

   If you have a requirements.txt file:

   pip install -r requirements.txt

   Or install manually:

   pip install psutil cryptography requests requests-toolbelt colorama pillow pycryptodomex customtkinter

   On Windows, if needed:

   pip install pypiwin32 wmi

4. Run the Builder

   Once dependencies are installed and the virtual environment is active:

   python builder.pyw

   This will launch the Ashihiro builder/control panel interface.

====================================================================
PROJECT STRUCTURE
====================================================================

A typical layout might look like:

Ashihrio/
│
├── builder.pyw        # Main GUI builder / control panel entry point
├── core/              # Core logic, shared utilities, base classes
├── modules/           # OSINT modules and feature-specific components
├── assets/            # Icons, images, UI assets, branding
├── logs/              # Runtime logs and output (if enabled)
└── README.md          # Project documentation (this file)

This structure is intentionally modular so that:

- New modules can be added under modules/
- Shared logic can live in core/
- Visual assets are centralized in assets/
- Logs are kept separate for easier review and cleanup

====================================================================
USAGE
====================================================================

1. Launching the Control Panel

   With your virtual environment active:

   python builder.pyw

2. Configuring Your Workflow

   Inside the GUI, you can:

   - Enable or disable specific OSINT modules.
   - Configure module parameters (where supported).
   - Choose output directories for logs and results.
   - Save or load configurations (if implemented).

3. Running OSINT Tasks

   - Trigger individual modules for targeted tasks.
   - Run combined workflows for broader reconnaissance.
   - Review logs and outputs for each run.

4. Extending Ashihiro

   - Add new modules under modules/.
   - Integrate external tools or APIs.
   - Adjust the UI to expose new capabilities.

====================================================================
BRANDING
====================================================================

Ashihrio is a personal project by:

   Owner: @9ukx

It is built with a focus on:

- Identity
- Precision
- Clean engineering
- Aesthetic discipline

If you fork, extend, or redistribute this project, please preserve 
attribution to Ashihiro and @9ukx in the documentation and interface 
where appropriate.

====================================================================
LEGAL & ETHICAL NOTICE
====================================================================

Ashihrio is intended for:

- Educational use
- Research
- Defensive OSINT
- Legitimate security analysis with proper authorization

You are solely responsible for how you use this tool.

You must:

- Comply with all applicable laws and regulations in your jurisdiction.
- Obtain proper authorization before performing any form of reconnaissance 
  or data gathering against systems, services, or individuals.
- Respect privacy, terms of service, and ethical guidelines.

The creator and contributors of Ashihiro do not assume responsibility for 
misuse, abuse, or illegal activity conducted with this software.

====================================================================
SUPPORT & CONTRIBUTION
====================================================================

If you find Ashihiro useful, interesting, or inspiring, you can:

- Star the repository to show support.
- Open issues for bugs, ideas, or feature requests.
- Contribute modules, improvements, or documentation.
- Share feedback on workflows, UI, and overall experience.

Your input helps shape the evolution of this control panel and pushes it 
toward even greater precision, capability, and refinement.

====================================================================
END OF README
====================================================================
