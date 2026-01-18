import random
import time

def generate_transactions():
    print("🚀 Generando lote de transacciones bancarias...")
    transactions = []
    for i in range(1, 11):
        amount = random.randint(10, 5000)
        status = "EXITOSA" if amount < 4000 else "REVISIÓN MANUAL"
        transactions.append({"id": f"TRX-{i*100}", "monto": amount, "status": status})
        print(f"Procesando: {transactions[-1]}")
        time.sleep(1)
    return transactions

if __name__ == "__main__":
    data = generate_transactions()
    total = sum(t['monto'] for t in data)
    print(f"\n--- REPORTE FINAL ---")
    print(f"Monto total procesado: ${total}")
    print(f"Estado del Guardian: ACTIVO ✅")
