import requests

from pschecker.helpers import get_first_line_from_command

name = "Check SSL for domain names"
description = "Ensure that your apps can only be reached through HTTPS"


def run_check(config):
    success = True
    without_ssl = []
    bad_certs = []
    not_reachable = []
    for domain in config["domains"]:
        try:
            response = requests.get(
                "http://%s" % domain,
                allow_redirects=False
            )
            if response.status_code != 301:
                success = False
                without_ssl.append(domain)
            else:
                requests.get("https://%s" % domain, allow_redirects=False)
        except requests.exceptions.SSLError as e:
            success = False
            bad_certs.append(domain)
        except requests.exceptions.ConnectionError as e:
            success = False
            not_reachable.append(domain)

    if success:
        return {"status": "SUCCESS"}
    else:
        message = "Following errors were encountered:"
        if len(without_ssl) > 0:
            message += "\n- Accessible via http (%s)" % ", ".join(without_ssl)
        if len(bad_certs) > 0:
            message += "\n- Has wrong certificate (%s)" % ", ".join(bad_certs)
        if len(not_reachable) > 0:
            message += "\n- Is not reachable (%s)" % ", ".join(not_reachable)

        return {
            "status": "FAILURE",
            "message": message
        }
