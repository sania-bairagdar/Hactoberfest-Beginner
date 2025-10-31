import argparse
import json
import sys

#!/usr/bin/env python3
import urllib.parse
import urllib.request

def fetch(url, timeout=10):
    try:
        with urllib.request.urlopen(url, timeout=timeout) as resp:
            return json.load(resp)
    except Exception as e:
        print("Network error:", e, file=sys.stderr)
        sys.exit(1)

def fmt_number(x):
    s = f"{x:.8f}"
    s = s.rstrip("0").rstrip(".")
    return s

def convert(amount, frm, to):
    params = {"from": frm.upper(), "to": to.upper(), "amount": amount}
    url = "https://api.exchangerate.host/convert?" + urllib.parse.urlencode(params)
    data = fetch(url)
    if not data.get("success", True) and "error" in data:
        print("API error:", data["error"], file=sys.stderr)
        sys.exit(1)
    if "result" not in data:
        print("Unexpected API response", file=sys.stderr)
        sys.exit(1)
    result = data["result"]
    rate = data.get("info", {}).get("rate")
    return result, rate

def main():
    p = argparse.ArgumentParser(prog="currency_converter", description="Convert one currency to another")
    p.add_argument("amount", nargs="?", help="amount to convert")
    p.add_argument("from_currency", nargs="?", help="source currency code (e.g. USD)")
    p.add_argument("to_currency", nargs="?", help="target currency code (e.g. EUR)")
    args = p.parse_args()
    if args.amount and args.from_currency and args.to_currency:
        try:
            amt = float(args.amount)
        except:
            print("Invalid amount", file=sys.stderr); sys.exit(1)
        frm = args.from_currency
        to = args.to_currency
    else:
        try:
            amt = float(input("Amount: ").strip())
            frm = input("From (currency code): ").strip()
            to = input("To (currency code): ").strip()
        except Exception:
            print("Invalid input", file=sys.stderr); sys.exit(1)
    result, rate = convert(amt, frm, to)
    amt_s = fmt_number(amt)
    res_s = fmt_number(result)
    if rate:
        rate_s = fmt_number(rate)
        print(f"{amt_s} {frm.upper()} = {res_s} {to.upper()} (rate: {rate_s})")
    else:
        print(f"{amt_s} {frm.upper()} = {res_s} {to.upper()}")

if __name__ == "__main__":
    main()