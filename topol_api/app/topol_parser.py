def parse_response(hex_string):
    try:
        hex_string = hex_string.strip()
        data = bytes.fromhex(hex_string)
        if len(data) < 10:
            return {"error": "short data"}

        values = []
        for i in range(7, len(data) - 1, 2):
            val = int.from_bytes(data[i:i+2], byteorder="little", signed=False)
            values.append(val)

        phase_names = {
            0: "Aktivace",
            1: "Sedimentace",
            2: "Plnění dekanteru",
            3: "Odkalování",
            4: "Vypouštění",
            5: "Denitrifikace – plnění",
            6: "Denitrifikace – sedimentace",
            7: "Denitrifikace – recirkulace",
            8: "Spouštění"
        }

        phase_id = values[0]
        phase_name = phase_names.get(phase_id, "Neznámá fáze")

        return {
            "phase_id": phase_id,
            "phase_name": phase_name,
            "accumulation_level_cm": values[1],
            "blower_power_percent": round(values[2] / 10, 1),
            "error_flags_1": values[19] if len(values) > 19 else 0,
            "error_flags_2": values[20] if len(values) > 20 else 0,
            "error_flags_3": values[21] if len(values) > 21 else 0,
            "raw_hex": hex_string,
            "raw_values": values
        }
    except Exception as e:
        return {"error": str(e)}
