# Project 03 - SQL Injection Vulnerability Assessment

## Objective

Assess and validate a SQL Injection vulnerability in the category parameter.

## Environment

-   Platform: PortSwigger Web Security Academy
-   Tool: Burp Suite Professional

## Steps

1.  Captured request using Burp Proxy.
2.  Send request to Repeater.
3.  Tested with `'`.
4.  Observed HTTP 500.
5.  Injected `' OR 1=1--+`.
6.  Observed HTTP 200.
7.  Confirmed hidden products and solved lab.

## Findings

The application is vulnerable to SQL Injection because user input is directly incorporated into SQL queries.

## Severity

High

## Remediation

-   Prepared statements
-   Input validation
-   Least privilege
-   Secure error handling

## Disclaimer

Testing was performed only in an authorized training environment.
