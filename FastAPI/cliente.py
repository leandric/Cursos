import csv
import sys
import requests


BASE_URL = "http://127.0.0.1:8000"
POST_URL = f"{BASE_URL}/livros/"  # <- repare na barra final


def main(csv_path: str) -> None:
    with open(csv_path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)

        required = {"autor", "titulo", "editora", "ano"}
        if not reader.fieldnames:
            print("CSV sem cabeçalho.")
            sys.exit(1)

        cols = {c.strip().lower() for c in reader.fieldnames}
        missing = required - cols
        if missing:
            print(f"CSV inválido. Faltando colunas: {sorted(missing)}")
            sys.exit(1)

        s = requests.Session()
        ok, fail = 0, 0

        for line_no, row in enumerate(reader, start=2):
            row_norm = {k.strip().lower(): (v or "").strip() for k, v in row.items()}

            # monta payload do POST
            try:
                payload = {
                    "autor": row_norm["autor"],
                    "titulo": row_norm["titulo"],
                    "editora": row_norm["editora"],
                    "ano": int(row_norm["ano"]),
                }
            except Exception as e:
                fail += 1
                print(f"[linha {line_no}] ❌ dados inválidos ({e}): {row}")
                continue

            r = s.post(POST_URL, json=payload, timeout=30)

            if r.status_code == 200:
                ok += 1
                data = r.json()
                print(f"[linha {line_no}] ✅ criado uuid={data.get('uuid')} titulo={payload['titulo']!r}")
            else:
                fail += 1
                try:
                    err = r.json()
                except Exception:
                    err = r.text
                print(f"[linha {line_no}] ❌ status={r.status_code} erro={err}")

        print("\nResumo:")
        print("Inseridos:", ok)
        print("Falhas:", fail)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python cliente.py livros.csv")
        sys.exit(1)
    main(sys.argv[1])
