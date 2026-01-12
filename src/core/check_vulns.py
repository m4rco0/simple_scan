import requests

def checkVuln(servico, versao):
    print("[+] Inicando checagem")

    params = {
            "keywordSearch": f"{servico} {versao}"
        }

    r = requests.get("https://services.nvd.nist.gov/rest/json/cves/2.0", params=params)
    if r.status_code == 200:
        print("Sucesso")
        dados = r.json()
        vulns = dados.get("vulnerabilities")
        for v in vulns:
            print(f"CVE: {v['cve']['id']}")

    else:
        print("Falhou")
