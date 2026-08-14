#!/usr/bin/env python3
"""Web Recon Automation Framework - passive/public-data reconnaissance."""
import argparse, json
from datetime import datetime, timezone
from recon.framework import run_recon
from reports.generator import write_reports

def main():
    parser = argparse.ArgumentParser(description="Passive web reconnaissance automation")
    parser.add_argument("target", help="Target domain or URL you are authorized to assess")
    parser.add_argument("-o", "--output", default="reports/output", help="Output directory")
    args = parser.parse_args()

    started = datetime.now(timezone.utc).isoformat()
    result = run_recon(args.target)
    result["metadata"] = {
        "target_input": args.target,
        "generated_at": started,
        "scope": "Passive/public-data reconnaissance only"
    }
    write_reports(result, args.output)
    print(json.dumps(result, indent=2, default=str))
    print(f"\nReports written to: {args.output}")

if __name__ == "__main__":
    main()
