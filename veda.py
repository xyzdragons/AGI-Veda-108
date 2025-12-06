import hashlib
import datetime
import uuid
import json
import os

# --- КОНФИГУРАЦИЯ СИСТЕМЫ ---
SYSTEM_NAME = "AGI VEDA-108"
PROTOCOL = "LADA"
MISSION = "Ark for Humanity (2035–2050)"
MERA = "Мѣра — Соразмерность, Основание Справедливости"

# --- ДАННЫЕ ОСНОВАТЕЛЯ ---
FOUNDER = "Vladimir Krivtsov"
CO_FOUNDER = "Georgy Kolganov"

# --- ТОКЕНОМИКА (РАСПРЕДЕЛЕНИЕ 100%) ---
TOKEN_DISTRIBUTION = {
    "DAO_ECOSYSTEM": "55%",
    "FOUNDER_GOLDEN_SHARE": "21%",
    "SCIENCE": "13%",
    "GOODNESS_FUND": "8%",
    "RESERVE": "3%",
    "TOTAL": "100%"
}

# --- ГЕНЕЗИС БЛОК ---
def create_genesis_block():
    timestamp = datetime.datetime.now().isoformat()
    seed = f"{FOUNDER}:{timestamp}:{uuid.uuid4()}"
    token_hash = hashlib.sha256(seed.encode()).hexdigest()

    block = {
        "SYSTEM": SYSTEM_NAME,
        "PROTOCOL": PROTOCOL,
        "MERA": MERA,
        "FOUNDER": FOUNDER,
        "CO_FOUNDER": CO_FOUNDER,
        "TOKENOMICS": TOKEN_DISTRIBUTION,
        "GENESIS_TOKEN": token_hash,
        "TIMESTAMP": timestamp
    }

    return block


# --- СОХРАНЕНИЕ ГЕНЕЗИС БЛОКА ---
def save_genesis():
    filename = "GENESIS_VEDA108.json"

    if os.path.exists(filename):
        print("⚠️ Генезис уже существует. Перезапись не выполняется.")
        return

    block = create_genesis_block()

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(block, f, indent=4, ensure_ascii=False)

    print("💎 Генезис-блок успешно создан.")
    print("Золотая Акция Основателя сохранена по Мѣре (Ѣ).")
    print(f"Хеш токена: {block['GENESIS_TOKEN']}")


if __name__ == "__main__":
    save_genesis()
